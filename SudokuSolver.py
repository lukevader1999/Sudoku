import Sudoku

class SudokuSolver:

    def __init__(self, Sudoku):
        self.Sudoku = Sudoku

    def analysePossibleArray(self):
        #Wenn nur noch eine Zahl in einer Zelle möglich ist, sollte dieses gesetzt werden
        for x in range(0,9):
            for y in range(0,9):
                if len(self.Sudoku.possibleArray[x][y]) == 1:
                    self.Sudoku.setCellValue(x,y,self.Sudoku.possibleArray[x][y][0])

        #Wenn eine mögliche Zahl in einer Zeile oder Spalte nur einmal vorkommt, kann diese Gesetzt werden
        for z in range(0,9):
            self.checkRowForSingleAppearanceOfNumber(z)
            self.checkColumnForSingleAppearanceOfNumber(z) 
    
    def checkRowForSingleAppearanceOfNumber(self, x):
        counter = [0 for _ in range(9)]
        for y in range(0,9):
            for number in self.Sudoku.possibleArray[x][y]:
                counter[number] = counter[number] + 1
        
        for number in range(0,9):
            if counter[number] == 1:
                for y in range(0,9):
                    if number in self.Sudoku.possibleArray[x][y]:
                        self.Sudoku.setCellValue(x,y,number)

    def checkColumnForSingleAppearanceOfNumber(self, y):
        counter = [0 for _ in range(9)]
        for x in range(0,9):
            for number in self.Sudoku.possibleArray[x][y]:
                counter[number] = counter[number] + 1
        
        for number in range(0,9):
            if counter[number] == 1:
                for x in range(0,9):
                    if number in self.Sudoku.possibleArray[x][y]:
                        self.Sudoku.setCellValue(x,y,number)

