# Copyright 2004-2012 Tom Rothamel <pytom@bishoujo.us>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import renpy
import os.path
from pickle import loads
from cStringIO import StringIO
import sys
import types

try:
    import android.apk
    apks = [ 
        android.apk.APK(prefix='assets/x-game/'),
        android.apk.APK(prefix='assets/x-common/'),
        ]
except ImportError:
    apks = [ ]

# Files on disk should be checked before archives. Otherwise, among
# other things, using a new version of bytecode.rpyb will break.
archives = [ ]

# The value of renpy.config.archives the last time index_archives was
# run.
old_config_archives = None

# A map from lower-case filename to regular-case filename.
lower_map = { }

def index_archives():
    """
    Loads in the indexes for the archive files. Also updates the lower_map.
    """

    # Update lower_map.
    lower_map.clear()
    
    for dir, fn in listdirfiles(): #@ReservedAssignment
        lower_map[fn.lower()] = fn

    # Index the archives.
    
    global old_config_archives

    if old_config_archives == renpy.config.archives:
        return

    old_config_archives = renpy.config.archives[:]
    
    global archives
    archives = [ ]

    for prefix in renpy.config.archives:

        fn = transfn(prefix + ".rpa")

        try:
            fn = transfn(prefix + ".rpa")
            f = file(fn, "rb")
            l = f.readline()

            # 3.0 Branch.
            if l.startswith("RPA-3.0 "):
                offset = int(l[8:24], 16)
                key = int(l[25:33], 16)
                f.seek(offset)
                index = loads(f.read().decode("zlib"))

                # Deobfuscate the index.

                for k in index.keys():

                    if len(index[k][0]) == 2:
                        index[k] = [ (offset ^ key, dlen ^ key) for offset, dlen in index[k] ]
                    else:
                        index[k] = [ (offset ^ key, dlen ^ key, start) for offset, dlen, start in index[k] ]

                archives.append((prefix, index))
                
                f.close()
                continue

            # 2.0 Branch.
            if l.startswith("RPA-2.0 "):
                offset = int(l[8:], 16)
                f.seek(offset)
                index = loads(f.read().decode("zlib"))
                archives.append((prefix, index))
                f.close()
                continue

            # 1.0 Branch.
        
            f.close()
            
            fn = transfn(prefix + ".rpi")
            index = loads(file(fn, "rb").read().decode("zlib")) 
            archives.append((prefix, index))

        except:
            if renpy.config.debug:
                raise

def walkdir(dir): #@ReservedAssignment
    rv = [ ]

    if not os.path.exists(dir) and not renpy.config.developer:
        return rv

    for i in os.listdir(dir):
        if i[0] == ".":
            continue

        if os.path.isdir(dir + "/" + i):
            for fn in walkdir(dir + "/" + i):
                rv.append(i + "/" + fn)
        else:
            rv.append(i)

    return rv
        
    
def listdirfiles():
    """
    Returns a list of directory, file tuples known to the system. If
    the file is in an archive, the directory is None.
    """

    rv = [ ]

    seen = set()
    
    for apk in apks:
        for f in apk.list():
            
            # Strip off the "x-" in front of each filename, which is there
            # to ensure that aapt actually includes every file.
            f = "/".join(i[2:] for i in f.split("/"))
            
            if f not in seen:
                rv.append((None, f))
    
    for i in renpy.config.searchpath:
        i = os.path.join(renpy.config.basedir, i)
        for j in walkdir(i):
            if j not in seen:            
                rv.append((i, j))
                seen.add(j)

    for _prefix, index in archives:
        for j in index.iterkeys():            
            if j not in seen:            
                rv.append((None, j))
                seen.add(j)
            
            
    return rv
    

class SubFile(object):

    def __init__(self, f, base, length, start):
        self.f = f
        self.base = base
        self.offset = 0
        self.length = length
        self.start = start

        if start is None:
            self.name = self.f.name
        else:
            self.name = None
            
        self.f.seek(self.base)

    def read(self, length=None):

        maxlength = self.length - self.offset

        if length is not None:
            length = min(length, maxlength)
        else:
            length = maxlength

        rv1 = self.start[self.offset:self.offset + length]
        length -= len(rv1)
        self.offset += len(rv1)

        if length:
            rv2 = self.f.read(length)        
            self.offset += len(rv2)
        else:
            rv2 = ""

        return (rv1 + rv2)

    def readline(self, length=None):

        maxlength = self.length - self.offset
        if length is not None:
            length = min(length, maxlength)
        else:
            length = maxlength

        # If we're in the start, then read the line ourselves.
        if self.offset < len(self.start):
            rv = ''

            while length:
                c = self.read(1)
                rv += c
                if c == '\n':
                    break
                length -= 1

            return rv
                
        # Otherwise, let the system read the line all at once.
        rv = self.f.readline(length)

        self.offset += len(rv)

        return rv

    def readlines(self, length=None):
        rv = [ ]

        while True:
            l = self.readline(length)

            if not l:
                break

            if length is not None:
                length -= len(l)
                if l < 0:
                    break

            rv.append(l)

        return rv

    def xreadlines(self):
        return self

    def __iter__(self):
        return self

    def next(self): #@ReservedAssignment
        rv = self.readline()

        if not rv:
            raise StopIteration()

        return rv
    
    def flush(self):
        return

    
    def seek(self, offset, whence=0):

        if whence == 0:
            offset = offset
        elif whence == 1:
            offset = self.offset + offset
        elif whence == 2:
            offset = self.length + offset

        if offset > self.length:
            offset = self.length

        self.offset = offset
            
        offset = offset - len(self.start)
        if offset < 0:
            offset = 0
            
        self.f.seek(offset + self.base)

    def tell(self):
        return self.offset

    def close(self):
        self.f.close()

    def write(self, s):
        raise Exception("Write not supported by SubFile")
    

def load(name):
    """
    Returns an open python file object of the given type.
    """

    name = lower_map.get(name.lower(), name)
    
    if renpy.config.reject_backslash and "\\" in name:
        raise Exception("Backslash in filename, use '/' instead: %r" % name)

    if renpy.config.file_open_callback:
        rv = renpy.config.file_open_callback(name)
        if rv is not None:
            return rv
    
    # Look for the file in the apk.
    for apk in apks:
        prefixed_name = "/".join("x-" + i for i in name.split("/"))
        
        try:
            return apk.open(prefixed_name)
        except IOError:
            pass
    
    # Look for the file directly.
    if not renpy.config.force_archives:
        try:
            fn = transfn(name)
            return file(fn, "rb")
        except:
            pass

    # Look for it in archive files.
    for prefix, index in archives:
        if not name in index:
            continue

        f = file(transfn(prefix + ".rpa"), "rb")

        data = [ ]

        # Direct path.
        if len(index[name]) == 1:

            t = index[name][0]
            if len(t) == 2:
                offset, dlen = t
                start = ''
            else:
                offset, dlen, start = t

            rv = SubFile(f, offset, dlen, start)

        # Compatability path.
        else:
            for offset, dlen in index[name]:           
                f.seek(offset)
                data.append(f.read(dlen))

            rv = StringIO(''.join(data))
            f.close()
            
        return rv

    raise IOError("Couldn't find file '%s'." % name)

loadable_cache = { }

def loadable(name):
    """
    Returns True if the name is loadable with load, False if it is not.
    """

    name = lower_map.get(name.lower(), name)
    
    if name in loadable_cache:
        return loadable_cache[name]

    try:
        transfn(name)
        loadable_cache[name] = True
        return True
    except:
        pass

    for _prefix, index in archives:
        if name in index:
            loadable_cache[name] = True
            return True

    loadable_cache[name] = False
    return False
    

def transfn(name):
    """
    Tries to translate the name to a file that exists in one of the
    searched directories.
    """

    name = lower_map.get(name.lower(), name)
    
    if renpy.config.reject_backslash and "\\" in name:
        raise Exception("Backslash in filename, use '/' instead: %r" % name)

    if isinstance(name, str):
        name = name.decode("utf-8")
    
    for d in renpy.config.searchpath:
        fn = os.path.join(renpy.config.basedir, d, name)

        if os.path.exists(fn):
            return fn

    raise Exception("Couldn't find file '%s'." % name)


def get_mtime(name):
    """
    Returns the time the file m was last modified, or 0 if it
    doesn't exist or is archived.
    """

    try:
        fn = transfn(name)
        return os.path.getmtime(fn)
    except:
        return 0

class RenpyImporter(object):
    """
    An importer, that tries to load modules from the places where Ren'Py
    searches for data files.
    """

    def __init__(self, prefix=""):
        self.prefix = ""

    def translate(self, fullname, prefix=""):
        
        fn = prefix + fullname.replace(".", "/")
        
        if loadable(fn + ".py"):
            return fn + ".py"

        if loadable(fn + "/__init__.py"):
            return fn + "/__init__.py"

        return None

    def find_module(self, fullname, path=None):
        if path is not None:
            for i in path:
                if self.translate(fullname, i):
                    return RenpyImporter(i)
        
        if self.translate(fullname):
            return self

    def load_module(self, fullname):

        filename = self.translate(fullname, self.prefix)
        
        mod = sys.modules.setdefault(fullname, types.ModuleType(fullname))
        mod.__name__ = fullname
        mod.__file__ = filename
        mod.__loader__ = self

        if filename.endswith("__init__.py"):
            mod.__path__ = [ filename[:-len("__init__.py")] ]

        source = load(filename).read().decode("utf8")
        if source and source[0] == u'\ufeff':
            source = source[1:]
        source = source.encode("raw_unicode_escape")
        
        source = source.replace("\r", "")
        code = compile(source, filename, 'exec')
        exec code in mod.__dict__
        return mod

    def get_data(self, filename):
        return load(filename).read()

sys.meta_path.append(RenpyImporter())
