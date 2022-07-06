import game_objects

class Player():
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.magicAffinity = 50
        self.strength = 50
        self.coin = game_objects.Coinpurse(250)

    def attack(self, enemy, attack):
        enemy.hp -= attack
        print(f"{self.name} attacks {enemy.name} and does {attack} damage!")

    def getPlayer(self):
        return self
    
    def interact(self, object):
        pass

class Warrior(Player):
    def __init__(self, name):
        super().__init__(name)
        self.className = "Warrior"
        self.name = name
        self.hp = 120
        self.magicAffinity = 30
        self.strength = 50
        self.coin = game_objects.Coinpurse(250)

        print(f"You selected the {self.className} class!")

class Merchant(Player):
    def __init__(self, name):
        super().__init__(name)
        self.className = "Merchant"
        self.name = name
        self.hp = 110
        self.magicAffinity = 30
        self.strength = 40
        self.coin = game_objects.Coinpurse(500)

        print(f"You selected the {self.className} class!")

class Mage(Player):
    def __init__(self, name):
        super().__init__(name)
        self.className = "Mage"
        self.name = name
        self.hp = 100
        self.magicAffinity = 70
        self.strength = 30
        self.coin = game_objects.Coinpurse(350)

        print(f"You selected the {self.className} class!")
        
        



        
    


