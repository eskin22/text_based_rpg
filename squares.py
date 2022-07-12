import game_objects.objects, game_objects.key_items, game_objects.weapons, random
import chests.testChests, chests.levelOneChests

class Square():
    def __init__(self, id=None):
        self.name = None
        self.id = id
        self.info = "Nothing to see here. "
        self.object = None

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

class CoinSquare(Square):
    def __init__(self, id=None):
        super().__init__(id)
        self.name = "Coin Square"
        self.coin = random.randint(0,9)
        self.info = "There are coins here! "

class ChestSquare(Square):
    def __init__(self, id=None):
        super().__init__(id)
        self.name = "Chest Square"
        self.info = "There is a chest here! "

class SwordSquare(ItemSquare):
    def __init__(self, id=None):
        super().__init__(id)
        self.object = game_objects.weapons.Sword()

class TestChestSquare(ChestSquare):
    def __init__(self, id=None):
        super().__init__(id)
        self.object = chests.testChests.TestChestA()

class CaptainChestSquare(ChestSquare):
    def __init__(self, id=None):
        super().__init__(id)
        self.object = chests.levelOneChests.CaptainChest()

