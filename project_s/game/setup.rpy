init python:
    class Board:
        def __init__(self, boxes=[], people=[]):
            self.boxes = boxes
            self.people = people
        def alert(self, ids=[]):
            for id in ids:
                for box in self.boxes:
                    if len(str(id)) == 1:
                        pk = 'a00' + str(id)
                    else:    
                        pk = 'a0' + str(id)
                    if box.id == pk:
                        box.alert = True
                        
        def normal(self):
            for box in self.boxes:
                box.alert = False
                
        def move(self, person_id, returns):
            for box in self.boxes:
                for person in self.people:
                    if person.id == person_id:
                        if box.returns == returns:
                            person.direction_change(box)
                            person.box = box
                            
    class Person:
        def __init__(self, id, icon):
            self.id = id
            self.icon = icon
            self.box = box1
            self.x = self.box.x
            self.y = self.box.y
            self.money = None
            self.direction = 360
        
        def direction_change(self, box):
            r_x = box.x - self.box.x
            r_y = box.y - self.box.y
            if self.direction == 90:
                if r_y > 0: 
                    if r_y == 2 and r_x <= 0:
                        self.direction = 270
                    elif r_y == 2 and r_x == 1:
                        self.direction = 270
                    elif r_y == 4 and r_x == 0:
                        self.direction = 270   
                    else:    
                        self.direction = 360
                elif r_y < 0:
                    if r_y == -2 and r_x <= 0:
                        self.direction = 270
                    elif r_y == -2 and r_x == 1:
                        self.direction = 270
                    elif r_y == 4 and r_x == 0:
                        self.direction = 270
                    else:    
                        self.direction = 180
            elif self.direction == 180:
                if r_x > 0:
                    if r_x == 3 and r_y <= 2:
                        self.direction = 360
                    elif r_x == 2 and r_y <= 2:
                        self.direction = 270
                    else:    
                        self.direction = 90
                elif r_x < 0:
                    if r_x == -3 and r_y <= 2:
                        self.direction = 360
                    elif r_x == -2 and r_y <= 2:
                        self.direction = 90
                    else:    
                        self.direction = 270
            elif self.direction == 270:
                if r_y > 0:
                    if r_y == 2 and r_x <= 0:
                        self.direction = 90
                    elif r_y == 2 and r_x == 1:
                        self.direction = 90
                    elif r_y == 4 and r_x == 0:
                        self.direction = 90
                    else:    
                        self.direction = 360
                elif r_y < 0:
                    if r_y == -2 and r_x <= 0:
                        self.direction = 90
                    elif r_y == -2 and r_x == 1:
                        self.direction = 90
                    elif r_y == 4 and r_x == 0:
                        self.direction = 90
                    else:    
                        self.direction = 180
            elif self.direction == 360:
                if r_x > 0:
                    if r_x == 3 and r_y == 2:
                        self.direction = 360
                    elif r_x == 3 and r_y == 0:
                        self.direction = 180
                    elif r_x == 2 and r_y == 2:
                        self.direction = 270
                    else:    
                        self.direction = 90
                elif r_x < 0:
                    if r_x == -3 and r_y == 2:
                        self.direction = 360
                    elif r_x == -3 and r_y == 0:
                        self.direction = 180
                    elif r_x == -2 and r_y == 2:
                        self.direction = 90
                    else:    
                        self.direction = 270
                    
                
    class Box:
        def __init__(self, id, x, y, data, xpos, ypos, pxpos, pypos, imgidle, imghover, imgalert, returns):
            self.id = id
            self.x = x
            self.y = y
            self.data = data
            self.xpos = xpos
            self.ypos = ypos
            self.pxpos = pxpos
            self.pypos = pypos
            self.imgidle = imgidle
            self.imghover = imghover
            self.imgalert = imgalert
            self.returns = returns
            self.alert = False
            
        #def project(self, roll, direction):  
                    
    def projection(board, box, roll, direction):
        for k, v in box.data.items():
            if k == direction:
                board.alert(v[roll])
            else:
                board.alert(v[roll])
                
                
                
        
    # a001
    data1 = {270: {1: [2], 2: [3], 3: [4, 21], 4: [5, 22], 5: [6, 23], 6: [7, 24, 27, 26]},
                  360: {1: [20], 2: [19], 3: [18], 4: [17, 26], 5: [16, 23], 6: [15, 22, 24, 27]}
                 }
    # a002
    data2 = {180: {1: [3], 2: [4, 21], 3: [5, 22], 4: [6, 23], 5: [7, 24, 26, 27], 6: [8, 25, 18, 8]},
                  360: {1: [1], 2: [20], 3: [19], 4: [18], 5: [17, 26], 6: [16, 23]}
                 }
    # a003
    data3 = {180: {1: [4, 21], 2: [5, 22], 3: [6, 23], 4: [7, 24, 26, 27], 5: [8, 25, 18], 6: [9, 13, 17]},
                  270: {1: [4, 2], 2: [5, 1], 3: [6, 20], 4: [7, 19], 5: [8, 18], 6: [9, 19, 26, 27]}, 
                  360: {1: [2, 21], 2: [1, 22], 3: [20, 23], 4: [19, 24, 26, 27], 5: [18, 25, 8], 6: [17, 26, 13]}
                 }
    # a004                 
    data4 = {180: {1: [5], 2: [6], 3: [7], 4: [8], 5: [9, 27], 6: [10, 23]},
                  360: {1: [3], 2: [2, 21], 3: [1, 22], 4: [20, 23], 5: [19, 24, 26, 25], 6: [18, 25, 8]}
                 }
    # a005
    data5 = {180: {1: [6], 2: [7], 3: [8], 4: [9, 27], 5: [10, 23], 6: [11, 22, 24, 26]},
                  270: {1: [4], 2: [3], 3: [2, 21], 4: [1, 22], 5: [20, 23], 6: [19, 24, 26, 27]}
                 }
    #a006
    data6 = {90: {1: [7], 2: [8], 3: [9, 27], 4: [10, 23], 5: [11, 22, 24, 26], 6: [12, 18, 25, 21]},
                  270: {1: [5], 2: [4], 3: [3], 4: [2, 21], 5: [1, 22], 6: [20, 23]}
                 }
    #a007             
    data7 = {90: {1: [8], 2: [9, 27], 3: [10, 23], 4: [11, 22, 24, 26], 5: [12, 21, 18, 25], 6: [13, 17, 3]},
                  270: {1: [6], 2: [5], 3: [4], 4: [3], 5: [2, 21], 6: [1, 22]} 
                 }
    #a008             
    data8 = {90: {1: [9, 27], 2: [10, 23], 3: [11, 22, 24, 26], 4: [12, 21, 18, 25], 5: [13, 17, 3], 6: [14, 16, 2, 20, 4, 12]},
                  270: {1: [7, 27], 2: [6, 23], 3: [5, 22, 24, 26], 4: [4, 18, 21, 25], 5: [3, 19, 17, 13], 6: [2, 21, 14, 12, 20, 16]}, 
                  360: {1: [7, 9], 2: [6, 10], 3: [5, 11], 4: [4, 12], 5: [3, 13], 6: [2, 21, 25, 14]}
                 }             
    #a009             
    data9 = {90: {1: [10], 2: [11], 3: [12], 4: [13], 5: [14, 25], 6: [15, 24]},
                  270: {1: [8], 2: [7, 27], 3: [6, 23], 4: [5, 22, 24, 26], 5: [4, 21, 18, 25], 6: [3, 13, 19, 17, 2, 4]}, 
                 }         
    #a010             
    data10 = {90: {1: [11], 2: [12], 3: [13], 4: [14, 25], 5: [15, 24], 6: [16, 23]},
                   270: {1: [9], 2: [8], 3: [7, 27], 4: [6, 23], 5: [5, 22, 24, 26], 6: [4, 21, 18, 25]}, 
                 }
    #a011             
    data11 = {90: {1: [12], 2: [13], 3: [14, 25], 4: [15, 24], 5: [16, 23], 6: [17, 22, 26, 27]},
                   180: {1: [10], 2: [9], 3: [8], 4: [7, 27], 5: [6, 23], 6: [5, 22, 24, 26]}, 
                 }             
    #a012             
    data12 = {180: {1: [11], 2: [10], 3: [9], 4: [8], 5: [7, 27], 6: [6, 23]},
                    360: {1: [13], 2: [14, 25], 3: [15, 23], 4: [16, 23], 5: [17, 22, 26, 27], 6: [8, 21, 18]}, 
                 }         
    #a013
    data13 = {90: {1: [12, 14], 2: [11, 15], 3: [10, 16], 4: [9, 17], 5: [8, 18], 6: [7, 19, 26, 27]},
                    180: {1: [12], 2: [11], 3: [10], 4: [9], 5: [8], 6: [7, 27]},
                    360: {1: [14, 25], 2: [15, 24], 3: [16, 23], 4: [17, 22, 26, 27], 5: [18, 21, 8], 6: [19, 17, 7, 9, 2, 4]}, 
                 }         
    #a014             
    data14 = {180: {1: [13], 2: [12, 25], 3: [11, 24], 4: [10, 23], 5: [9, 22, 26, 27], 6: [8, 21, 18]},
                    360: {1: [15], 2: [16], 3: [17], 4: [18], 5: [19, 26], 6: [20, 23]}, 
                 }                   
    #a015             
    data15 = {90: {1: [14], 2: [13], 3: [12, 25], 4: [11, 24], 5: [10, 23], 6: [9, 22, 26, 27]},
                    360: {1: [16], 2: [17], 3: [18], 4: [19, 26], 5: [20, 23], 6: [1, 22, 24, 27]}, 
                 } 
    #a016             
    data16 = {90: {1: [15], 2: [14], 3: [13], 4: [12, 25], 5: [11, 24], 6: [10, 23]},
                    270: {1: [17], 2: [18], 3: [19, 26], 4: [20, 23], 5: [1, 22, 24, 27], 6: [2, 8, 21, 25]}, 
                 }
    #a017             
    data17 = {90: {1: [16], 2: [15], 3: [14], 4: [13], 5: [12, 25], 6: [11, 24]},
                    270: {1: [18], 2: [19, 26], 3: [20, 23], 4: [1, 22, 24, 27], 5: [2, 8, 21, 25], 6: [3, 13, 7, 9]}, 
                 }             
    #a018            
    data18 = {90: {1: [17, 26], 2: [16, 23], 3: [15, 22, 24, 27], 4: [14, 21, 25, 18], 5: [13, 3, 7, 9], 6: [2, 4, 12, 14, 10, 16]},
                    270: {1: [19, 26], 2: [20, 23], 3: [1, 22, 24, 27], 4: [2, 8, 21, 25], 5: [3, 13, 7, 9], 6: [2, 4, 6, 10, 12, 14]},
                    360: {1: [17, 19], 2: [16, 20], 3: [15, 1], 4: [14, 2], 5: [13, 3], 6: [25, 12, 21, 4]}
                 }          
    #a019            
    data19 = {90: {1: [18], 2: [17, 26], 3: [16, 23], 4: [15, 22, 24, 27], 5: [14, 21, 8, 25], 6: [13, 3, 7, 9]},
                    270: {1: [20], 2: [1], 3: [2], 4: [3], 5: [4, 21], 6: [5, 22]}, 
                 }    
    #a020            
    data20 = {90: {1: [19], 2: [18], 3: [17, 26], 4: [16, 23], 5: [15, 22, 24, 27], 6: [14, 21, 8, 25]},
                    270: {1: [1], 2: [2], 3: [3], 4: [4, 21], 5: [5, 22], 6: [6, 23]}, 
                 }        
    #a021            
    data21 = {90: {1: [22], 2: [23], 3: [24, 26, 27], 4: [25, 18, 8], 5: [13, 7, 9, 19, 17], 6: [12, 14, 16, 20, 10, 6]},
                    270: {1: [3], 2: [2, 4], 3: [1, 5], 4: [20, 6], 5: [19, 7], 6: [18, 8]}, 
                 }            
    #a022            
    data22 = {90: {1: [23], 2: [24, 26, 27], 3: [25, 18, 8], 4: [13, 7, 9, 19, 17], 5: [12, 14, 16, 20, 10, 6], 6: [1, 15, 11, 5]},
                    270: {1: [21], 2: [3], 3: [2, 4], 4: [1, 5], 5: [20, 6], 6: [19, 7]}, 
                 }      
    #a023             
    data23 = {90: {1: [24, 26, 27], 2: [25, 18, 8], 3: [13, 19, 17, 7, 9], 4: [12, 14, 16, 20, 6, 10], 5: [11, 15, 5, 1], 6: [2, 14, 10, 4]},
                    180: {1: [22, 24, 27], 2: [21, 25, 8], 3: [3, 13, 7, 9], 4: [2, 4, 12, 14, 6, 10], 5: [11, 15, 5, 1], 6: [6, 20, 16, 10, 4, 12]},
                    270: {1: [22, 26, 27], 2: [21, 18, 8], 3: [19, 17, 3, 7, 9], 4: [20, 16, 2, 4, 6, 10], 5: [11, 15, 5, 1], 6: [2, 14, 6, 20, 4, 12]},
                    360: {1: [22, 24, 26], 2: [21, 18, 25], 3: [3, 17, 19, 13], 4: [2, 4, 16, 20, 12, 14], 5: [11, 15, 5, 1], 6: [16, 20, 2, 14, 10, 16]}
                 } 
    #a024
    data24 = {90: {1: [25], 2: [13], 3: [14, 12], 4: [15, 11], 5: [16, 10], 6: [17, 9]},
                    270: {1: [23], 2: [22, 26, 27], 3: [21, 18, 8], 4: [3, 19, 17, 7, 9], 5: [2, 4, 16, 20, 6, 10], 6: [11, 15, 5, 1]}, 
                 }    
    #a025
    data25 = {90: {1: [13], 2: [14, 12], 3: [15, 11], 4: [16, 10], 5: [17, 9], 6: [18, 8]},
                    270: {1: [24], 2: [23], 3: [22, 26, 27], 4: [21, 18, 8], 5: [3, 19, 17, 7, 9], 6: [2, 4, 16, 20, 6, 10]}, 
                 }     
    #a026
    data26 = {180: {1: [23], 2: [22, 24, 27], 3: [21, 25, 8], 4: [3, 13, 7, 9], 5: [2, 4, 6, 10, 12, 14], 6: [11, 15, 5, 1]},
                    360: {1: [18], 2: [17, 19], 3: [16, 20], 4: [1, 15], 5: [2, 14], 6: [3, 13]}, 
                 }               
    #a027
    data27 = {180: {1: [8], 2: [7, 9], 3: [6, 10], 4: [5, 11], 5: [4, 12], 6: [3, 13]},
                    360: {1: [23], 2: [22, 26, 27], 3: [21, 18, 24], 4: [3, 17, 19, 13], 5: [2, 4, 16, 20, 12, 14], 6: [11, 15, 5, 1]}, 
                 }         
                 
    box1 = Box("a001", 0,4, data1, 85, 140, 105, 150, "tile4.png", "tile4r.png", "tile4r.png", 1)
    box2 = Box("a002", 0,3, data2, 85, 230, 105, 240, "tile4.png", "tile4r.png", "tile4r.png", 2)
    box3 = Box("a003", 0,2, data3, 85, 320, 105, 330, "tile4.png", "tile4r.png", "tile4r.png", 3)
    box4 = Box("a004", 0,1, data4, 85, 410, 105, 420, "tile4.png", "tile4r.png", "tile4r.png", 4)
    box5 = Box("a005", 0,0, data5, 85, 500, 105, 510, "tile4.png", "tile4r.png", "tile4r.png", 5)
    
    box6 = Box("a006", 1,0, data6, 175, 500, 195, 510, "tile4.png", "tile4r.png", "tile4r.png", 6)
    box7 = Box("a007", 2,0, data7, 265, 500, 285, 510, "tile4.png", "tile4r.png", "tile4r.png", 7)
    box8 = Box("a008", 3,0, data8, 355, 500, 375, 510, "tile4.png", "tile4r.png", "tile4r.png", 8)
    box9 = Box("a009", 4,0, data9, 445, 500, 465, 510, "tile4.png", "tile4r.png", "tile4r.png", 9)
    box10 = Box("a010", 5,0, data10, 535, 500, 555, 510, "tile4.png", "tile4r.png", "tile4r.png", 10)
    
    box11 = Box("a011", 6,0, data11, 625, 500, 645, 510, "tile4.png", "tile4r.png", "tile4r.png", 11)
    box12 = Box("a012", 6,1, data12, 625, 410, 645, 420, "tile4.png", "tile4r.png", "tile4r.png", 12)
    box13 = Box("a013", 6,2, data13, 625, 320, 645, 330, "tile4.png", "tile4r.png", "tile4r.png", 13)
    box14 = Box("a014", 6,3, data14, 625, 230, 645, 240, "tile4.png", "tile4r.png", "tile4r.png", 14)
    box15 = Box("a015", 6,4, data15, 625, 140, 645, 150, "tile4.png", "tile4r.png", "tile4r.png", 15)
    
    box16 = Box("a016", 5,4, data16, 535, 140, 555, 150, "tile4.png", "tile4r.png", "tile4r.png", 16)
    box17 = Box("a017", 4,4, data17, 445, 140, 465, 150, "tile4.png", "tile4r.png", "tile4r.png", 17)
    box18 = Box("a018", 3,4, data18, 355, 140, 375, 150, "tile4.png", "tile4r.png", "tile4r.png", 18)
    box19 = Box("a019", 2,4, data19, 265, 140, 285, 150, "tile4.png", "tile4r.png", "tile4r.png", 19)
    box20 = Box("a020", 1,4, data20, 175, 140, 195, 150, "tile4.png", "tile4r.png", "tile4r.png", 20)
    
    box21 = Box("a021", 1,2, data21, 175, 320, 195, 330, "tile4.png", "tile4r.png", "tile4r.png", 21)
    box22 = Box("a022", 2,2, data22, 265, 320, 285, 330, "tile4.png", "tile4r.png", "tile4r.png", 22)
    box23 = Box("a023", 3,2, data23, 355, 320, 375, 330, "tile4.png", "tile4r.png", "tile4r.png", 23)
    box24 = Box("a024", 4,2, data24, 445, 320, 465, 330, "tile4.png", "tile4r.png", "tile4r.png", 24)
    box25 = Box("a025", 5,2, data25, 535, 320, 555, 330, "tile4.png", "tile4r.png", "tile4r.png", 25)
    
    box26 = Box("a026", 3,3, data26, 355, 230, 375, 240, "tile4.png", "tile4r.png", "tile4r.png", 26)
    box27 = Box("a027", 3,1, data27, 355, 410, 375, 420, "tile4.png", "tile4r.png", "tile4r.png", 27)
    
    person1 = Person(1, "dot.png")
    
    board =  Board(
                            [box1, box2, box3, box4, box5, box6, box7, box8, box9, box10, 
                            box11, box12, box13, box14, box15, box16, box17, box18, box19, box20, 
                            box21, box22, box23, box24, box25, box26, box27],
                            [person1,]
                   )                      
                     
