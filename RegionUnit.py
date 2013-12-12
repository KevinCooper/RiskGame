'''
Created on Dec 11, 2013

@author: C15Kevin.Cooper
'''
import unittest
import Region


class Test(unittest.TestCase):

    def testReigon(self):
        testRegion = Region.Region("test1", (300, 300))
        Test.assertEqual(self, testRegion.getName(), "test1", "The region \
            does not have the correct name")
        Test.assertEqual(self, testRegion.getUnits(), 0, "The region started \
            with the wrong number of pieces")
        Test.assertFalse(self, testRegion.canAttack(), "The region was able \
            to attack with the incorrect amount of units")
        Test.assertFalse(self, testRegion.canMove(), "The region was able to \
            move with the incorrect amount of units")
        Test.assertEqual(self, testRegion.getPlayer(), None, "Somehow the \
            Region already has a player")
        Test.assertEqual(self, testRegion.getUnits(), 0, "Somehow the region \
            has acquired units")
        testRegion.addUnits(1)
        Test.assertFalse(self, testRegion.canAttack(), "The region was able \
            to attack with the incorrect amount of units")
        Test.assertFalse(self, testRegion.canMove(), "The region was able \
            to move with the incorrect amount of units")
        Test.assertEqual(self, testRegion.getUnits(), 1, "Somehow the region \
            has incorrect number of units")
        testRegion.addUnits(1)
        Test.assertTrue(self, testRegion.canAttack(), "The region was not able \
            to attack with the correct amount of units")
        Test.assertTrue(self, testRegion.canMove(), "The region was not able \
            to move with the correct amount of units")
        Test.assertEqual(self, testRegion.getUnits(), 2, "Somehow the region \
            has incorrect number of units")
        testRegion.removeUnits(3)
        Test.assertFalse(self, testRegion.canAttack(), "The region was able \
            to attack with the incorrect amount of units")
        Test.assertFalse(self, testRegion.canMove(), "The region was able to \
            move with the incorrect amount of units")
        Test.assertEqual(self, testRegion.getUnits(), 0, "Somehow the region \
            has incorrect number of units")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testReigon']
    unittest.main()