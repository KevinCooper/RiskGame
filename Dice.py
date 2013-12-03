'''
Created on Dec 2, 2013

@author: C15JREYNOR
'''
import random
class Dice:
    def __init__(self, sides):
        self.sides = sides
        random.seed(1)
    def rollDice(self):
        return random.randint(1,self.sides)
        