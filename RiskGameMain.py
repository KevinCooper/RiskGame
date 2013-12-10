'''
@author: Kevin Cooper
@version: 0.0.2
@date: 01 Dec 13
@class: CS 359
'''

import RiskGUI
import RiskBoard
import pygame
import Player
import random
import Dice
import MenuStuff

def menu(screen):
    myMenu = MenuStuff.Menu(("Start Game", "Quit"))
    myMenu.drawMenu()
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    while 1:
        clock.tick(60)

    # Handle Input Events
        for event in pygame.event.get():
            myMenu.handleEvent(event)
            # quit the game if escape is pressed
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                myMenu.activate()
            elif event.type == myMenu.MENUCLICKEDEVENT:
                if event.text == "Quit":
                    exit(0)
                elif event.item == 0:
                    return
        screen.blit(background, (0, 0))    
        if myMenu.isActive():
            myMenu.drawMenu()
        else:
            background.fill((0, 0, 0))
               
        
        pygame.display.flip()


if __name__ == '__main__':
    GameScreen = RiskGUI.RiskGUI()
    clock = pygame.time.Clock()
    menu(GameScreen.screen)
    board = RiskBoard.RiskBoard(GameScreen.size)  
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
        #All manual events here
        GameScreen.clearScreen()
        for event in pygame.event.get():
            # Ensure that the current player is capable of making a move
            count = 0
            while(board.hasValidMove(players[order]) != True):
                order = (order + 1) % (len(players))
                count = count + 1
                if(count == len(players)):
                    print("There are no possible moves left!")
                    exit(1) # None of the players has a valid move
            gotEvent = GameScreen.resolveEvent(board, event)
            # print event
            if (gotEvent == None):
                pass
            elif (gotEvent[0] == "Exit"):
                exit(0)
            elif (gotEvent[0] == "SpaceBar"):
                order = (order + 1) % (len(players))
                players[order].addPieces(5) #Change this to be dynamic later!!!!!
            elif (gotEvent[0] == "Region"):
                #print gotEvent
                if(gotEvent[1] == "Left"):
                    if(gotEvent[2][1].getPlayer() == players[order]and source == None):
                        source = gotEvent[2][1]
                    elif(gotEvent[2][1].validAttack(players[order]) and source != None):
                        GameScreen.battleSequence(source,gotEvent[2][1], dice)
                        source = None
                    elif(gotEvent[2][1].validMove(players[order]) and source != None and source != gotEvent[2][1]):
                        GameScreen.moveSequence(source,gotEvent[2][1])
                        source = None
                    else:
                        source = None
                elif(gotEvent[1] == "Right"):
                    if(gotEvent[2][1].getPlayer() == players[order]):
                        if(players[order].removePieces(1)):
                            gotEvent[2][1].addUnits(1)
        #All clock based events move down here         
        GameScreen.drawBoard(board)
        GameScreen.drawTurn(board, str(players[order]) + " turn!", players[order].getPieces())  
        time = clock.tick(1000) #Slow down the clock 1000/100 = 10 FPS
        for region in board.getRegions():
            region[1].update(time, GameScreen.screen)        
        pygame.display.flip()

    exit(0)
