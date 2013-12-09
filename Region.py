'''
@author: Kevin Cooper
@version: 0.0.1
@date: 01 Dec 13
@class: CS 359
'''
import CustomExceptionList as CEL
import pygame
import math
class Region(object):

    def __init__(self, image, player, units, name, position):
        self.image = image
        self.name = name
        self.player = None
        self.units = 0
        self.position = position 
        
    def __eq__(self, otherRegion):
        return otherRegion.getName() == self.name
    
    def __str__(self):
        return self.name
    
    def setPlayer(self, player):
        self.player = player
        
    def addUnits(self, number):
        self.units += number
        
    def getName(self):
        return self.name
    
    def draw(self, screen):
        screen.blit(self.image, self.position)
        
    def getCenterPosition(self):
        # ADD 10,10 because circle of radius 10!!
        return (self.position[0]+10, self.position[1]+10)

    def wasClicked(self, mouseX, mouseY):
        
        if(mouseX < 0 or mouseY < 0):
            CEL.DetailedException("A mouse event was called on a region with a mouse value that was less than zero.")
            
        try:
            if (math.fabs( mouseX-self.position[0])<20 and math.fabs( mouseY-self.position[1])<20):
                return True
            else:
                return False
        except Exception as e:
            print("Error in the wasClicked method:\n %s" %(e.message))
            
    
    def removeUnits(self, numberToRemove):
        try:
            if(self.units - numberToRemove <0):
                raise CEL.TooFewPiecesException
            self.units -= numberToRemove
        except CEL.TooFewPiecesException as error:
            error.handleItself()
            