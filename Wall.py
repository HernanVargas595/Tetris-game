from Piece import *
import numpy as np
import keyboard
import time
import threading

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

    def checkFillBlocks(self):
        wallCoordinates=self.get_blocks().tolist()
        wallCoordinates=coordinates(wallCoordinates)
        return wallCoordinates
    
    def pieceToWall(self, new_block):
        coordinatesBlock=new_block.get_blocks()
        coordinatesWall=self.checkFillBlocks()
        canMoveRight=True
        canMoveLeft=True
        canMoveDown=True
        for siteBlock in coordinatesBlock:
            for siteWall in coordinatesWall:
                if ((siteBlock[0]==siteWall[0])&(siteBlock[1]==siteWall[1]-1)):
                    canMoveRight=False
                if ((siteBlock[0]==siteWall[0])&(siteBlock[1]==siteWall[1]+1)):
                    canMoveLeft=False
                if ((siteBlock[0]<=siteWall[0]+1)&(siteBlock[1]==siteWall[1]))    :
                    canMoveDown=False
        return canMoveRight, canMoveLeft, canMoveDown


    def collidePiece(self, Piece):
        oldPositionBlocks=Piece.get_blocks().copy()
        # canMoveRight, canMoveLeft, canMoveDown=Piece.pieceLimits()
        canMoveRightScreen, canMoveLeftScreen, canMoveDownScreen=Piece.pieceLimits()
        canMoveRightWall, canMoveLeftWall, canMoveDownWall=self.pieceToWall(Piece)

        if ((canMoveDownScreen==False)|(canMoveDownWall==False)):
            # flag = event_obj.wait(0.5)
            # if flag:
            # print("Event was set to true() earlier, moving ahead with the thread") 
            event=keyboard.read_event()
            if event.name == "s":
                self.addPiecetoWall(oldPositionBlocks)
                return True  
      
        return False
    

    def movePiece(self, Piece):
        event=keyboard.read_event()
        canMoveRightScreen, canMoveLeftScreen, canMoveDownScreen=Piece.pieceLimits()
        canMoveRightWall, canMoveLeftWall, canMoveDownWall=self.pieceToWall(Piece)
        if event.event_type == keyboard.KEY_DOWN:
            if (canMoveRightScreen & canMoveRightWall):
                if event.name == "d":
                    Piece.moveRight()
            if (canMoveLeftScreen & canMoveLeftWall):
                if event.name == "a":
                    Piece.moveLeft()
            if (canMoveDownScreen & canMoveDownWall):
                if event.name == "s":
                    Piece.moveDown()
            if event.name == "space":
                # savePiece=Piece.copy()
                Piece.rotate_shape()
                outRight, outLeft, outUp =Piece.pieceOutScreen()
                while outRight:
                    piece.moveLeft()
                    outRight, outLeft, outUp =Piece.pieceOutScreen()
                while outLeft:
                    Piece.moveRight()
                    outRight, outLeft, outUp =Piece.pieceOutScreen()
                while outUp:
                    Piece.moveDown()
                    outRight, outLeft, outUp =Piece.pieceOutScreen()

    def checkFillRows(self):
        wallBlocks=self.get_blocks()#.copy()
        numberRows=len(wallBlocks)
        # print(len(wallBlocks))
        # lastRow=np.array([])
        for row in range(numberRows):
            blocksInRow=np.sum(wallBlocks[row])
            # print(blocksInRow)
            if blocksInRow==width:
                for rowToChange in range(row, numberRows-1):
                    wallBlocks[rowToChange]=wallBlocks[rowToChange+1]
                return 1
        return 0

