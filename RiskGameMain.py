'''
@author: Kevin Cooper
@version: 0.0.3
@date: 01 Dec 13
@class: CS 359
'''

import RiskGUI
import RiskBoard
import pygame
import Player
import Dice
import MenuStuff
import os


def menu(screen, options):
    myMenu = MenuStuff.Menu(options)
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
                elif event.text == "Start Game":
                    return
                elif event.text == "Toggle Music":
                    setupGameMusic()
                    return
                elif event.text == "Toggle Fullscreen":
                    pass
                elif event.text == "Back":
                    return
        pygame.display.flip()


def setupGameMusic():
    try:
        if(not pygame.mixer.music.get_busy()):
            pygame.mixer.music.load(os.path.join('resources', \
                "Dexter_Britain_-_01_-_Shooting_Star.mp3"))
            pygame.mixer.music.play()
            pygame.mixer.music.queue(os.path.join('resources', \
                "Rolemusic_-_04_-_The_Pirate_And_The_Dancer.mp3"))
            pygame.mixer.music.queue(os.path.join('resources', \
                "Lomz__Lezet_-_08_-_Cod.mp3"))
            pygame.mixer.music.queue(os.path.join('resources', \
                "Koona_-_02_-_Starkey.mp3"))
        else:
            pygame.mixer.music.stop()
    except:
        pass


if __name__ == '__main__':
    play = True
    fullscreen = True
    pygame.init()
    GameScreen = RiskGUI.RiskGUI()
    clock = pygame.time.Clock()
    menu(GameScreen.screen, ("Start Game", "Quit"))
    board = RiskBoard.RiskBoard(GameScreen.size)
    dice = Dice.Dice(6)
    setupGameMusic()
    # Setup two players for testing
    players = []
    one = Player.Player((255, 0, 0), 4, "Player 1")
    two = Player.Player((0, 0, 255), 0, "Player 2")
    players.append(one)
    players.append(two)
    order = 0
    playerPicker = 0
    for region in board:
        playerPicker = (playerPicker + 1) % len(players)
        if(playerPicker == 1):
            region.setPlayer(players[0])
        else:
            region.setPlayer(players[1])
        region.addUnits(3)

    # Setup for main game logic loop
    GameScreen.drawBoard(board)
    pygame.display.flip()  # update the screen
    source = None
    while True:
        # All manual events here
        GameScreen.clearScreen()
        for event in pygame.event.get():
            # Ensure that the current player is capable of making a move
            count = 0
            while(board.hasValidMove(players[order]) != True):
                order = (order + 1) % (len(players))
                count = count + 1
                if(count == len(players)):
                    print("There are no possible moves left!")
                    exit(1)  # None of the players has a valid move
            if(board.getCountRegions(players[order]) \
                    == len(board)):
                menu(GameScreen.screen, (str(players[order]) +\
                     " Won!", "Quit"))
            gotEvent = GameScreen.resolveEvent(board, event)
            # print event
            if (gotEvent == None):
                pass
            elif (gotEvent[0] == "Help"):
                menu(GameScreen.screen, ("Back", "Toggle Music", "Quit"))
            elif (gotEvent[0] == "Exit"):
                exit(0)
            elif (gotEvent[0] == "SpaceBar"):
                order = (order + 1) % (len(players))
                players[order].addPieces(board.getCountRegions(players[order]))
            elif (gotEvent[0] == "Region"):
                # print gotEvent
                if(gotEvent[1] == "Left"):
                    if(gotEvent[2][1].getPlayer() == players[order]and \
                            source == None):
                        source = gotEvent[2][1]
                    elif(gotEvent[2][1].validAttack(players[order]) and \
                            source != None and source != gotEvent[2][1] and \
                            board.areNeighbors(source, gotEvent[2][1])):
                        GameScreen.battleSequence(source, gotEvent[2][1], dice)
                        source = None
                    elif(gotEvent[2][1].validMove(players[order]) and \
                            source != None and source != gotEvent[2][1] and \
                            board.areNeighbors(source, gotEvent[2][1])):
                        GameScreen.moveSequence(source, gotEvent[2][1])
                        source = None
                    else:
                        source = None
                elif(gotEvent[1] == "Right"):
                    if(gotEvent[2][1].getPlayer() == players[order]):
                        if(players[order].removePieces(1)):
                            gotEvent[2][1].addUnits(1)
        # All clock based events move down here
        GameScreen.drawBoard(board)
        GameScreen.drawTurn(board, str(players[order]) + " turn!", \
                            players[order].getPieces())
        time = clock.tick(1000)  # Slow down the clock 1000/100 = 10 FPS
        for region in board:
            region.update(time, GameScreen.screen)
        pygame.display.flip()

    exit(0)
