import chest, game_objects.weapons as weapons

class TestChestA(chest.Chest):
    def __init__(self):
        super().__init__()
        self.name = "Test Chest"
        self.introString = "\nYou found the test chest!"

        self.inventory.extend({weapons.Mace(), weapons.WoodenSword(), weapons.CrabSword()})

