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
        self.color = color
        self.pieces = pieces
        self.name = name
        self.cards = []
        
    def __str__(self):
        return self.name
        
    def getPieces(self):
        return self.pieces
    
    def getColor(self):
        return self.color
    
    def addCard(self, card):
        self.cards.append(card)
        
    def getCards(self):
        for item in self.cards:
            yield self.cards[item]
            
    def removeCard(self, card):
        try:
            if(self.cards == []):
                raise CEL.TooFewCardsException
            self.cards.remove(card)
        except CEL.TooFewCardsException as error:
            error.handleItself()
            
    def addPieces(self, numberToAdd):
        self.pieces += numberToAdd
        
    def removePieces(self, numberToLose):
        try:
            if(self.pieces - numberToLose < 0):
                CEL.TooFewPiecesException
            self.pieces -= numberToLose
        except CEL.TooFewPiecesException as error:
            error.handleItself()
            
        
        
            
    
        