'''
@author: Kevin Cooper
@version: 0.0.1
@date: 01 Dec 13
@class: CS 359
'''

import CustomExceptionList as CEL
import RiskGUI
import RiskBoard
import pygame
if __name__ == '__main__':
    try:
        GameScreen = RiskGUI.RiskGUI()
    except CEL.DetailedException as EO:
        EO.handleItself()
    board = RiskBoard.RiskBoard()
    GameScreen.drawBoard(board)
    pygame.display.flip()
    while True:
        event = GameScreen.getEvent(board)
        print event
        if event == "Exit":
            break
        if event == "Region":
            print event
        
       
    
    
    
    
    
    
    
    exit(0)