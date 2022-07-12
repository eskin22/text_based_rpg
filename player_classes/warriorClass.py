import player, game_objects.bank as bank

class Warrior(player.Player):
    def __init__(self, name):
        self.className = "Warrior"
        super().__init__(name)
        self.name = name
        self.hp = 120
        self.magicAffinity = 30
        self.strength = 50
        self.speed = 55
        self.bank = bank.Bank(250)
        self.attackPower = ((1+(self.strength/100))*5)