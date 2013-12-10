'''
@author: Kevin Cooper
@version: 0.0.1
@date: 01 Dec 13
@class: CS 359
'''
import random
class Dice:
    def __init__(self, sides):
        self.sides = sides
        random.seed(1)
    def rollDice(self):
        return random.randint(1, self.sides)
        
