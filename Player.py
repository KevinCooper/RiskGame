'''
@author: Kevin Cooper
@version: 0.0.3
@date: 01 Dec 13
@class: CS 359
'''


class Player:
    '''
    Class that contains information about a player
    '''
    def __init__(self, color, pieces, name):
        '''
        color - 3 integer tuple
        pieces - integer number of starting pieces
        name - string player name
        '''
        self._color = color
        self._pieces = pieces
        self._name = name
        self._cards = []

    def __str__(self):
        '''
        return - String player name
        '''
        return self._name

    def getPieces(self):
        '''
        return - integer number of pieces the player has
        '''
        return self._pieces

    def getColor(self):
        '''
        return - 3 integer tuple representing the RGB color values
        '''
        return self._color

    def addCard(self, card):
        ''' Not implemented'''
        self._cards.append(card)

    def getCards(self):
        ''' Not implemented'''
        for item in self._cards:
            yield self._cards[item]

    def removeCard(self, card):
        ''' Not implemented'''
        try:
            self._cards.remove(card)
        except:
            pass

    def addPieces(self, numberToAdd):
        '''
        numberToAdd - integer

        Adds the given number to the total number of pieces the player has.
        '''
        self._pieces += numberToAdd

    def removePieces(self, numberToLose):
        '''
        numberToLose - integer

        Subtracts the given number to the total number of pieces the player has.
        '''
        if(self._pieces - numberToLose < 0):
            self._pieces = 0
            return False
        else:
            self._pieces -= numberToLose
            return True
