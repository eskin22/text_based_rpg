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

    def getLocation(self):
        print(f"ROW {self.row}: Square: {self.square} ({self[self.row][self.square].name}) ")

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



class TestRoom(Room):
    def __init__(self):
        super().__init__()
        self.extend([[squares.Square(10), squares.Square(11), squares.EnemySquare(12), squares.Square(13), squares.Square(14)]])
        self.extend([[squares.Square(20), squares.Square(21), squares.Square(22), squares.Square(23), squares.Square(24)]])
        self.extend([[squares.StartingSquare(30), squares.Square(31), squares.Square(32), squares.ChestSquare(33), squares.ItemSquare(34)]])
        self.extend([[squares.Square(40), squares.Square(41), squares.Square(42), squares.Square(43), squares.Square(44)]])
        self.extend([[squares.Square(50), squares.Square(51), squares.Square(52), squares.Square(53), squares.Square(54)]])

        self.row, self.square = 2, 0
    