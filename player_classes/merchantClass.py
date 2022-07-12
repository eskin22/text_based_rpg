import player, game_objects.bank as bank

class Merchant(player.Player):
    def __init__(self, name):
        self.className = "Merchant"
        super().__init__(name)
        self.name = name
        self.hp = 110
        self.magicAffinity = 30
        self.strength = 40
        self.speed = 60
        self.bank = bank.Bank(500)
        self.attackPower = ((1+(self.strength/100))*5)