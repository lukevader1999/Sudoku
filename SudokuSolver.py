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
        for x in range(0,3):
            for y in range(0,3):
                self.checkBoxForSingleAppearanceOfNumber(x*3,y*3)
    
    def checkRowForSingleAppearanceOfNumber(self, x):
        #Counter has length of 10, so position i can reference number i
        counter = [0 for _ in range(10)]
        for y in range(0,9):
            for number in self.Sudoku.possibleArray[x][y]:
                counter[number] = counter[number] + 1
        
        for number in range(1,10):
            if counter[number] == 1:
                for y in range(0,9):
                    if number in self.Sudoku.possibleArray[x][y]:
                        self.Sudoku.setCellValue(x,y,number)

    def checkColumnForSingleAppearanceOfNumber(self, y):
        #Counter has length of 10, so position i can reference number i
        counter = [0 for _ in range(10)]
        for x in range(0,9):
            for number in self.Sudoku.possibleArray[x][y]:
                counter[number] = counter[number] + 1
        
        for number in range(1,10):
            if counter[number] == 1:
                for x in range(0,9):
                    if number in self.Sudoku.possibleArray[x][y]:
                        self.Sudoku.setCellValue(x,y,number)

    def checkBoxForSingleAppearanceOfNumber(self,x,y):
        #Counter has length of 10, so position i can reference number i
        counter = [0 for _ in range(10)]
        for x in range(0,9):
            for number in self.Sudoku.possibleArray[x][y]:
                counter[number] = counter[number] + 1

        xBox = (x // 3)*3
        yBox = (y // 3)*3
        for i in range(0,3):
            for j in range(0,3):
                xTemp = xBox + i
                yTemp = yBox + j
                for number in self.Sudoku.possibleArray[xTemp][yTemp]:
                    counter[number] = counter[number] + 1

        for number in range(1,10):
            if counter[number] == 1:
                for i in range(0,3):
                    for j in range(0,3):
                        xTemp = xBox + i
                        yTemp = yBox + j
                        if number in self.Sudoku.possibleArray[xTemp][yTemp]:
                            self.Sudoku.setCellValue(x,y,number)