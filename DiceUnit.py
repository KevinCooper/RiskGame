'''
Created on Dec 11, 2013

@author: C15Kevin.Cooper
'''
import unittest
import Dice


class Test(unittest.TestCase):

    def testDiceAboveZero(self):
        testDice =  Dice.Dice(6)
        Test.assertGreater(self, testDice.rollDice(), 0, "The dice returned a number less than or equal to 0")
        Test.assertGreater(self, testDice.rollDice(), 0, "The dice returned a number less than or equal to 0")
        Test.assertGreater(self, testDice.rollDice(), 0, "The dice returned a number less than or equal to 0")
        Test.assertGreater(self, testDice.rollDice(), 0, "The dice returned a number less than or equal to 0")
        Test.assertGreater(self, testDice.rollDice(), 0, "The dice returned a number less than or equal to 0")
    def testDiceBelowMax(self):
        testDice =  Dice.Dice(6)
        Test.assertLessEqual(self, testDice.rollDice(), 6, "The dice returned a number greater than 0")
        Test.assertLessEqual(self, testDice.rollDice(), 6, "The dice returned a number greater than 0")
        Test.assertLessEqual(self, testDice.rollDice(), 6, "The dice returned a number greater than 0")
        Test.assertLessEqual(self, testDice.rollDice(), 6, "The dice returned a number greater than 0")
        Test.assertLessEqual(self, testDice.rollDice(), 6, "The dice returned a number greater than 0")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()