import enemy

class Wolf(enemy.Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.hp = 20
        self.attackPower = 5
        self.speed = 60