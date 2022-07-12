
class Object():
    def __init__(self):
        self.name = None
        self.value = None
        self.desc = None
        self.chestID = None

class Coins(Object):
    def __init__(self, value):
        super().__init__()
        self.name = "coins"
        self.value = value
        self.desc = "A collection of gold coins"

class Weapon(Object):
    def __init__(self):
        self.damage = None

class KeyItem(Object):
    def __init__(self):
        super().__init__()

class Food(Object):
    def __init__(self):
        super().__init__()
        self.hp = None

class MiscItem(Object):
    def __init__(self):
        super().__init__()
