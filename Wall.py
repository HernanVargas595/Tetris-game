from Piece import *
import numpy as np
import keyboard

class Wall():
    blocks=[]
    def __init__(self, height, width):
        self.blocks=np.zeros((height,width), dtype=int)

    ##getters and setters
    def get_blocks(self):
        return(self.blocks)
    
    def set_blocks(self, value):
        self.blocks=value
    

    def addPiecetoWall(self, new_blocks):
        new_blocks=tuple(map(tuple, new_blocks))
        for block in new_blocks:
            self.blocks[block]=1
        # wallBlocks=self.blocks
        # for wallBlocks in rows:
        #     for column in row:
        #         if wallBlocks[row, column]=
        
        #  self.set_blocks(self.blocks+new_blocks)
        

    def collidePiece(self, Piece):
        oldPositionBlocks=Piece.get_blocks().copy()
        canMoveRight, canMoveLeft, canMoveDown=Piece.pieceLimits()

        if canMoveDown==False:
            event=keyboard.read_event()
            if event.name == "s":
                self.addPiecetoWall(oldPositionBlocks)
                return True  
            
        return False
                
        # for site in oldPositionBlocks:
        # pass
