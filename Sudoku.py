from Cell import *

class Sudoku:

    def __init__(self, arrayGrid = [[0 for _ in range(0,9)] for _ in range(0,9)]):
        self.arrayGrid = arrayGrid
        self.cellGrid = []
        for x in range(0,9):
            self.cellGrid.append([])
            for y in range(0,9):
                self.cellGrid[x].append(Cell(x,y))

        for x in range(0,9):
            for y in range(0,9):
                if arrayGrid[x][y] != 0:
                    self.setCellValue(self.cellGrid[x][y],arrayGrid[x][y]) 

    def getRows(self):
        return self.cellGrid   

    def getColumns(self):
        res = []
        for x in range(0,9):
            res.append(self.getColumn(self.cellGrid[x][0]))
        return res 

    def getBoxes(self):
        res = []
        for x in range(0,3):
            for y in range(0,3):  
                res.append(self.getBox(self.cellGrid[x*3][y*3]))
        return res

    def getRow(self, cell):
        return self.cellGrid[cell.x]   

    def getColumn(self, cell):
        res = []
        for x in range(0,9):
            res.append(self.cellGrid[x][cell.y])
        return res 

    def getBox(self, cell):
        res = []
        xBox = (cell.x // 3)*3
        yBox = (cell.y // 3)*3
        for x in range(0,3):
            for y in range(0,3):
                res.append(self.cellGrid[xBox +x][yBox+y])
        return res

    def setManual(self):
        self.setCellValue(self.cellGrid[0][0],1) 

    def setCellValue(self,cell,value):
        cell.value = value
        cell.possibleValues = [] 

        for rowCell in self.getRow(cell):
            if value in rowCell.possibleValues:
                rowCell.possibleValues.remove(value) 

        for columnCell in self.getColumn(cell):
            if value in columnCell.possibleValues:
                columnCell.possibleValues.remove(value) 

        for boxCell in self.getBox(cell):
            if value in boxCell.possibleValues:
                boxCell.possibleValues.remove(value)   

    def print(self):
        print("Sudoku Grid:")
        for x in range(0,9):
            for y in range(0,9):
                print(self.cellGrid[x][y].value, end = " ")
            print()   

    def printPossibles(self):
        print("Possible Sudoku Grid:")
        for x in range(0,9):
            for y in range(0,9):
                print(self.cellGrid[x][y].possibleValues, end = " ")
            print()