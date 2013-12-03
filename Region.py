'''
Created on Dec 2, 2013

@author: C15JREYNOR
'''
import CustomExceptionList as CEL

class Region(object):

    def __init__(self, player, units, name):
        self.name = name
        self.player = None
        self.units = 0
        
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
    
    def removeUnits(self, numberToRemove):
        try:
            if(self.units - numberToRemove <0):
                raise CEL.TooFewPiecesException
            self.units -= numberToRemove
        except CEL.TooFewPiecesException as error:
            error.handleItself()
            