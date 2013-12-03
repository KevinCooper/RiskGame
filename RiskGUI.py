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
        user32 = ctypes.windll.user32
        screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        '''End Reference'''
        pygame.init()
        self.size = self.width, self.height = screensize[0], screensize[1]
        #Draws the board
        self.screen = pygame.display.set_mode(self.size)
        self.black = 0, 0, 0
        self.screen.fill(self.black)
    
    def updateRegion(self):
        pass
    def drawBoard(self, board):
        pass
    def battleSequence(self, Agressor, Defender):
        pass
    def getEvent(self):
        #It should not return from this loop unless some scripted event occurs
        while True:            
            for event in pygame.event.get():
                #Handle key events
                if event.type == pygame.KEYUP: 
                    if event.key == pygame.K_ESCAPE:
                        return ("Exit")
                    if  event.key == pygame.K_SPACE:
                        return ("SpaceBar")  
                #Handle mouse events    
                if event.type == pygame.MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    print event.button
                    if event.button == 1:
                        return ("Left", mousex, mousey)
                    if event.button == 3:
                        return ("Right", mousex, mousey)

    

        