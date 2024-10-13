#Checks validity for the whole configuarion
def puzzleValid(puzzle):
    #Check validity for every single tiles
    for i in range(0,9):
        for j in range(0,9):
            if puzzle[i][j] != 0:
                if not (rowValid(puzzle,i,j) and columnValid(puzzle,i,j) and boxValid(puzzle,i,j)):
                    return False
    return True

#Check row validity of a single tile
def rowValid(puzzle,x,y):
    check = True
    value = puzzle[x][y]
    for i in range(0,9):
        if i != y:
            if puzzle[x][i] == value:
                check = False
    return check

#Check column validity of a single tile
def columnValid(puzzle,x,y):
    check = True
    value = puzzle[x][y]
    for i in range(0,9):
        if i != x:
            if puzzle[i][y] == value:
                check = False
    return check

#Check box validity of a single tile
def boxValid(puzzle,x,y):
    check = True
    value = puzzle[x][y]
    xBox = (x // 3)*3
    yBox = (y // 3)*3
    for i in range(0,3):
        for j in range(0,3):
            xTemp = xBox + i
            yTemp = yBox + j
            if (xTemp != x and yTemp != y):
                if puzzle[xTemp][yTemp] == value:
                    check = False
    return check