import checkRules

class Sudoku: 
	
    #Zero is used as a placeholder for undefined cells
    def __init__(self, array= [[0 for _ in range(9)] for _ in range(9)] ): 
        self.array = array 

    def print(self):
        print(self.array)
    
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

    def isValid(self):
        return checkRules.puzzleValid(self.array) 