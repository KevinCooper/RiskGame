'''
Created on Dec 12, 2013

@author: Kevin Cooper
'''
import unittest
import RiskBoard


class Test(unittest.TestCase):

    def testBoard(self):
        testBoard = RiskBoard.RiskBoard(10)
        Test.assertEqual(self, len(testBoard.getRegions()), 13, "The board \
            did not initialize with the right number of players")
        Test.assertTrue(self, testBoard.areNeighbors(testBoard._regions["ce1"]\
            , testBoard._regions["ce2"]), "ce1 and ce2 are supposed \
            to be connected")
        Test.assertTrue(self, testBoard.areNeighbors(testBoard._regions["tl5"]\
            , testBoard._regions["ce7"]), "tl5 and ce7 are supposed to \
            be connected")
        Test.assertTrue(self, testBoard.areNeighbors(testBoard._regions["tl1"]\
            , testBoard._regions["tl2"]), "tl1 and tl2 are supposed to \
            be connected")
        Test.assertTrue(self, testBoard.areNeighbors(testBoard._regions["tl6"]\
            , testBoard._regions["tl3"]), "tl6 and tl3 are supposed to \
            be connected")
        Test.assertTrue(self, testBoard.areNeighbors(testBoard._regions["tl3"]\
            , testBoard._regions["tl6"]), "tl3 and tl6 are suposed to \
            be connected")
        Test.assertTrue(self, testBoard.areNeighbors(testBoard._regions["ce6"]\
            , testBoard._regions["ce7"]), "ce6 and ce7 are suposed to \
            be connected")
        Test.assertTrue(self, testBoard.areNeighbors(testBoard._regions["ce7"]\
            , testBoard._regions["ce6"]), "ce7 and ce6 are suposed to \
            be connected")
        Test.assertTrue(self, testBoard.areNeighbors(testBoard._regions["ce2"]
            , testBoard._regions["ce5"]), "ce2 and ce5 are suposed to \
            be connected")
        Test.assertEqual(self, len(testBoard.getNeighbors("ce2")), 3, "ce2 \
            does not have the right number of connections")
        Test.assertEqual(self, len(testBoard.getNeighbors("tl5")), 3, "tl5 \
        does not have the right number of connections")
        Test.assertEqual(self, len(testBoard.getNeighbors("ce1")), 2, "ce1 \
        does not have the right number of connections")
        Test.assertEqual(self, len(testBoard.getNeighbors("tl3")), 2, "tl3 \
        does not have the right number of connections")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()