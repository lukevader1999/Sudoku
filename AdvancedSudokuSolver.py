from SudokuSolver import *
from Cell import *

class AdvancedSudokuSolver(SudokuSolver):
    def __init__(self, arrayGrid):
        super().__init__(arrayGrid)
    
    def solve(self):
        self.checkSingleAppearences()
        counter = 1

        while self.somethingChanged: 
            #print(counter)
            self.somethingChanged = False
            self.checkSingleAppearences()
            self.checkDoubles()
            self.checkTriples()
            counter += 1

        print("I could solve the sudoku to this result in {} iterations:".format(counter))
        self.print()
    
    def checkDoubles(self):
        for row in self.getRows():
            self.doublesInRowcolbox(row)
        for column in self.getColumns():
            self.doublesInRowcolbox(column)
        for box in self.getBoxes():
            self.doublesInRowcolbox(box)

    def checkTriples(self):
        for row in self.getRows():
            self.triplesInRowcolbox(row)
        for column in self.getColumns():
            self.triplesInRowcolbox(column)
        for box in self.getBoxes():
            self.triplesInRowcolbox(box)

    def doublesInRowcolbox(self,rowcolbox):
        for cell1 in rowcolbox:
            if len(cell1.possibleValues) != 2:
                continue
            for cell2 in rowcolbox:
                if cell1 == cell2:
                    continue
                if len(cell2.possibleValues) != 2:
                    continue
                contVariable = False
                for i in range(0,2):
                    if cell1.possibleValues[i] != cell2.possibleValues[i]:
                        contVariable = True
                if contVariable:
                    continue
                for cell in rowcolbox:
                    if cell == cell1 or cell == cell2:
                        continue
                    for number in cell1.possibleValues:
                        if number in cell.possibleValues:
                            self.somethingChanged = True
                            cell.possibleValues.remove(number)
                            self.checkCellForSingle(cell)

    def triplesInRowcolbox(self, rowcolbox):
        for cell1 in rowcolbox:
            tempLen =len(cell1.possibleValues) 
            if tempLen>=4 or tempLen<=1:
                continue
            possibleSet1 = set(cell1.possibleValues)
            for cell2 in rowcolbox:
                if cell1 == cell2:
                    continue
                tempLen =len(cell2.possibleValues) 
                if tempLen>=4 or tempLen<=1:
                    continue
                possibleSet2 = possibleSet1.union(set(cell2.possibleValues))
                if len(possibleSet2) >= 4:
                    continue
                for cell3 in rowcolbox:
                    if cell1 == cell3 or cell2 == cell3:
                        continue
                    tempLen =len(cell3.possibleValues) 
                    if tempLen>=4 or tempLen<=1:
                        continue
                    possibleSet3 = possibleSet2.union(set(cell3.possibleValues))
                    if len(possibleSet3) >= 4:
                        continue
                    #Now remove the triple
                    for cell in rowcolbox:
                        if cell == cell1 or cell == cell2 or cell == cell3:
                            continue
                        for number in possibleSet3:
                            if number in cell.possibleValues:
                                print("Found triple:")
                                print("x={} ,y={} , possibleValues={}".format(cell1.x,cell1.y,cell1.possibleValues))
                                print("x={} ,y={} , possibleValues={}".format(cell1.x,cell2.y,cell2.possibleValues))
                                print("x={} ,y={} , possibleValues={}".format(cell3.x,cell3.y,cell3.possibleValues))
                                print("In Grid:")
                                self.printPossibles()
                                print("Removing {} from x={}, y={}".format(number,cell.x,cell.y))
                                self.somethingChanged = True
                                cell.possibleValues.remove(number)
                                self.checkCellForSingle(cell)