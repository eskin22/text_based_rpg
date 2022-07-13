

import random, sys, enemy, game_objects.bank as bank, game_objects.objects as objects, game_objects.weapons as weapons, chest, inventory, room

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

    #methods for player bank

    def addCoins(self, coins):
        self.bank.addCoins(coins)
    
    def removeCoins(self, value):
        self.bank.removeCoins(value)

    def getBankValue(self):
        return self.bank.value

    def displayBankValue(self):
        self.bank.showValue()
    
    #methods for player inventory

    def displayInventory(self):
        self.inventory.viewInventory()
    
    def addItems(self, *args):
        for item in [*args]:
            self.inventory.addItems(item)
            print(f"{item.name} added to inventory.")

    def takeItems(self, inv, *args):
        for item in [*args]:
            self.inventory.addItems(item)
            inv.removeItems(item)
            print(f"\n{item.name} added to inventory. ")

    def equipWeapon(self, weapon):
        self.weapon = weapon
        self.attackPower = ((1+(self.strength/100))*weapon.damage)
        print(f"\n{weapon.name} equipped successfully. ")

    def findWeapon(self, weapon):
        menuFindWeapon = input(f"You found a {weapon.name}! Would you like to equip it now? (y/n)\n").lower()
        
        if menuFindWeapon == "y":
            self.equipWeapon(weapon)
        elif menuFindWeapon == "n":
            self.inventory.addItems(weapon)
            print(f"The {weapon.name} was added to your inventory.")
        else:
            print("ERROR: Invalid input. Please try again.")

    def findChest(self, chest):
        menuFindChest = input(f"You found a chest! Would you like to open it? (y/n)\n").lower()
        
        if menuFindChest == "y":
            chest.open(self)
        elif menuFindChest == "n":
            print("You chose not search the chest. ")
        else:
            print("ERROR: Invalid input. Please try again.")

    def findObject(self, object):
        menuFindObject = input(f"You found a {object.name}! Would you like to add it to your inventory? (y/n)\n").lower()
        
        if menuFindObject == "y":
            self.addItems(object)
        elif menuFindObject == "n":
            print(f"You chose not to pick up the {object.name}.")
        else:
            print("ERROR: Invalid input. Please try again.")

    #methods for player navigation

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
            self.findChest(object)
        elif isinstance(object, enemy.Enemy):
            self.encounter(object)
        elif isinstance(object, objects.Weapon):
            self.findWeapon(object)
        elif isinstance(object, objects.KeyItem):
            self.findObject(object)
        elif isinstance(object, objects.MiscItem):
            self.findObject(object)
        else:
            print("ERROR: An error has occurred. ")

    def explore(self):
        running = True

        while running == True:
            menuExplore = input("\nWhat would you like to do? TIP: use the $help command to get a list of action commands ")
        
            if menuExplore.startswith("$go"):
                selection = menuExplore[3:]
                if selection.startswith(" f"):
                    self.moveForward()
                elif selection.startswith(" b"):
                    self.moveBackward()
                elif selection.startswith(" r"):
                    self.moveDown()
                elif selection.startswith(" l"):
                    self.moveUp()
                else:
                    print("ERROR: Invalid input. Please try again. ")

            elif menuExplore.startswith("$ins"):
                self.inspect()

            elif menuExplore.startswith("$int"):
                self.interact()
            
            else:
                print("ERROR: Invalid input. Please try again. ")

    #methods for player combat

    def attack(self, enemy):
        enemy.hp -= self.attackPower
        if enemy.hp <= 0:
            enemy.hp = 0
        print(f"{self.name} attacks {enemy.name} and does {self.attackPower} damage! {enemy.name} has {enemy.hp} HP remaining.")
        if enemy.hp <= 0:
            print("\n------------------------------------------------------------------------------------------")
            print("{:^90}".format("The " + enemy.name + " has been slain!"))
            print("------------------------------------------------------------------------------------------")

    def battle(self, enemy):
        print()
        while ((self.hp > 0) and (enemy.hp > 0)):
            if self.speed == enemy.speed:
                if (random.randint(0,9)<=5):
                    self.attack(enemy)
                    if enemy.hp > 0:
                        enemy.attack(self)
                else:
                    enemy.attack(self)
                    if self.hp > 0:
                        self.attack(enemy)
            elif self.speed > enemy.speed:
                self.attack(enemy)
                if enemy.hp > 0:
                    enemy.attack(self)
            else:
                enemy.attack(self)
                if self.hp > 0:
                    self.attack(enemy)
                
            if enemy.hp <= 0:
                enemy.isDead = True
                break
            
            if self.hp <= 0:
                sys.exit()
    
    def encounter(self, enemy):
        print("------------------------------------------------------------------------------------------")
        print("{:>8}{:^68}{:>5}".format("ENEMY: " + enemy.name.upper(), "HP: " + str(enemy.hp), "DAMAGE: " + str(enemy.attackPower)))
        print("------------------------------------------------------------------------------------------")

        menuAttack = input(f"\nWhat would you like to do? ($attack/$flee) \n").lower()
        if menuAttack == "$attack":
            self.battle(enemy)
        elif menuAttack == "$flee":
            randNum = random.randint(0,9)
            if (randNum <= 7):
                print("\nYou escaped safely. \n")
            elif (randNum > 7):
                print(f"\nYou try to escape, but the {enemy.name} has cornered you! \n")
                self.battle(enemy)
        else:
            print("\nError: Invalid input. Please try again. \n")
        



        
    


