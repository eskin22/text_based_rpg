import enemy

class Ogre(enemy.Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.hp = 200
        self.attackPower = 20
        self.speed = 25