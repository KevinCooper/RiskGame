'''
@author: Kevin Cooper
@version: 0.0.1
@date: 01 Dec 13
@class: CS 359
'''
import pygame
import ctypes

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
        self.screen = pygame.display.set_mode(self.size)
        self.white = 255, 255, 255
        self.black = 0, 0, 0
        self.red = 255, 0, 0
        self.blue = 0, 0, 255
        self.green = 0, 255, 0
        self.screen.fill(self.white)
        self.font = pygame.font.SysFont("monospace", 15)
    
    def updateRegion(self, board, region):
        pygame.display.flip()
        pass
    
    def drawBoard(self, board):
        for region in board.getRegions():
            region[1].draw(self.screen)
            for neighbor in board.getNeighbors(region[0]):
                pygame.draw.line(self.screen, self.black, neighbor.getCenterPosition(), region[1].getCenterPosition(), 1)
            self.screen.blit(self.font.render(str(region[1].getUnits()), 1, self.black), (region[1].getCenterPosition()[0]+10,region[1].getCenterPosition()[1]-10 ))
        pygame.display.flip()
        
    def drawTurn(self, board, player):
        self.screen.blit(self.font.render(str(player), 1, self.black), (10, 10))
        pygame.display.flip()
                
                
    def battleSequence(self, AgressorRegion, DefenderRegion):
        pass
    
    
    def getEvent(self, board):
        # It should not return from this loop unless some scripted event occurs
        while True:            
            for event in pygame.event.get():
                # Handle key events
                if event.type == pygame.KEYUP: 
                    if event.key == pygame.K_ESCAPE:
                        return ("Exit")
                    if  event.key == pygame.K_SPACE:
                        return ("SpaceBar")  
                # Handle mouse events    
                if event.type == pygame.MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    print event.button
                    if event.button == 1:
                        for region in board.getRegions():
                            if(region[1].wasClicked(mousex, mousey)):
                                return ("Region", "Left", region)
                    if event.button == 3:
                        for region in board.getRegions():
                            if(region[1].wasClicked(mousex, mousey)):
                                return ("Region", "Right", region)

    

        
