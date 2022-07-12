import game_objects.objects as objects

class WoodenSword(objects.Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Wooden Sword"
        self.damage = 10
        self.value = 3
        self.desc = "A small wooden sword"

class Dagger(objects.Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Dagger"
        self.damage = 12
        self.value = 5
        self.desc = "A small iron dagger"

class Sword(objects.Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Sword"
        self.damage = 20
        self.value = 12
        self.desc = "A steel sword"

class Mace(objects.Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Mace"
        self.damage = 23
        self.value = 15
        self.desc = "A steel mace"

class Greatsword(objects.Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Greatsword"
        self.damage = 27
        self.value = 20
        self.desc = "A mighty steel greatsword"

class CrabSword(objects.Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Crab Sword"
        self.damage = 9 
        self.value = 15
        self.desc = "A blade forged from the claw of the mighty Crabosaur"
