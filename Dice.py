'''
@author: Kevin Cooper
@version: 0.0.1
@date: 01 Dec 13
@class: CS 359
@purpose: This file contains the class for a simulated dice.
'''
import random
import os


class Dice:
    '''
    When used, it returns a random number between 1 and the\
    value chosen when the dice was first initialized
    '''
    def __init__(self, sides):
        '''
        sides - integer

        Takes an integer number of simulated sides that the dice\
        should have.
        '''
        self._sides = sides
        random.seed(os.urandom(16))

    def rollDice(self):
        '''
        return - integer

        Returns a random integer number between 1 and sides.  The sequence of \
        numbers will be different for each dice used
        '''
        return random.randint(1, self._sides)
