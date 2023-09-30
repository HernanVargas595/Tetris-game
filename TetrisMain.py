from TetrisClasses import *
import random
import os
import time
import keyboard

#Main function
def tetris():

    screen=Screen()
    screen.plotBackground()
    
    wall=Wall()
    
    new_piece=Square()
#     new_piece=L_right()
#     new_piece=L_left()
    # new_piece=T_piece()
#     new_piece=I_piece()
    
    screen.newBackground(wall, new_piece)
    screen.plotBackground()
    
#     new_piece=rotate_shape(new_piece)

#     screen.newBackground(wall, new_piece)
#     screen.plotBackground()

    score=0

    while True:
        new_piece.movePiece()

        screen.newBackground(wall, new_piece)
        screen.plotBackground()
        print(f"Score: {score}")
        time.sleep(0.05)    


if __name__ == '__main__':
    try:
        tetris()
    except KeyboardInterrupt:
        print("¡Juego terminado!")

# tetris()