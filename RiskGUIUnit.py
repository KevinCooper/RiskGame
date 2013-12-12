'''
Created on Dec 12, 2013

@author: Kevin Cooper
'''
import unittest
import RiskGUI
import Region


class Test(unittest.TestCase):

    def testRiskGUI(self):
        gui = RiskGUI.RiskGUI()
        region1 = Region.Region("one", (10, 10))
        region2 = Region.Region("two", (20, 20))
        region1.addUnits(3)
        region2.addUnits(3)
        gui.moveSequence(region1, region2)
        Test.assertEqual(self, region1.getUnits(), 2, "The first region has the incorrect amount of units")
        Test.assertEqual(self, region2.getUnits(), 4, "The first region has the incorrect amount of units")
        '''
        Can't test battle, since the dice rolls are internal
        Can't test any of the GUI actions
        '''

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testRiskGUI']
    unittest.main()