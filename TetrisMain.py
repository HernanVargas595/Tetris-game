# from TetrisClasses import *
from Piece import *
from Wall import Wall
from Screen import Screen

import random
import os
import time
import keyboard

height, width=20, 10

#Main function
def tetris():

    screen=Screen(height, width)
    # screen.plotBackground()
    
    wall=Wall(height, width)
    
    # new_piece=Square()  
    # new_piece=L_right()
    new_piece=randomPiece()
    # new_piece=T_piece()
    # new_piece=I_piece()
    
    screen.newBackground(wall, new_piece)
    screen.plotBackground()
    

    score=0

    while True:
        new_piece.movePiece()
        checkCollision=wall.collidePiece(new_piece)
        if checkCollision==True:
            new_piece=randomPiece()


        screen.newBackground(wall, new_piece)
        screen.plotBackground()
        print(f"Score: {score}")
        print(f"Piece can move to right: {new_piece.pieceLimits()[0]}")
        print(f"Piece can move to left: {new_piece.pieceLimits()[1]}")
        print(f"Piece can move to down: {new_piece.pieceLimits()[2]}")
        # print(new_piece.get_blocks())


        time.sleep(0.02)    


if __name__ == '__main__':
    try:
        tetris()
    except KeyboardInterrupt:
        print("¡Juego terminado!")

# tetris()