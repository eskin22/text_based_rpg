import game_objects.chests as chests

class Square():
    def __init__(self, id=None):
        self.name = None
        self.id = id
        self.info = "Nothing to see here. "

class StartingSquare(Square):
    def __init__(self, id=None):
        super().__init__(id)
        self.name = "Starting Square"
        
class ItemSquare(Square):
    def __init__(self, id=None):
        super().__init__(id)
        self.name = "Item Square"
        self.item = None
        self.info = "There is an item here! "

class EnemySquare(Square):
    def __init__(self, id=None):
        super().__init__(id)
        self.name = "Enemy Square"
        self.enemy = None
        self.info = "There is an enemy here! "

class ChestSquare(Square):
    def __init__(self, id=None):
        super().__init__(id)
        self.name = "Chest Square"
        self.chest = None
        self.info = "There is a chest here! "