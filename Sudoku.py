import checkRules
import SudokuSolver

class Sudoku: 
	
    #Zero is used as a placeholder for undefined cells
    def __init__(self, array= [[0 for _ in range(9)] for _ in range(9)] ): 
        lenArray = len(array)
        if not(lenArray == 9):
            raise ValueError("Length {} of array not valid for initialising Sudoku class".format(lenArray))
        for i in range(0,lenArray):
            if not(len(array[i]) == 9):
                raise ValueError("Length {} of sub-array not valid for initialising Sudoku class".format(len(array[i])))
            for element in array[i]:
                if not(0<=element<=9):
                    raise ValueError("Value {} not valid for entry of init-array of class Sudoku".format(element))   

        self.array = array 

        self.possibleArray = [[[x for x in range(1,10)] for _ in range(9)] for _ in range(9)]
        for x in range(0,9):
            for y in range(0,9):
                number = self.array[x][y]
                if number != 0:
                    self.possibleArray[x][y] = []
                    self.removeNumberFromPossibleArray(x,y,number)                

        self.SudokuSolver = SudokuSolver.SudokuSolver(self)
    
    def removeNumberFromPossibleArray(self,x,y,number):
        self.possibleArray[x][y] = []

        #Remove number from corresponding row
        for i_x in range(0,9):
            if i_x != x:
                if number in self.possibleArray[i_x][y]:
                    self.possibleArray[i_x][y].remove(number)

        #Remove number from corresponding column
        for i_y in range(0,9):
            if i_y != y:
                if number in self.possibleArray[x][i_y]:
                    self.possibleArray[x][i_y].remove(number)

        #Remove number from corresponding box
        xBox = (x // 3)*3
        yBox = (y // 3)*3
        for i in range(0,3):
            for j in range(0,3):
                xTemp = xBox + i
                yTemp = yBox + j
                if (xTemp == x and yTemp == y):
                    continue
                else:
                    if number in self.possibleArray[xTemp][yTemp]:
                        self.possibleArray[xTemp][yTemp].remove(number)

    def print(self):
        print("Array:")
        for line in self.array:
            print(line)
        print("Possible Array:")
        for line in self.possibleArray: 
            print(line)
    
    def getRow(self, x):
        if not(0<=x<=8):
            raise ValueError("Value {} not valid for method getRow of class Sudoku".format(x))
        return self.array[x]
    
    def getCol(self,y):
        if not(0<=y<=8):
            raise ValueError("Value {} not valid for method getCol of class Sudoku".format(y))
        res = []
        for i in range(0,9):
            res.append(self.array[i][y])
        return res
    
    def cellValueDefined(self,x,y):
        if self.array[x][y] == 0:
            return False
        return True
    
    def setCellValue(self,x,y,value):
        if (not(0<=y<=8)) or (not(0<=x<=8)) or (not(0<=value<=9)):
            return ValueError("One of the values x={}, y={} and value={} isn't a valid argument for method setCellValue of class Sudoku".format(x,y,value))
    
        self.array[x][y] = value
        self.removeNumberFromPossibleArray(x,y,value)

    def isValid(self):
        return checkRules.puzzleValid(self.array) 