'''
@author: Kevin Cooper
@version: 0.0.2
@date: 01 Dec 13
@class: CS 359
'''
import pygame
import ctypes
import os
class RiskGUI(object):

    def __init__(self):
        '''Reference for screen width/height
        http://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python'''
        # user32 = ctypes.windll.user32
        # screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        '''End Reference'''
        pygame.init()
        # self.size = self.width, self.height = screensize[0], screensize[1]
        self.size = (1024, 768)
        # Draws the board
        self.screen         = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Kevin Cooper CS359 Project")
        self.white          = 255, 255, 255
        self.black          = 0, 0, 0
        self.red            = 255, 0, 0
        self.blue           = 0, 0, 255
        self.green          = 0, 255, 0
        self.font           = pygame.font.SysFont("monospace", 15)
        self.screen.fill(self.white)
        
        
    def clearScreen(self):
        self.screen.fill(self.white)
    
    def drawBoard(self, board):
        for region in board.getRegions():
            for neighbor in board.getNeighbors(region[0]):
                pygame.draw.line(self.screen, self.black, neighbor.getCenterPosition(), region[1].getCenterPosition(), 1)
        for region in board.getRegions(): 
            region[1].draw(self.screen)
            self.screen.blit(self.font.render(str(region[1].getUnits()), 1, self.black), (region[1].getCenterPosition()[0]+10,region[1].getCenterPosition()[1]-25 ))
        
    def drawTurn(self, board, player, pieces):
        self.screen.blit(self.font.render(str(player), 1, self.black), (10, 10))
        self.screen.blit(self.font.render("You can place this many pieces: " + str(pieces), 1, self.black), (10, 25))
        self.screen.blit(self.font.render("Press ESC to quit.", 1, self.black), (10, 40))
                
                
    def battleSequence(self, AgressorRegion, DefenderRegion, Dice):
        if(AgressorRegion.canAttack()):
            if(Dice.rollDice()>Dice.rollDice()):
                DefenderRegion.setAnimate()
                DefenderRegion.subUnits(1)
                if(DefenderRegion.getUnits() == 0):
                    DefenderRegion.setPlayer(AgressorRegion.getPlayer())
                    DefenderRegion.addUnits(1)
                    AgressorRegion.subUnits(1)
            else:
                AgressorRegion.setAnimate()
                AgressorRegion.subUnits(1)
    
    def moveSequence(self, sourceRegion, destRegion):
        if(sourceRegion.canMove()):
            sourceRegion.subUnits(1)
            destRegion.addUnits(1)
            #Fancy animation here
    
    def resolveEvent(self, board, event):          
        # Handle key events
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_ESCAPE:
                return ("Exit", "Junk")
            if  event.key == pygame.K_SPACE:
                return ("SpaceBar", "Junk")  
        # Handle mouse events    
        if event.type == pygame.MOUSEBUTTONUP:
            mousex, mousey = event.pos
            #print event.button
            if event.button == 1:
                for region in board.getRegions():
                    if(region[1].wasClicked(mousex, mousey)):
                        return ("Region", "Left", region)
                return ("Left", mousex, mousey)
            if event.button == 3:
                for region in board.getRegions():
                    if(region[1].wasClicked(mousex, mousey)):
                        return ("Region", "Right", region)
                return ("Right", mousex, mousey)
                        

    

        
