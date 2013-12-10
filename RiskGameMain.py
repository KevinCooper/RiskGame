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
import Player
import random
if __name__ == '__main__':
    GameScreen = RiskGUI.RiskGUI()  
    board = RiskBoard.RiskBoard()  
        # Setup two players for testing
    players = []
    one = Player.Player((255, 0, 0), 10, "Player 1")
    two = Player.Player((0, 0, 255), 10, "Player 2")
    players.append(one)
    players.append(two)
    order = 0
    for region in board.getRegions():
        test = random.randint(1,2)
        if(test == 1):
            region[1].setPlayer(players[0])
        else:
            region[1].setPlayer(players[1])
        region[1].addUnits(2)
    #

    GameScreen.drawBoard(board)
    pygame.display.flip()  # update the screen
    

    
    
    while True:
        # Ensure that the current player is capable of making a move
        count = 0
        while(board.hasValidMove(players[order]) != True):
            order = (order + 1) % (len(players))
            count = count + 1
            if(count == len(players)):
                exit(1) # None of the players has a valid move
                          
        event = GameScreen.getEvent(board)
        
        print event
        if event == "Exit":
            break
        if event == "Region":
            print event
        
       
    
    
    
    
    
    
    
    exit(0)
