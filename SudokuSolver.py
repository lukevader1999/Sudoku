from Sudoku import *
 
class SudokuSolver(Sudoku):   

    def __init__(self, arrayGrid):
        super().__init__(arrayGrid)
        self.somethingChanged = False 

    def checkCellForSingle(self,cell):
        if len(cell.possibleValues) == 1:
            self.setCellValue(cell,cell.possibleValues[0])
            self.somethingChanged = True

    def checkSinglePossibleInCell(self):
        for row in self.getRows():
            for cell in row:
                if len(cell.possibleValues) == 1:
                    self.setCellValue(cell,cell.possibleValues[0])
                    self.somethingChanged = True   

    def checkForSingleAppearenceOfNumberInRowcolbox(self,rowcolbox,number):
        counter = [0 for _ in range(0,10)]
        for cell in rowcolbox:
            for number in cell.possibleValues:
                counter[number] += 1

        for number in range(1,10):
            if counter[number] == 1:
                for cell in rowcolbox:
                    if number in cell.possibleValues:
                        self.setCellValue(cell,number)
                        self.somethingChanged = True   

    def checkSingleAppearences(self):
        self.checkSinglePossibleInCell()

        for row in self.getRows():
            for number in range(1,10):
                self.checkForSingleAppearenceOfNumberInRowcolbox(row,number)   

        for column in self.getColumns():
            for number in range(1,10):
                self.checkForSingleAppearenceOfNumberInRowcolbox(column,number) 

        for box in self.getBoxes():
            for number in range(1,10):
                self.checkForSingleAppearenceOfNumberInRowcolbox(box,number)   

    def solve(self):
        self.checkSingleAppearences()
        counter = 1
        while self.somethingChanged: 
            #print(counter)
            self.somethingChanged = False
            self.checkSingleAppearences()
            counter += 1
        print("I could solve the sudoku to this result in {} iterations:".format(counter))
        self.print()