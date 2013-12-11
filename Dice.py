'''
@author: Kevin Cooper
@version: 0.0.1
@date: 01 Dec 13
@class: CS 359
@purpose: This file contains the class for a simulated dice.  When used, it \
returns a random number between 1 and the value chose when the dice was first\
 initialized
'''
import random
import os


class Dice:
    def __init__(self, sides):
        self._sides = sides
        random.seed(os.urandom(16))

    def rollDice(self):
        return random.randint(1, self._sides)
