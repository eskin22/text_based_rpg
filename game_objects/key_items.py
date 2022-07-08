class KeyItem():
    def __init__(self):
        self.name = None
        self.desc = None

class GlowingAmber(KeyItem):
    def __init__(self):
        super().__init__()
        self.name = "Glowing Amber"
        self.desc = "A mysterious glowing nugget of amber that seems to have magical properties"