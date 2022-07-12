import game_objects.objects as objects, game_objects.weapons as weapons

class Chest():
    def __init__(self, name):
        self.name = name
        self.introString = None
        self.inventory = []

    def addItems(self, *items):
        for item in items:
            self.inventory.append(item)

    def removeItems(self, *items):
        for item in items:
            self.inventory.remove(item)

    def open(self, player):
        running = True
        count = 0 
        while running == True:
            spacingString1 = ""
            spacingValue1 = (38-(len(self.name)))

            for a in range(spacingValue1):
                spacingString1 += " "

            print(f"------------------------------------------------------------------")
            print(f"{spacingString1}{self.name.upper()}")
            print(f"------------------------------------------------------------------")
            print("ITEM                        VALUE                        DAMAGE\n")
            for item in self.inventory:
                count += 1
                item.chestID = count
                spacingString2 = ""
                spacingString3 = ""
                spacingValue2 = (27-(len(item.name)))
                spacingValue3 = (29-(len(str(item.value))))

                for j in range(spacingValue2):
                    spacingString2 += " "
                    
                for k in range(spacingValue3):
                    spacingString3 += " "

                if isinstance(item, objects.Weapon):
                    print(f"{count}. {item.name}{spacingString2}{item.value}{spacingString3}{item.damage}")
                else:
                    print(f"{count}. {item.name}{spacingString2}{item.value}")
            print("------------------------------------------------------------------")
            print("                            BACK ($back)                                   ")
            print("------------------------------------------------------------------")

            menuChest = input("\n            TIP: Use command $take to take items \n")
            if menuChest == "$back":
                running = False
            elif menuChest.startswith("$take"):
                menuChest = int(menuChest[6:])
                for item in self.inventory:
                    if item.chestID == menuChest:
                        player.takeItems(self, item)

class TestChest(Chest):
    def __init__(self, name):
        super().__init__(name)
        self.name = "Test Chest"
        self.introString = "\nYou found the test chest!"
        self.inventory.extend({weapons.Mace(), weapons.WoodenSword()})


class CaptainChest(Chest):
    def __init__(self, name=None):
        super().__init__(name)
        self.name = "Captain's Chest"
        self.introString = "\nYou proceed to the wreckage and make your way into the captain's quarters of the ship; there you find a chest with something shining inside."
        self.inventory.extend([weapons.Sword(), weapons.Dagger()])

    def intro(self):
        print(self.introString)
        return input("Would you like to open it? (y/n)\n")