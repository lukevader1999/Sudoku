import Sudoku

class SudokuSolver:

    def __init__(self, Sudoku):
        self.Sudoku = Sudoku

    def analysePossibleArray(self):
        result = False
        #Wenn nur noch eine Zahl in einer Zelle möglich ist, sollte dieses gesetzt werden
        for x in range(0,9):
            for y in range(0,9):
                if len(self.Sudoku.possibleArray[x][y]) == 1:
                    self.Sudoku.setCellValue(x,y,self.Sudoku.possibleArray[x][y][0])
                    result = True

        #Wenn eine mögliche Zahl in einer Zeile oder Spalte nur einmal vorkommt, kann diese Gesetzt werden
        for z in range(0,9):
            if self.checkRowForSingleAppearanceOfNumber(z):
                result = True
            if self.checkColumnForSingleAppearanceOfNumber(z):
                result = True
        for x in range(0,3):
            for y in range(0,3):
                if self.checkBoxForSingleAppearanceOfNumber(x*3,y*3):
                    result = True
        
        #Wenn bisher nichts passiert ist, überprüfen wir die Rows auf nützliche Duos
        for y in range(0,9):
            if self.checkRowForDuos(y):
                return True
        
        #Wenn immer noch nichts passiert ist, überprüfen wir die Rows auf nützliche Trios
        for y in range(0,9):
            if self.checkRowForTrios(y):
                return True

        return result
    
    def countRow(self,x):
        counter = [0 for _ in range(10)]
        for y in range(0,9):
            for number in self.Sudoku.possibleArray[x][y]:
                counter[number] = counter[number] + 1
        return counter

    def checkRowForSingleAppearanceOfNumber(self, x):
        result = False
        #Counter has length of 10, so position i can reference number i
        counter = self.countRow(x) 
        
        for number in range(1,10):
            if counter[number] == 1:
                for y in range(0,9):
                    if number in self.Sudoku.possibleArray[x][y]:
                        self.Sudoku.setCellValue(x,y,number)
                        result = True
        return result

    def checkColumnForSingleAppearanceOfNumber(self, y):
        result = False
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
                        result = True
        return result

    def checkBoxForSingleAppearanceOfNumber(self,x,y):
        result = False
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
                            result = True
        return result
    
    def checkRowForDuos(self,y):
        result = False
        possibleUsefullDuos = []

        #Iterate through duos
        for x in range(0,8):
            cell = self.Sudoku.possibleArray[x][y]
            if len(cell)!=2:
                continue
            for x2 in range(x+1,9):
                cell2 = self.Sudoku.possibleArray[x2][y]
                if len(cell2)!=2:
                    continue
                if cell[0] == cell2[0] and cell[1] == cell2[1]:
                    possibleUsefullDuos.append([x,x2])
        
        #Check if the duos actually remove possibilitys from the row
        for duo in possibleUsefullDuos:
            x1 = duo[0]
            x2 = duo[1]
            duoValues=self.Sudoku.possibleArray[x1][y]
            for x in range(0,9):
                if (x != x1) and (x != x2):
                    for value in self.Sudoku.possibleArray[x][y]:
                        if value in duoValues:
                            result = True
                            self.Sudoku.possibleArray[x][y].remove(value)
        
        return result

    def checkRowForTrios(self,y):
        result = False
        possibleUsefullTrios = []

        #Iterate through trios of cells and check if they are trios
        for x in range(0,7):
            cell = self.Sudoku.possibleArray[x][y]
            if len(cell)!=2 and len(cell)!=3:
                continue
            for x2 in range(x+1,8):
                cell2 = self.Sudoku.possibleArray[x2][y]
                if len(cell2)!=2 and len(cell2)!=3:
                    continue
                possibles = set()
                for number in cell:
                    possibles.add(number)
                for number in cell2:
                    possibles.add(number)
                if len(possibles)>=4:      
                    continue
                for x3 in range(x2+1,8):
                    cell3 = self.Sudoku.possibleArray[x2][y]
                    if len(cell3)!=2 and len(cell3)!=3:
                        continue
                    possibles2 = set()
                    for number in cell:
                        possibles2.add(number)
                    for number in cell2:
                        possibles2.add(number)
                    if len(possibles2)<=3:      
                        possibleUsefullTrios.append([x,x2,x3])
        
        #Check if the duos actually remove possibilitys from the row
        for trio in possibleUsefullTrios:
            x1 = trio[0]
            x2 = trio[1]
            x3 = trio[2]
            trioValues=set()
            for number in self.Sudoku.possibleArray[x1][y]:
                trioValues.add(number)
            for number in self.Sudoku.possibleArray[x2][y]:
                trioValues.add(number)
            for number in self.Sudoku.possibleArray[x3][y]:
                trioValues.add(number)
            for x in range(0,9):
                if (x != x1) and (x != x2) and (x != x3):
                    for value in self.Sudoku.possibleArray[x][y]:
                        if value in trioValues:
                            result = True
                            print("Removing possible Value {} from cell {},{}".format(value,x,y))
                            print("Using following row:")
                            print(Sudoku.possibleArray)
                            print(self.Sudoku.possibleArray[x][y])
                            self.Sudoku.possibleArray[x][y].remove(value)
        
        return result