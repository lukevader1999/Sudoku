class Cell:

    def __init__(self,x,y,value=0):
        self.x = x
        self.y = y
        self.value = value
        self.possibleValues = [_ for _ in range(1,10)]   

    def print(self):
        print(self.possibleValues)