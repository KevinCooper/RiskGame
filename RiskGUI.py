'''
Created on Dec 2, 2013

@author: C15Kevin.Cooper
'''
import pygame
import ctypes

class RiskGUI(object):

    def __init__(self):
        #Reference for screen width/height
        #http://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python
        user32 = ctypes.windll.user32
        screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        print screensize  
        #End Reference
        pygame.init()
        self.size = self.width, self.height = screensize[0], screensize[1]
        #Draws the board
        self.screen = pygame.display.set_mode(self.size)
    
    def updateRegion(self):
        pass
    def drawBoard(self):
        pass
    def battleSequence(self, Agressor, Defender):
        pass
    def getEvent(self):
        event = pygame.event.get()
                
        for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    return ("Exit")
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    return ("SpaceBar")
        return ("None")
    

        