
class Square():
    def __init__(self):
        self.name = None
        
class ItemSquare(Square):
    def __init__(self):
        super().__init__()
        self.name = "Item Square"
        self.item = None

class EnemySquare(Square):
    def __init__(self):
        super().__init__()
        self.name = "Enemy Square"
        self.enemy = None

class ChestSquare(Square):
    def __init__(self):
        super().__init__()
        self.name = "Chest Square"
        self.chest = None