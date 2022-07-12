import enemy, game_objects.weapons as weapons

class Wolf(enemy.Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Wolf"
        self.hp = 20
        self.attackPower = 5
        self.speed = 60

class Ogre(enemy.Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Ogre"
        self.hp = 200
        self.attackPower = 20
        self.speed = 25

class GiantCrab(enemy.Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Giant Crab"
        self.hp = 60
        self.attackPower = 9
        self.speed = 35
        self.item = weapons.CrabSword()