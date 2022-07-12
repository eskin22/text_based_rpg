import enemy, game_objects.weapons as weapons

class GiantCrab(enemy.Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.name = name 
        self.hp = 60
        self.attackPower = 9
        self.speed = 35
        self.item = weapons.CrabSword()