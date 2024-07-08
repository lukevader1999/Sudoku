import unittest
from checkRules import *

# test_module1.py
class Test_checkRules(unittest.TestCase):

    #This functions does the setUp before every thest
    def setUp(self):
        self.array = [[0 for _ in range(9)] for _ in range(9)]

    def test_rowValid(self):
        self.array[0][0] = 1
        self.assertEqual(rowValid(self.array,0,0),True)

        self.array[0][8] = 1
        self.assertEqual(rowValid(self.array,0,0),False)

    def test_columnValid(self):
        self.array[0][0] = 1
        self.assertEqual(columnValid(self.array,0,0),True)

        self.array[8][0] = 1
        self.assertEqual(columnValid(self.array,0,0),False)

    def test_boxValid(self):
        self.array[0][0] = 1
        self.assertEqual(boxValid(self.array,0,0),True)

        self.array[1][1] = 1
        self.assertEqual(boxValid(self.array,0,0),False)

    def test_puzzleValid(self):
        self.array[0][0] = 1
        self.assertEqual(rowValid(self.array,0,0),True)

        self.array[0][8] = 1
        self.assertEqual(rowValid(self.array,0,0),False)
        self.array[0][8] = 0 

        self.array[8][0] = 1
        self.assertEqual(columnValid(self.array,0,0),False)
        self.array[8][0] = 0 

        self.array[1][1] = 1
        self.assertEqual(boxValid(self.array,0,0),False)
        self.array[1][1] = 0 
        