'''
@author: Kevin Cooper
@version: 0.0.2
@date: 01 Dec 13
@class: CS 359
'''
import Card
import CustomExceptionList as CEL

class Player:
    def __init__(self, color, pieces, name):
        self._color = color
        self._pieces = pieces
        self._name = name
        self._cards = []
        
    def __str__(self):
        return self._name
        
    def getPieces(self):
        return self._pieces
    
    def getColor(self):
        return self._color
    
    def addCard(self, card):
        self._cards.append(card)
        
    def getCards(self):
        for item in self._cards:
            yield self._cards[item]
            
    def removeCard(self, card):
        try:
            if(self._cards == []):
                raise CEL.TooFewCardsException
            self._cards.remove(card)
        except CEL.TooFewCardsException as error:
            error.handleItself()
            
    def addPieces(self, numberToAdd):
        self._pieces += numberToAdd
        
    def removePieces(self, numberToLose):
        if(self._pieces - numberToLose < 0):
            return False
        self._pieces -= numberToLose
        return True