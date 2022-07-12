
import game_objects.objects as objects, game_objects.weapons as weapons, game_objects.key_items as key_items, game_objects.food as food

class Inventory(list):
    def __init__(self):
        super().__init__()
        self.name = None
        self.ind = None

        self.weaponsList = []
        self.foodList = []
        self.keyItemsList = []
        self.miscItemsList = []

        self.extend([self.weaponsList, self.foodList, self.keyItemsList, self.miscItemsList])

    def addItems(self, *args):
        for item in [*args]:
            if isinstance(item, objects.Weapon):
                self.weaponsList.append(item)
            elif isinstance(item, objects.KeyItem):
                self.keyItemsList.append(item)
            elif isinstance(item, objects.Food):
                self.foodList.append(item)
            elif isinstance(item, objects.MiscItem):
                self.miscItemsList.append(item)
 
    def removeItems(self, *args):
        for item in [*args]:
            if isinstance(item, objects.Weapon):
                self.weaponsList.remove(item)
            elif isinstance(item, objects.KeyItem):
                self.keyItemsList.remove(item)
            elif isinstance(item, objects.Food):
                self.foodList.remove(item)
            elif isinstance(item, objects.MiscItem):
                self.miscItemsList.remove(item)

    def listToString(self, list):
        string = "["
        for i in list:
            string += i.name

            if list.index(i) <= (len(list)-2):
                string += ", "
        
        string += "]"

    def getInventory(self):
        print(f"WEAPONS: {self.listToString(self.weaponsList)} \nFOOD: {self.listToString(self.foodList)} \nKEY ITEMS: {self.listToString(self.keyItemsList)} \nMISC: {self.listToString(self.miscItemsList)}")
        # Broken 
        
    def viewInventory(self):
        running = True
        while running == True:
            self.inventoryMenu()
            menuView = input("Select a category with the view command ($view) \n").lower()
            categoryName = menuView[6:]
            
            if menuView.startswith("$view "):
                if categoryName == "weapons":
                    self.displayCategory(categoryName, self.weaponsList)
                elif categoryName == "food":
                    self.displayCategory(categoryName, self.foodList)
                elif categoryName == "key items":
                    self.displayCategory(categoryName, self.keyItemsList)
                elif categoryName == "misc items":
                    self.displayCategory(categoryName, self.miscItemsList)
                else:
                    print("ERROR: Invalid category name. When selecting category, use this format: $view category name")
            elif menuView.startswith("$back"):
                break
            else:
                print("ERROR: Invalid  input, please try again. ")

    def displayCategory(self, categoryName, categoryList):
        running = True
        while running == True:
            global count
            count = 0
            print("\n------------------------------------------------------------------------------------------")
            print("INVENTORY")
            print("------------------------------------------------------------------------------------------")
            print("{:<40}".format("     - " + categoryName.upper()))
            print("------------------------------------------------------------------------------------------")
            print("{:>8}{:^75}{:>1}".format("NAME", "VALUE", "DAMAGE"))
            print("------------------------------------------------------------------------------------------")


            if categoryName == "weapons":
                for object in categoryList:
                    count += 1
                    object.chestID = count
                    spacingValue = (35-len(object.name))
                    spacingString = ""
                    for i in range(spacingValue):
                        spacingString += " "
                    print("{:>8}{}{}{:>4}{:>42}".format(str(count) + ". ", object.name, spacingString, object.value, object.damage))
            elif categoryName in ["food", "key items", "misc items"]:
                for object in categoryList:
                    count += 1
                    object.chestID = count
                    spacingValue = (35-len(object.name))
                    spacingString = ""
                    for i in range(spacingValue):
                        spacingString += " "
                    print("{:>8}{}{}{:>4}{:>42}".format(str(count) + ". ", object.name, spacingString, object.value, "N/A"))
            else:
                print("There's nothing to see here")


            print("------------------------------------------------------------------------------------------")
            print("{:^95}".format("BACK ($back) "))
            print("------------------------------------------------------------------------------------------")

            menu = input("What would you like to do? TIP: Use command $equip to equip weapons, or $drop to drop them\n").lower()

            if menu.startswith("$equip"):
                pass
            elif menu.startswith("$drop"):
                pass
            elif menu.startswith("$back"):
                break
            else:
                print("ERROR: Invalid input. Please try again.")

    
    def inventoryMenu(self):
        print("\n--------------------------------------------------")
        print("{:<40}".format("INVENTORY"))
        print("--------------------------------------------------")

        print("{:<40}".format("     - WEAPONS"))
        print("{:<40}".format("     - FOOD"))
        print("{:<40}".format("     - KEY ITEMS"))
        print("{:<40}".format("     - MISC"))

        print("--------------------------------------------------")
        print("{:^55}".format("BACK ($back) "))
        print("--------------------------------------------------")


                




