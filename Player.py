'''
Created on Dec 2, 2013

@author: C15JREYNOR
'''
import Card
import CustomExceptionList as CEL

class Player:
    def __init__(self, color, order, pieces):
        self.color = color
        self.order = order
        self.pieces = pieces
        self.cards = []
        
    def getPieces(self):
        return self.pieces
    
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
            
        
        
            
    
        