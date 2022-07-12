import game_objects.objects as objects

class Cake(objects.Food):
    def __init__(self):
        super().__init__()
        self.name = "Cake"
        self.value = 8
        self.desc = "A delicious frosted cake for you to devour. "
        self.hp = 10
        self.createObjectID()

class CheeseWedge(objects.Food):
    def __init__(self):
        super().__init__()
        self.name = "Cheese Wedge"
        self.value = 3
        self.desc =  "A thick wedge of cheese to be eaten. "
        self.hp = 3
        self.createObjectID()

class MuttonChop(objects.Food):
    def __init__(self):
        super().__init__()
        self.name = "Mutton Chop"
        self.value = 12
        self.desc = "A steaming juicy mutton chop to fil your belly. "
        self.hp = 15
        self.createObjectID()
