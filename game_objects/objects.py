import random

class Object():
    def __init__(self):
        self.name = None
        self.value = None
        self.desc = None
        self.chestID = None
        self.uniqueID = random.randint(10000000, 99999999)
        self.objectID = None

    def createObjectID(self):
        if isinstance(self, Weapon):
            self.objectID = f"Weapon: [{self.name}]"
        elif isinstance(self, Food):
            self.objectID = f"Food: [{self.name}]"
        elif isinstance(self, KeyItem):
            self.objectID = f"KeyItem: [{self.name}]"
        elif isinstance(self, MiscItem):
            self.objectID = f"MiscItem: [{self.name}]"
        else:
            print("I don't know what kind of object this is")

class Coins(Object):
    def __init__(self, value):
        super().__init__()
        self.name = "coins"
        self.value = value
        self.desc = "A collection of gold coins"

class Weapon(Object):
    def __init__(self):
        super().__init__()
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

