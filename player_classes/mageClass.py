import player, game_objects.bank as bank

class Mage(player.Player):
    def __init__(self, name):
        self.className = "Mage"
        super().__init__(name)
        self.name = name
        self.hp = 100
        self.magicAffinity = 70
        self.strength = 30
        self.speed = 45
        self.bank = bank.Bank(350)
        self.attackPower = ((1+(self.strength/100))*5)