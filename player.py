from unicodedata import name
import game_objects

class Player():
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attackPower = 5
        self.coin = game_objects.Coinpurse(50)

    def attack(self, enemy, attack):
        enemy.hp -= attack
        print(f"{self.name} attacks {enemy.name} and does {attack} damage!")
    
    def interact(self, object):
        pass

class Warrior(Player):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.hp = 110
        self.attackPower = 8
        self.coin = game_objects.Coinpurse(30)
        
        



        
    


