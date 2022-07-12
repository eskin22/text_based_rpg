class Bank():
    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def showValue(self):
        print(f"Coins: {self.value} ")

    def addCoins(self, coins):
        self.value += coins.value

    def removeCoins(self, value):
        self.value -= value