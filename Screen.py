from Piece import Piece
from Wall import Wall
import numpy as np
import os

#Define class of screen to show the game
class Screen:
    blocks=[]
    #init method to define an empty wall
    def __init__(self, height, width):
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