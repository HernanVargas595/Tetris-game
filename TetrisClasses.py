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
        print("Welcome to game")
        print("\n")
#         print(background)
        # for row in self.blocks:
        #     print("".join(map(str, row)))
        height=len(self.blocks)
        # print(self.blocks[0])
        # for row in self.blocks:
        #     print(' '.join(map(lambda cell: str(cell) if cell != 1 else '■', row)))
        for height_row in range(height):
            row=self.blocks[height-1-height_row]
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

###########To get coordenates for any shape
def coordinates(shape):
    i, j=0, 0
    shape=np.array(shape)
    coordinates=np.empty([0, 2], dtype=int)
    for row in range(shape.shape[0]):
        for element in range(shape.shape[1]):
            if shape[row, element]==1:
                temp=np.array([(row, element)])
                coordinates=np.concatenate((coordinates,temp), axis=0)
    return coordinates

class Piece:
    Figure=str
    position=[]
    shape=[]
    blocks=[]
    coordinates=[]
    
    def __init__(self, shape, large):
        self.position=np.array([height-large,int(width/2)-1])
        self.shape=shape
        self.coordinates=coordinates(self.shape)
        self.blocks=self.position+self.coordinates

    ##getters
    def get_position(self):
        return(self.position)
    
    def get_blocks(self):
        return(self.blocks)
    
    
    ########################################
    ###To move piece

    ######To have information on piece limits for the movement of the piece
    def pieceLimits(self):
        coordinates=self.get_blocks()
        canMoveRight=True
        canMoveLeft=True
        canMoveDown=True
        for site in coordinates:
            if site[1]>=width-1:
                canMoveRight=False
            if site[1]<=0:
                canMoveLeft=False
            if site[0]<=0    :
                canMoveDown=False
        return canMoveRight, canMoveLeft, canMoveDown

    def moveRight(self):
        self.position = self.position + np.array([0,1])
        self.blocks=self.position+self.coordinates

    def moveLeft(self):
        self.position = self.position + np.array([0,-1])
        self.blocks=self.position+self.coordinates

    def moveDown(self):
        self.position = self.position + np.array([-1,0])
        self.blocks=self.position+self.coordinates

    def rotate_shape(self):
        # self.shape=[list(row) for row in zip(*self.shape[::-1])]
        self.shape=[list(row) for row in zip(*self.shape[::-1])]
        self.coordinates=coordinates(self.shape)
        self.blocks=self.position+self.coordinates

    def pieceOutScreen(self):
        coordinates=self.get_blocks()
        outRight=False
        outLeft=False
        outUp=False
        for site in coordinates:
            if site[1]>=width:
                outRight=True
            if site[1]<0:
                outLeft=True
            if site[0]>=height    :
                outUp=True
        return outRight, outLeft, outUp


    def movePiece(self):
        event=keyboard.read_event()
        canMoveRight, canMoveLeft, canMoveDown=self.pieceLimits()
        if event.event_type == keyboard.KEY_DOWN:
            if canMoveRight:
                if event.name == "d":
                    self.moveRight()
            if canMoveLeft:
                if event.name == "a":
                    self.moveLeft()
            if canMoveDown:
                if event.name == "s":
                    self.moveDown()
            if event.name == "space":
                self.rotate_shape()
                outRight, outLeft, outUp =self.pieceOutScreen()
                while outRight:
                    self.moveLeft()
                    outRight, outLeft, outUp =self.pieceOutScreen()
                while outLeft:
                    self.moveRight()
                    outRight, outLeft, outUp =self.pieceOutScreen()
                while outUp:
                    self.moveDown()
                    outRight, outLeft, outUp =self.pieceOutScreen()
                #     pass


    
        
#####################################################            
        
        
class Square(Piece):
    def __init__(self):
        """"Define the figure square, with the initial position and the shape
        for a square for each pixel for itself """
        shape=[[1, 1], [1, 1]]
        super().__init__(shape, 2)
        
class L_right(Piece):
    def __init__(self):
        shape=[[1, 1, 1], [0, 0, 1]]        
        super().__init__(shape, 2)

class L_left(Piece):
    def __init__(self):
        shape=[[1, 1, 1], [1, 0, 0]]      
        super().__init__(shape, 2)
        
class T_piece(Piece):
    def __init__(self):     
        shape=[[1, 1, 1], [0, 1, 0]]                
        super().__init__(shape, 2)  

class I_piece(Piece):
    def __init__(self):
        shape=[[1, 1, 1, 1]]        
        super().__init__(shape, 1)    