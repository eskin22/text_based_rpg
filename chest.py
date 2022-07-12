import game_objects.objects as objects, game_objects.weapons as weapons

class Chest():
    def __init__(self):
        self.name = None
        self.introString = None
        self.inventory = []

    def addItems(self, *objects):
        for i in objects:
            self.inventory.append(i)

    def removeItems(self, *objects):
        for i in objects:
            for j in self.inventory:
                if i.objectID == j.objectID:
                    self.inventory.remove(j)

    def viewInventory(self):
        output = []
        for i in self.inventory:
            output.append(i.name)

        print(output)

    def open(self, player):
        running = True
        while running == True:
            count = 0
            print("\n------------------------------------------------------------------------------------------")
            print("{:^90}".format(self.name.upper()))
            print("------------------------------------------------------------------------------------------")
            print("{:>8}{:^75}{:>1}".format("NAME", "VALUE", "DAMAGE"))
            print("------------------------------------------------------------------------------------------")

            self.inventory.sort(key=lambda x: x.name)

            for i in self.inventory:
                if isinstance(i, objects.Weapon):
                    count += 1
                    i.chestID = count
                    spacingValue = (35-len(i.name))
                    spacingString = ""
                    for j in range(spacingValue):
                        spacingString += " "
                    print("{:>8}{}{}{:>4}{:>42}".format(str(count) + ". ", i.name, spacingString, i.value, i.damage))

                elif isinstance(i, (objects.Food, objects.KeyItem, objects.MiscItem),):
                    count += 1
                    i.chestID = count
                    spacingValue = (35-len(i.name))
                    spacingString = ""
                    for j in range(spacingValue):
                        spacingString += " "
                    print("{:>8}{}{}{:>4}{:>42}".format(str(count) + ". ", i.name, spacingString, i.value, "N/A"))

                else:
                    print("\n{:^90}\n".format("CHEST EMPTY"))
            
            print("------------------------------------------------------------------------------------------")
            print("{:^90}".format("BACK ($back) "))
            print("------------------------------------------------------------------------------------------")

            print("{:^95}".format("TIP: Use command $take to take items \n"))
            menuChest = input()
            if menuChest == "$back":
                break
            elif menuChest.startswith("$take"):
                selection = int(menuChest[6:])
                for item in self.inventory:
                    if item.chestID == selection:
                        player.takeItems(self, item)
                        self.removeItems(item)
                        break
                    elif item.chestID != selection:
                        pass
                    else:
                        print("There has been an error")
            else:
                print("ERROR: Invalid input. Please try again.")