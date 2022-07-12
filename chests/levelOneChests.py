import chest, game_objects.weapons as weapons

class CaptainChest(chest.Chest):
    def __init__(self):
        super().__init__()
        self.name = "Captain's Chest"
        self.introString = "\nYou proceed to the wreckage and make your way into the captain's quarters of the ship; there you find a chest with something shining inside."
        self.inventory.extend([weapons.Sword(), weapons.Dagger()])

    def intro(self):
        print(self.introString)
        return input("Would you like to open it? (y/n)\n")