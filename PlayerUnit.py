'''
Created on Dec 11, 2013

@author: C15Kevin.Cooper
'''
import unittest
import Player


class Test(unittest.TestCase):

    def testPlayer(self):
        red = (255, 0, 0)
        startPieces = 10
        playerName = "Player 1"
        testPlayer = Player.Player(red, startPieces, playerName)
        Test.assertEqual(self, testPlayer.getPieces(), startPieces, "The \
            player does not have the correct starting pieces")
        Test.assertEqual(self, testPlayer.__str__(), playerName, "The string \
            representation of the player was not correct")
        testPlayer.addPieces(5)
        Test.assertEqual(self, testPlayer.getPieces(), startPieces + 5, "The \
            player does not have the correct pieces after adding 5")
        testPlayer.removePieces(10)
        Test.assertEqual(self, testPlayer.getPieces(), startPieces - 5, "The \
            player does not have the correct pieces after subtracting 10 \
            pieces")
        testPlayer.removePieces(10)
        Test.assertEqual(self, testPlayer.getPieces(), 0, "The player does not \
                have the correct pieces after subtracting 10 more pieces")
        testPlayer.removePieces(10)
        Test.assertEqual(self, testPlayer.getPieces(), 0, "The player does not \
            have the correct pieces after subtracting 30 pieces")

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
