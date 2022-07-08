import game_objects.weapons

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

    def open(self):
        print(f"------------------------------------------------------------------")
        print(f"                            {self.name.upper()}")
        print(f"------------------------------------------------------------------")
        print("ITEM                        VALUE                        DAMAGE\n")
        try:
            for item in self.inventory:
                spacingString = ""
                spacingValue = (30-(len(item.name)))
                for j in range(spacingValue):
                    spacingString += " "
                if isinstance(item, game_objects.weapons.Weapon):
                    print(f"{item.name}{spacingString}{item.value}                            {item.damage}")
                else:
                    print(f"{item.name}{spacingString}{item.value}")
        except:
            print()
        print(f"\n------------------------------------------------------------------\n")