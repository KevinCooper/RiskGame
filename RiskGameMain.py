'''
@author: Kevin Cooper
@version: 0.0.1
@date: 01 Dec 13
@class: CS 359
'''

import CustomExceptionList as CEL
import RiskGUI
import RiskBoard

if __name__ == '__main__':
    try:
        GameScreen = RiskGUI.RiskGUI()
    except CEL.DetailedException as EO:
        EO.handleItself()
    board = RiskBoard.RiskBoard()
    while True:
        event = GameScreen.getEvent()
        if event == "Exit":
            break
        print event
        
       
    
    
    
    
    
    
    
    exit(0)