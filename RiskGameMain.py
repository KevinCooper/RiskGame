'''
@author: Kevin Cooper
@version: 0.0.0
@date: 01 Dec 13
@class: CS 359
'''

import CustomExceptionList as CEL
import RiskGUI

if __name__ == '__main__':
    try:
        GameScreen = RiskGUI.RiskGUI()
    except CEL.DetailedException as EO:
        EO.handleItself()
    
    
    while True:
        event = GameScreen.getEvent()[0]
        if event == "Exit":
            break
        
       
    
    
    
    
    
    
    
    exit(0)