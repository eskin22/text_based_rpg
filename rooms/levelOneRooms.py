import room, squares

class SunkenShip(room.Room):
    def __init__(self):
        super().__init__()
        self.extend([[squares.Square(10), squares.Square(11), squares.EnemySquare(12), squares.Square(13), squares.Square(14)]])
        self.extend([[squares.Square(20), squares.Square(21), squares.Square(22), squares.Square(23), squares.Square(24)]])
        self.extend([[squares.Square(30), squares.Square(31), squares.Square(32), squares.Square(33), squares.CaptainChestSquare(34)]])
        self.extend([[squares.StartingSquare(40), squares.Square(41), squares.Square(42), squares.Square(43), squares.Square(44)]])
        self.extend([[squares.Square(50), squares.Square(51), squares.Square(52), squares.Square(53), squares.Square(54)]])

        self.row, self.square = 2, 4