import game_objects.objects as objects

class GlowingAmber(objects.KeyItem):
    def __init__(self):
        super().__init__()
        self.name = "Glowing Amber"
        self.value = 100
        self.desc = "A mysterious glowing nugget of amber that seems to have magical properties"
        self.createObjectID()
        