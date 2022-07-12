import game_objects.bank as bank, game_objects.objects as objects, game_objects.weapons as weapons, chest, inventory, room

class Player():
    def __init__(self, name):
        self.name = name
        self.hp = None
        self.magicAffinity = None
        self.strength = None
        self.speed = None
        self.bank = bank.Bank(250)
        self.attackPower = None
        self.weapon = None
        self.inventory = inventory.Inventory()
        self.location = None

        print(f"\nYou selected the {self.className} class!")

    def attack(self, enemy):
        enemy.hp -= self.attackPower
        if enemy.hp <= 0:
            enemy.hp = 0
        print(f"{self.name} attacks {enemy.name} and does {self.attackPower} damage! {enemy.name} has {enemy.hp} HP remaining.")
        if enemy.hp <= 0:
            print("\n------------------------------------------------------------------------------------------")
            print("{:^90}".format("The " + enemy.name + " has been slain!"))
            print("------------------------------------------------------------------------------------------")

    def addCoins(self, coins):
        self.bank.addCoins(coins)
    
    def removeCoins(self, value):
        self.bank.removeCoins(value)

    def getBankValue(self):
        return self.bank.value

    def displayBankValue(self):
        self.bank.showValue()

    def displayInventory(self):
        self.inventory.viewInventory()

    def takeItems(self, inv, *args):
        for item in [*args]:
            self.inventory.addItems(item)
            inv.removeItems(item)
            print(f"\n{item.name} added to inventory. ")

    def findWeapon(self, weapon):
        menuFindWeapon = input(f"You found a {weapon.name}! Would you like to equip it now? (y/n)").lower()
        
        if menuFindWeapon == "y":
            self.equipWeapon(weapon)
        elif menuFindWeapon == "n":
            self.inventory.addItems(weapon)
        else:
            print("ERROR: Invalid input. Please try again.")
        
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

    def showLocation(self):
        self.location.showLocation()

    def setLocation(self, row, square):
        self.location.setLocation(row, square)

    def inspect(self):
        self.location.getSquareInfo()

    def interact(self):
        object = self.location.getSquareObject()

        if isinstance(object, chest.Chest):
            object.open(self)
        elif isinstance(object, objects.Weapon):
            self.findWeapon(object)
        elif isinstance(object, objects.KeyItem):
            pass
   
    def getPlayer(self):
        return self


        
        



        
    


