import numpy as np
import os
import keyboard

###Parameters of game table
height, width=20, 10


#####################################################            
#####################################################            
#####################################################            
####Define classes

#Define class of screen to show the game
class Screen:
    blocks=[]
    #init method to define an empty wall
    def __init__(self):
        self.blocks=np.zeros((height,width), dtype=int)
        #To crete an matrix for background empty with shape (height, width)
    
    ##getters
    def get_blocks(self):
        return(self.blocks)
        
    #Plot the wall
    ##We have to improve the form to show the screen
    def plotBackground(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Bienvenido al Tetris")
        print("\n")
#         print(background)
        # for row in self.blocks:
        #     print("".join(map(str, row)))
        for row in self.blocks:
            print(' '.join(map(lambda cell: str(cell) if cell != 1 else '■', row)))

    #Change the screen plot
    def newBackground(self, Wall, Figure):
        screenshot=Wall.get_blocks().copy()
        coordinates_blocks=Figure.get_blocks()
        coordinates_blocks=tuple(map(tuple, coordinates_blocks))
        ##Painted blocks
        for pixel in coordinates_blocks:
            # print(pixel)
            screenshot[pixel]=1      
        self.blocks=screenshot

            
            
#####################################################            
#####################################################            
#####################################################            

class Wall():
    blocks=[]
    def __init__(self):
        self.blocks=np.zeros((height,width), dtype=int)

    ##getters
    def get_blocks(self):
        return(self.blocks)
#     pass

#####################################################            
#####################################################            
#####################################################            

class Movement:
    down=1
    right=2
    left=3
    rotate=4

class Piece:
    Figure=str
    position=[]
    shape=[]
    blocks=[]
    def __init__(self, shape):
        self.position=np.array([0,int(width/2)-1])
        self.shape=shape
        self.blocks=self.position+self.shape 

    ##getters
    def get_position(self):
        return(self.position)
    
    def get_blocks(self):
        return(self.blocks)
    
    ########################################
    ###To move piece
    def moveRight(self):
        self.position = self.position + np.array([0,1])
        self.blocks=self.position+self.shape

    def moveLeft(self):
        self.position = self.position + np.array([0,-1])
        self.blocks=self.position+self.shape

    def rotatePiece():
        pass

    def movePiece(self):
        event=keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == "d":
                self.moveRight()
            if event.name == "a":
                self.moveLeft()
    
        
#####################################################            
        
        
class Square(Piece):
    def __init__(self):
        """"Define the figure square, with the initial position and the shape
        for a square for each pixel for itself """
        shape=np.array([(0,0),(1,0),(0,1),(1,1)]) 
        super().__init__(shape)
        
class L_right(Piece):
    def __init__(self):
        shape=np.array([(1,0),(1,1),(1,2),(0,0)])        
        super().__init__(shape)

class L_left(Piece):
    def __init__(self):
        shape=np.array([(1,0),(1,1),(1,2),(0,2)])        
        super().__init__(shape)
        
class T_piece(Piece):
    def __init__(self):
        shape=np.array([(1,0),(1,1),(1,2),(0,1)])        
        super().__init__(shape)  

class I_piece(Piece):
    def __init__(self):
        shape=np.array([(0,0),(1,0),(2,0),(3,0)])        
        super().__init__(shape)    