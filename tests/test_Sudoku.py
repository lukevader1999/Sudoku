import unittest
from Sudoku import *

# test_module1.py
class TestSudoku(unittest.TestCase):

    #This functions does the setUp before every test
    def setUp(self):
        self.Sudoku = Sudoku()

    def test_init(self):
        self.assertEqual(self.Sudoku.array, [[0 for _ in range(9)] for _ in range(9)])
        self.assertEqual(len(self.Sudoku.array),9) 
        self.assertEqual(len(self.Sudoku.array[0]),9) 
        self.assertEqual(self.Sudoku.array[0][0],0)

    def test_setCellValue(self):
        self.Sudoku.setCellValue(0,0,1)
        self.assertEqual(self.Sudoku.array[0][0],1)

    def test_isValid(self):
        self.assertEqual(self.Sudoku.isValid(), True)
        
        self.Sudoku.setCellValue(0,0,1)
        self.assertEqual(self.Sudoku.isValid(), True)

        self.Sudoku.setCellValue(0,8,1)
        self.assertEqual(self.Sudoku.array[0][0], 1)
        self.assertEqual(self.Sudoku.array[0][8], 1)
        self.assertEqual(self.Sudoku.isValid(), False)
        self.Sudoku.setCellValue(0,8,0)

        self.Sudoku.setCellValue(8,0,1)
        self.assertEqual(self.Sudoku.isValid(), False)
        self.Sudoku.setCellValue(8,0,0)

        self.Sudoku.setCellValue(1,1,1)
        self.assertEqual(self.Sudoku.isValid(), False)
        self.Sudoku.setCellValue(1,1,0)
        
if __name__ == '__main__':
    unittest.main()
