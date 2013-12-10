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
    
    #Setup for main game logic loop
    GameScreen.drawBoard(board)
    pygame.display.flip()  # update the screen
    sourceAttack = None
    sourceMove = None
    while True:
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
                if(event[2][1].getPlayer() == players[order]and sourceAttack==None):
                    sourceAttack = event[2][1]
                    print "Got attack source"
                elif(event[2][1].validAttack(players[order]) and sourceAttack != None):
                    print "Got attack target"
            elif(event[1] == "Right"):
                if(event[2][1].getPlayer() == players[order]and sourceMove == None):
                    sourceMove = event[2][1]
                    print "Got move source"
                elif(event[2][1].validMove(players[order]) and sourceMove != None):
                    print "Got move target"
            else:
                sourceAttack = None
                sourceMove = None

    exit(0)
