import game_objects.objects as objects, game_objects.weapons as weapons, rooms

class Player():
    def __init__(self, name):
        self.name = name
        self.hp = None
        self.magicAffinity = None
        self.strength = None
        self.speed = None
        self.coin = objects.Coinpurse(250)
        self.attackPower = None
        self.weapon = None
        self.inventory = []
        self.location = None

        print(f"\nYou selected the {self.className} class!")

    def attack(self, enemy):
        enemy.hp -= self.attackPower
        if enemy.hp <= 0:
            enemy.hp = 0
        print(f"{self.name} attacks {enemy.name} and does {self.attackPower} damage! {enemy.name} has {enemy.hp} HP remaining.")
        if enemy.hp <= 0:
            print("\n------------------------------------------------------------------")
            print(f"                   The {enemy.name} has been slain!")
            print("------------------------------------------------------------------")

    def addCoin(self, coins):
        self.coin.addCoin(coins)

    def takeItems(self, inv, *args):
        for item in args:
            self.inventory.append(item)
            inv.removeItems(item)
            print(f"\n{item.name} added to inventory. \n")
        
    def equipWeapon(self, weapon):
        self.weapon = weapon
        self.attackPower = ((1+(self.strength/100))*weapon.damage)
        print(f"\n{weapon.name} equipped successfully. ")

    def moveUp(self):
        self.location.moveUp()

    def moveDown(self):
        self.location.moveDown()

    def moveForward(self):
        self.location.moveForward()

    def moveBackward(self):
        self.location.moveBackward()

    def getLocation(self):
        self.location.getLocation()
        
    def getPlayer(self):
        return self
    
    def interact(self, object):
        pass

class Warrior(Player):
    def __init__(self, name):
        self.className = "Warrior"
        super().__init__(name)
        self.name = name
        self.hp = 120
        self.magicAffinity = 30
        self.strength = 50
        self.speed = 55
        self.coin = objects.Coinpurse(250)
        self.attackPower = ((1+(self.strength/100))*5)

class Merchant(Player):
    def __init__(self, name):
        self.className = "Merchant"
        super().__init__(name)
        self.name = name
        self.hp = 110
        self.magicAffinity = 30
        self.strength = 40
        self.speed = 60
        self.coin = objects.Coinpurse(500)
        self.attackPower = ((1+(self.strength/100))*5)

class Mage(Player):
    def __init__(self, name):
        self.className = "Mage"
        super().__init__(name)
        self.name = name
        self.hp = 100
        self.magicAffinity = 70
        self.strength = 30
        self.speed = 45
        self.coin = objects.Coinpurse(350)
        self.attackPower = ((1+(self.strength/100))*5)

class Tester(Player):
    def __init__(self, name):
        self.className = "Tester"
        super().__init__(name)
        self.name = name
        self.hp = 1000
        self.magicAffinity = 50
        self.strength = 50
        self.speed = 50
        self.coin = objects.Coinpurse(500)
        self.attackPower = ((1+(self.strength/100))*5)
        self.weapon = None
        self.inventory = []

        
        



        
    


