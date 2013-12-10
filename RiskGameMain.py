'''
@author: Kevin Cooper
@version: 0.0.2
@date: 01 Dec 13
@class: CS 359
'''

import CustomExceptionList as CEL
import RiskGUI
import RiskBoard
import pygame
import Player
import random
import Dice
if __name__ == '__main__':
    GameScreen = RiskGUI.RiskGUI()  
    board = RiskBoard.RiskBoard()  
    dice = Dice.Dice(6)
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
    
    #Setup for main game logic loop
    GameScreen.drawBoard(board)
    pygame.display.flip()  # update the screen
    source = None
    while True:
        GameScreen.clearScreen()
        GameScreen.drawBoard(board)
        # Ensure that the current player is capable of making a move
        count = 0
        while(board.hasValidMove(players[order]) != True):
            order = (order + 1) % (len(players))
            count = count + 1
            if(count == len(players)):
                exit(1) # None of the players has a valid move
        GameScreen.drawTurn(board, str(players[order]) + " turn!")     
                     
        event = GameScreen.getEvent(board)
        
        # print event
        if event[0] == "Exit":
            break
        if event[0] == "Region":
            print event
            if(event[1] == "Left"):
                if(event[2][1].getPlayer() == players[order]and source == None):
                    source = event[2][1]
                elif(event[2][1].validAttack(players[order]) and source != None):
                    GameScreen.battleSequence(source,event[2][1], dice)
                    source = None
                elif(event[2][1].validMove(players[order]) and source != None and source != event[2][1]):
                    GameScreen.moveSequence(source,event[2][1])
                    source = None
            else:
                source = None

    exit(0)
