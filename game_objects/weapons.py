class Weapon():
    def __init__(self):
        self.name = None
        self.damage = None
        self.value = None
        self.desc = None

class WoodenSword(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Wooden Sword"
        self.damage = 10
        self.value = 3
        self.desc = "A small wooden sword"

class Dagger(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Dagger"
        self.damage = 12
        self.value = 5
        self.desc = "A small iron dagger"

class Sword(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Sword"
        self.damage = 20
        self.value = 12
        self.desc = "A steel sword"

class Mace(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Mace"
        self.damage = 23
        self.value = 15
        self.desc = "A steel mace"

class Greatsword(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Greatsword"
        self.damage = 27
        self.value = 20
        self.desc = "A mighty steel greatsword"

class CrabSword(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Crab Sword"
        self.damage = 9 
        self.value = 15
        self.desc = "A blade forged from the claw of the mighty Crabosaur"
