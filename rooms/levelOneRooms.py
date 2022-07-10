import game_objects.chests

class Square():
    def __init__(self, id=None):
        self.name = None
        self.id = id
        
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
    def __init__(self, chest):
        super().__init__(self, chest)
        self.name = "Chest Square"
        self.chest = chest

roomRow1 = [Square(), Square(), Square(), Square(), Square()]
roomRow2 = [Square(), Square(), Square(), Square(), Square()]
roomRow3 = [Square(), Square(), Square(), ChestSquare(game_objects.chests.LevelOneChest), Square()]
roomRow4 = [Square(), Square(), Square(), Square(), Square()]
roomRow5 = [Square(), Square(), Square(), Square(), Square()]

room = [roomRow1, roomRow2, roomRow3, roomRow4, roomRow5]

