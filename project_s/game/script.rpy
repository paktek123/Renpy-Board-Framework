init:
    define e = Character('Eileen', color="#c8ffc8")
    
    ######## Outer frame #########
    
    # Row east
    image tile1 = "tile4.png"
    image tile2 = "tile4.png"
    image tile3 = "tile4.png"
    image tile4 = "tile4.png"
    image tile5 = "tile4.png"
    
    # Row south
    image tile5 = "tile4.png"
    image tile6 = "tile4.png"
    image tile7 = "tile4.png"
    image tile8 = "tile4.png"
    image tile9 = "tile4.png"
    
    # Row west
    image tile10 = "tile4.png"
    image tile11 = "tile4.png"
    image tile12 = "tile4.png"
    image tile13 = "tile4.png"
    image tile14 = "tile4.png"
    
    # Row north
    image tile15 = "tile4.png"
    image tile16 = "tile4.png"
    image tile17 = "tile4.png"
    image tile18 = "tile4.png"
    image tile19 = "tile4.png"
    
    ###### Inner frame ########
    
    # Middle horizontal
    image tile20 = "tile4.png"
    image tile21 = "tile4.png"
    image tile22 = "tile4.png" # Neutral
    image tile23 = "tile4.png"
    image tile24 = "tile4.png"
    
    # Middle Vertical
    image tile25 = "tile4.png"
    image tile26 = "tile4.png"
    image tile27 = "tile4.png"
    
    image dot = "dot.png"
    image arrow1 = "arrow1.png"
    image arrow1h = "arrow1h.png"
    image arrow2 = "arrow2.png"
    image arrow2h = "arrow2h.png"
    image arrow3 = "arrow3.png"
    image arrow3h = "arrow3h.png"
    image arrow4 = "arrow4.png"
    image arrow4h = "arrow4h.png"
    image tiler1 = "tile4r.png"
    image tiler2 = "tile4r.png"
    image tiler3 = "tile4r.png"
    image tiler4 = "tile4r.png"
    image tiler5 = "tile4r.png"

    # Row east
    $ a001 = Position(xpos=85, xanchor=0, ypos=140, yanchor=0)
    $ a002 = Position(xpos=85, xanchor=0, ypos=230, yanchor=0)
    $ a003 = Position(xpos=85, xanchor=0, ypos=320, yanchor=0)
    $ a004 = Position(xpos=85, xanchor=0, ypos=410, yanchor=0)
    $ a005 = Position(xpos=85, xanchor=0, ypos=500, yanchor=0)
    
    # Row south
    $ a006 = Position(xpos=175, xanchor=0, ypos=500, yanchor=0)
    $ a007 = Position(xpos=265, xanchor=0, ypos=500, yanchor=0)
    $ a008 = Position(xpos=355, xanchor=0, ypos=500, yanchor=0)
    $ a009 = Position(xpos=445, xanchor=0, ypos=500, yanchor=0)
    $ a010 = Position(xpos=535, xanchor=0, ypos=500, yanchor=0)
    
    # Row west
    $ a011 = Position(xpos=625, xanchor=0, ypos=500, yanchor=0)
    $ a012 = Position(xpos=625, xanchor=0, ypos=410, yanchor=0)
    $ a013 = Position(xpos=625, xanchor=0, ypos=320, yanchor=0)
    $ a014 = Position(xpos=625, xanchor=0, ypos=230, yanchor=0)
    $ a015 = Position(xpos=625, xanchor=0, ypos=140, yanchor=0)
    
    # Row North
    $ a016 = Position(xpos=535, xanchor=0, ypos=140, yanchor=0)
    $ a017 = Position(xpos=445, xanchor=0, ypos=140, yanchor=0)
    $ a018 = Position(xpos=355, xanchor=0, ypos=140, yanchor=0)
    $ a019 = Position(xpos=265, xanchor=0, ypos=140, yanchor=0)
    $ a020 = Position(xpos=175, xanchor=0, ypos=140, yanchor=0)
    
    # Middle Horizontal
    $ a021 = Position(xpos=175, xanchor=0, ypos=320, yanchor=0)
    $ a022 = Position(xpos=265, xanchor=0, ypos=320, yanchor=0)
    $ a023 = Position(xpos=355, xanchor=0, ypos=320, yanchor=0)
    $ a024 = Position(xpos=445, xanchor=0, ypos=320, yanchor=0)
    $ a025 = Position(xpos=535, xanchor=0, ypos=320, yanchor=0)
    
    # Middle Vertical
    $ a026 = Position(xpos=355, xanchor=0, ypos=230, yanchor=0)
    $ a027 = Position(xpos=355, xanchor=0, ypos=410, yanchor=0)
    
    # Dot pos
    $ d001 = Position(xpos=105, xanchor=0, ypos=150, yanchor=0)
    $ d002 = Position(xpos=105, xanchor=0, ypos=240, yanchor=0)
    $ d003 = Position(xpos=105, xanchor=0, ypos=330, yanchor=0)
    $ d004 = Position(xpos=105, xanchor=0, ypos=420, yanchor=0)
    $ d005 = Position(xpos=105, xanchor=0, ypos=510, yanchor=0)
    
    $ d006 = Position(xpos=195, xanchor=0, ypos=510, yanchor=0)
    $ d007 = Position(xpos=285, xanchor=0, ypos=510, yanchor=0)
    $ d008 = Position(xpos=375, xanchor=0, ypos=510, yanchor=0)
    $ d009 = Position(xpos=465, xanchor=0, ypos=510, yanchor=0)
    $ d010 = Position(xpos=555, xanchor=0, ypos=510, yanchor=0)
    
    $ d011 = Position(xpos=645, xanchor=0, ypos=510, yanchor=0)
    $ d012 = Position(xpos=645, xanchor=0, ypos=420, yanchor=0)
    $ d013 = Position(xpos=645, xanchor=0, ypos=330, yanchor=0)
    $ d014 = Position(xpos=645, xanchor=0, ypos=240, yanchor=0)
    $ d015 = Position(xpos=645, xanchor=0, ypos=150, yanchor=0)
    
    $ d016 = Position(xpos=555, xanchor=0, ypos=150, yanchor=0)
    $ d017 = Position(xpos=465, xanchor=0, ypos=150, yanchor=0)
    $ d018 = Position(xpos=375, xanchor=0, ypos=150, yanchor=0)
    $ d019 = Position(xpos=285, xanchor=0, ypos=150, yanchor=0)
    $ d020 = Position(xpos=195, xanchor=0, ypos=150, yanchor=0)
    
    $ d021 = Position(xpos=195, xanchor=0, ypos=330, yanchor=0)
    $ d022 = Position(xpos=285, xanchor=0, ypos=330, yanchor=0)
    $ d023 = Position(xpos=375, xanchor=0, ypos=330, yanchor=0)
    $ d024 = Position(xpos=465, xanchor=0, ypos=330, yanchor=0)
    $ d025 = Position(xpos=555, xanchor=0, ypos=330, yanchor=0)
    
    $ d026 = Position(xpos=375, xanchor=0, ypos=240, yanchor=0)
    $ d027 = Position(xpos=375, xanchor=0, ypos=420, yanchor=0)

    image black = "#000000"
    $ move = 1
    $ roll = 0
    $ direction = 270
    $ target = 1

# The game starts here.
label start:
    scene black
    
    # Row West
    show tile1 at a001
    show tile2 at a002
    show tile3 at a003
    show tile4 at a004
    show tile5 at a005
    
    # Row south
    show tile6 at a006
    show tile7 at a007
    show tile8 at a008
    show tile9 at a009
    show tile10 at a010
    
    # Row east
    show tile11 at a011
    show tile12 at a012
    show tile13 at a013
    show tile14 at a014
    show tile15 at a015
    
    # Row north
    show tile16 at a016
    show tile17 at a017
    show tile18 at a018
    show tile19 at a019
    show tile20 at a020
    
    # Middle horizontal
    show tile21 at a021
    show tile22 at a022
    show tile23 at a023
    show tile24 at a024
    show tile25 at a025
    
    # Middle Vertical
    show tile26 at a026
    show tile27 at a027
    
    call map
    jump mover
    
label map:
    if move == 1:
        show dot at d001
    elif move == 2:
        show dot at d002
    elif move == 3:
        show dot at d003
    elif move == 4:
        show dot at d004
    elif move == 5:
        show dot at d005
    elif move == 6:
        show dot at d006
    elif move == 7:
        show dot at d007
    elif move == 8:
        show dot at d008
    elif move == 9:
        show dot at d009
    elif move == 10:
        show dot at d010
    elif move == 11:
        show dot at d011  
    elif move == 12:
        show dot at d012
    elif move == 13:
        show dot at d013
    elif move == 14:
        show dot at d014  
    elif move == 15:
        show dot at d015
    elif move == 16:
        show dot at d016
    elif move == 17:
        show dot at d017
    elif move == 18:
        show dot at d018
    elif move == 19:
        show dot at d019  
    elif move == 20:
        show dot at d020
    elif move == 21:
        show dot at d021
    elif move == 22:
        show dot at d022
    elif move == 23:
        show dot at d023
    elif move == 24:
        show dot at d024  
    elif move == 25:
        show dot at d025
    elif move == 26:
        show dot at d026    
    elif move == 27:
        show dot at d027
    elif move == 28:
        $ move = 1
        call map
    return

label mover:
    python:
        ui.imagebutton("arrow1.png", "arrow1h.png", clicked=ui.returns("1"), xpos=90,ypos=40)
        ui.imagebutton("arrow2.png", "arrow2h.png", clicked=ui.returns("1"), xpos=50,ypos=40)
        ui.imagebutton("arrow3.png", "arrow3h.png", clicked=ui.returns("1"), xpos=71,ypos=60)
        ui.imagebutton("arrow4.png", "arrow4h.png", clicked=ui.returns("1"), xpos=66,ypos=25)
        ui.textbutton("Roll Dice", clicked=ui.returns("2"), xminimum=80, xpos=40, ypos=80)
        choice = ui.interact()
        
    if choice == "1":
        $ move += 1
        jump start
    elif choice == "2":
        #$ move += 1
        call dice
        #call project
        call select
        $ board.normal()
        jump start

label dice:
    $ roll = renpy.random.randint(1, 6)
    "I rolled %(roll)s" 
    $ projection(board, person1.box, roll, person1.direction)
    return
    
label select:
    python:
        if box1.alert:
            ui.imagebutton(box1.imghover, box1.imghover, clicked=ui.returns(box1.returns), xpos=box1.xpos,ypos=box1.ypos)
        else:
            ui.imagebutton(box1.imgidle, box1.imgidle, clicked=None, xpos=box1.xpos,ypos=box1.ypos)
        
        if box2.alert:
            ui.imagebutton(box2.imghover, box2.imghover, clicked=ui.returns(box2.returns), xpos=box2.xpos,ypos=box2.ypos)
        else:
            ui.imagebutton(box2.imgidle, box2.imgidle, clicked=None, xpos=box2.xpos,ypos=box2.ypos)
            
        if box3.alert:
            ui.imagebutton(box3.imghover, box3.imghover, clicked=ui.returns(box3.returns), xpos=box3.xpos,ypos=box3.ypos)
        else:
            ui.imagebutton(box3.imgidle, box3.imgidle, clicked=None, xpos=box3.xpos,ypos=box3.ypos)
            
        if box4.alert:
            ui.imagebutton(box4.imghover, box4.imghover, clicked=ui.returns(box4.returns), xpos=box4.xpos,ypos=box4.ypos)
        else:
            ui.imagebutton(box4.imgidle, box4.imgidle, clicked=None, xpos=box4.xpos,ypos=box4.ypos)   
            
        if box5.alert:
            ui.imagebutton(box5.imghover, box5.imghover, clicked=ui.returns(box5.returns), xpos=box5.xpos,ypos=box5.ypos)
        else:
            ui.imagebutton(box5.imgidle, box5.imgidle, clicked=None, xpos=box5.xpos,ypos=box5.ypos)    
       
        if box6.alert:
            ui.imagebutton(box6.imghover, box6.imghover, clicked=ui.returns(box6.returns), xpos=box6.xpos,ypos=box6.ypos)
        else:
            ui.imagebutton(box6.imgidle, box6.imgidle, clicked=None, xpos=box6.xpos,ypos=box6.ypos)
        
        if box7.alert:
            ui.imagebutton(box7.imghover, box7.imghover, clicked=ui.returns(box7.returns), xpos=box7.xpos,ypos=box7.ypos)
        else:
            ui.imagebutton(box7.imgidle, box7.imgidle, clicked=None, xpos=box7.xpos,ypos=box7.ypos)    
            
        if box8.alert:
            ui.imagebutton(box8.imghover, box8.imghover, clicked=ui.returns(box8.returns), xpos=box8.xpos,ypos=box8.ypos)
        else:
            ui.imagebutton(box8.imgidle, box8.imgidle, clicked=None, xpos=box8.xpos,ypos=box8.ypos)    
            
        if box9.alert:
            ui.imagebutton(box9.imghover, box9.imghover, clicked=ui.returns(box9.returns), xpos=box9.xpos,ypos=box9.ypos)
        else:
            ui.imagebutton(box9.imgidle, box9.imgidle, clicked=None, xpos=box9.xpos,ypos=box9.ypos)  
            
        if box10.alert:
            ui.imagebutton(box10.imghover, box10.imghover, clicked=ui.returns(box10.returns), xpos=box10.xpos,ypos=box10.ypos)
        else:
            ui.imagebutton(box10.imgidle, box10.imgidle, clicked=None, xpos=box10.xpos,ypos=box10.ypos)    
          
        if box11.alert:
            ui.imagebutton(box11.imghover, box11.imghover, clicked=ui.returns(box11.returns), xpos=box11.xpos,ypos=box11.ypos)
        else:
            ui.imagebutton(box11.imgidle, box11.imgidle, clicked=None, xpos=box11.xpos,ypos=box11.ypos)        
            
        if box12.alert:
            ui.imagebutton(box12.imghover, box12.imghover, clicked=ui.returns(box12.returns), xpos=box12.xpos,ypos=box12.ypos)
        else:
            ui.imagebutton(box12.imgidle, box12.imgidle, clicked=None, xpos=box12.xpos,ypos=box12.ypos)   
            
        if box13.alert:
            ui.imagebutton(box13.imghover, box13.imghover, clicked=ui.returns(box13.returns), xpos=box13.xpos,ypos=box13.ypos)
        else:
            ui.imagebutton(box13.imgidle, box13.imgidle, clicked=None, xpos=box13.xpos,ypos=box13.ypos)  
            
        if box14.alert:
            ui.imagebutton(box14.imghover, box14.imghover, clicked=ui.returns(box14.returns), xpos=box14.xpos,ypos=box14.ypos)
        else:
            ui.imagebutton(box14.imgidle, box14.imgidle, clicked=None, xpos=box14.xpos,ypos=box14.ypos)      
            
        if box15.alert:
            ui.imagebutton(box15.imghover, box15.imghover, clicked=ui.returns(box15.returns), xpos=box15.xpos,ypos=box15.ypos)
        else:
            ui.imagebutton(box15.imgidle, box15.imgidle, clicked=None, xpos=box15.xpos,ypos=box15.ypos)  
            
        if box16.alert:
            ui.imagebutton(box16.imghover, box16.imghover, clicked=ui.returns(box16.returns), xpos=box16.xpos,ypos=box16.ypos)
        else:
            ui.imagebutton(box16.imgidle, box16.imgidle, clicked=None, xpos=box16.xpos,ypos=box16.ypos)    
            
        if box17.alert:
            ui.imagebutton(box17.imghover, box17.imghover, clicked=ui.returns(box17.returns), xpos=box17.xpos,ypos=box17.ypos)
        else:
            ui.imagebutton(box17.imgidle, box17.imgidle, clicked=None, xpos=box17.xpos,ypos=box17.ypos)        
            
        if box18.alert:
            ui.imagebutton(box18.imghover, box18.imghover, clicked=ui.returns(box18.returns), xpos=box18.xpos,ypos=box18.ypos)
        else:
            ui.imagebutton(box18.imgidle, box18.imgidle, clicked=None, xpos=box18.xpos,ypos=box18.ypos) 
            
        if box19.alert:
            ui.imagebutton(box19.imghover, box19.imghover, clicked=ui.returns(box19.returns), xpos=box19.xpos,ypos=box19.ypos)
        else:
            ui.imagebutton(box19.imgidle, box19.imgidle, clicked=None, xpos=box19.xpos,ypos=box19.ypos)       
            
        if box20.alert:
            ui.imagebutton(box20.imghover, box20.imghover, clicked=ui.returns(box20.returns), xpos=box20.xpos,ypos=box20.ypos)
        else:
            ui.imagebutton(box20.imgidle, box20.imgidle, clicked=None, xpos=box20.xpos,ypos=box20.ypos)   
            
        if box21.alert:
            ui.imagebutton(box21.imghover, box21.imghover, clicked=ui.returns(box21.returns), xpos=box21.xpos,ypos=box21.ypos)
        else:
            ui.imagebutton(box21.imgidle, box21.imgidle, clicked=None, xpos=box21.xpos,ypos=box21.ypos)  
            
        if box22.alert:
            ui.imagebutton(box22.imghover, box22.imghover, clicked=ui.returns(box22.returns), xpos=box22.xpos,ypos=box22.ypos)
        else:
            ui.imagebutton(box22.imgidle, box22.imgidle, clicked=None, xpos=box22.xpos,ypos=box22.ypos)   
            
        if box23.alert:
            ui.imagebutton(box23.imghover, box23.imghover, clicked=ui.returns(box23.returns), xpos=box23.xpos,ypos=box23.ypos)
        else:
            ui.imagebutton(box23.imgidle, box23.imgidle, clicked=None, xpos=box23.xpos,ypos=box23.ypos)   
            
        if box24.alert:
            ui.imagebutton(box24.imghover, box24.imghover, clicked=ui.returns(box24.returns), xpos=box24.xpos,ypos=box24.ypos)
        else:
            ui.imagebutton(box24.imgidle, box24.imgidle, clicked=None, xpos=box24.xpos,ypos=box24.ypos)   
            
        if box25.alert:
            ui.imagebutton(box25.imghover, box25.imghover, clicked=ui.returns(box25.returns), xpos=box25.xpos,ypos=box25.ypos)
        else:
            ui.imagebutton(box25.imgidle, box25.imgidle, clicked=None, xpos=box25.xpos,ypos=box25.ypos)   
            
        if box26.alert:
            ui.imagebutton(box26.imghover, box26.imghover, clicked=ui.returns(box26.returns), xpos=box26.xpos,ypos=box26.ypos)
        else:
            ui.imagebutton(box26.imgidle, box26.imgidle, clicked=None, xpos=box26.xpos,ypos=box26.ypos)    
            
        if box27.alert:
            ui.imagebutton(box27.imghover, box27.imghover, clicked=ui.returns(box27.returns), xpos=box27.xpos,ypos=box27.ypos)
        else:
            ui.imagebutton(box27.imgidle, box27.imgidle, clicked=None, xpos=box27.xpos,ypos=box27.ypos)       
        
        ui.imagebutton(person1.icon, person1.icon, clicked=None, xpos=person1.box.pxpos, ypos=person1.box.pypos)    
        
        choice = ui.interact()    
    if choice:
        $ move = choice
        $ board.move(1, choice)
        call map
        
        return

    
    
    
label project:
    if box1.x == 0 and box1.y == 4:
        if roll == 1:
            if direction == 270:
                show tiler2 at a002
            elif direction == 360:    
                show tiler1 at a020
        elif roll == 2:
            if direction == 270:
                show tiler1 at a003
            elif direction == 360:    
                show tiler2 at a019
        elif roll == 3:
            if direction == 270:
                show tiler1 at a004
                show tiler3 at a021
            elif direction == 360:   
                show tiler2 at a018
        elif roll == 4:
            if direction == 270:
                show tiler1 at a005
                show tiler3 at a022
            elif direction == 360:    
                show tiler2 at a017
                show tiler4 at a026
        elif roll == 5:
            if direction == 270:
                show tiler1 at a006
            elif direction == 360:    
                show tiler2 at a016
            show tiler3 at a023
        elif roll == 6:
            if direction == 270:
                show tiler1 at a007
                show tiler5 at a024
                show tiler3 at a026
            elif direction == 360:    
                show tiler2 at a015
            show tiler4 at a027
    elif self.x == 0 and self.y == 3:
        if roll == 1:
            if direction == 180:
                show tiler2 at a003
            elif direction == 360:    
                show tiler1 at a001
        elif roll == 2:
            if direction == 180:
                show tiler1 at a021
                show tiler2 at a004
            elif direction == 360:    
                show tiler3 at a020
        elif roll == 3: ######### to do ##########
            if direction == 270:
                show tiler1 at a004
                show tiler3 at a021
            elif direction == 360:   
                show tiler2 at a018
        elif roll == 4:
            if direction == 270:
                show tiler1 at a005
                show tiler3 at a022
            elif direction == 360:    
                show tiler2 at a017
                show tiler4 at a026
        elif roll == 5:
            if direction == 270:
                show tiler1 at a006
            elif direction == 360:    
                show tiler2 at a016
            show tiler3 at a023
        elif roll == 6:
            if direction == 270:
                show tiler1 at a007
                show tiler5 at a024
                show tiler3 at a026
            elif direction == 360:    
                show tiler2 at a015
            show tiler4 at a027
    return
