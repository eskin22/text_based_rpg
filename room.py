import squares

class Room(list):
    def __init__(self):
        super().__init__()
        self.name = None
        self.row = None
        self.square = None
    
    def toStringByRow(self, row):
        for square in self[row]:
            print(square.name)

    def addRows(self, rows):
        self.extend(rows)

    def toString(self):
        count = 0
        for row in self:
            count += 1
            rowSquares = [square.name for square in row]
            print(f"ROW {count}: {rowSquares}")

    def showLocation(self):
        print(f"ROW {self.row}: Square: {self.square} ({self[self.row][self.square].name}) ")

    def getLocation(self):
        return self.row, self.square

    def setLocation(self, row, square):
        self.row = row
        self.square = square

    def getSquareInfo(self):
        print(self[self.row][self.square].info)

    def getSquareChest(self):
        return self[self.row][self.square].chest

    def moveForward(self):
        if (self.square + 1) <= 4:
            self.square += 1
        else:
            print("You can't go any further forwards, there's a wall in your way...")

    def moveBackward(self):
        if (self.square - 1) >= 0:
            self.square -= 1
        else:
            print("You can't go any further backward, there's a wall in your way")
    
    def moveUp(self):
        if (self.row - 1) >= 0:
            self.row -= 1
        else:
            print("You can't go any further left, there's a wall in your way...")

    def moveDown(self):
        if (self.row + 1) <= 4:
            self.row += 1
        else:
            print("You can't go any further right, there's a wall in your way...")
        
    