class Coinpurse():
    def __init__(self, value):
        self.value = value

    def getValue(self): 
        return self.value

    def addCoin(self, coin):
        self.value += coin

    def removeCoin(self, coin):
        self.value -= coin
