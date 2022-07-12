import player, game_objects.bank as bank

class Tester(player.Player):
    def __init__(self, name):
        self.className = "Tester"
        super().__init__(name)
        self.name = name
        self.hp = 1000
        self.magicAffinity = 50
        self.strength = 50
        self.speed = 50
        self.bank = bank.Bank(500)
        self.attackPower = ((1+(self.strength/100))*5)
        self.weapon = None