
class Coinpurse():
    def __init__(self, value):
        self.value = value

    def getValue(self): 
        return self.value

    def addCoin(self, coin):
        self.value += coin

    def removeCoin(self, coin):
        self.value -= coin

class Object():
    def __init__(self):
        self.name = None
        self.value = None
        self.desc = None

    
class Dildo(Object):
    def __init__(self):
        super().__init__()
        self.name = "Dildo"
        self.value = 100
        self.desc = "A thick 5 inch dildo"
