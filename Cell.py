class Cell:

    def __init__(self,x,y,value=0):
        self.x = x
        self.y = y
        self.value = value
        self.possibleValues = [_ for _ in range(1,10)]   

    def __eq__(self, other):
        if not isinstance(other, Cell):
            print("Error with = cell")
            return None
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def print(self):
        print(self.possibleValues)