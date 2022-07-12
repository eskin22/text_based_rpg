import game_objects.objects as objects

class Torch(objects.MiscItem):
    def __init__(self):
        super().__init__()
        self.name = "Torch"
        self.value = 5
        self.desc = "A torch you can hold up to light the way. "
        self.createObjectID()

class ChildsToy(objects.MiscItem):
    def __init__(self):
        super().__init__()
        self.name = "Child's Toy"
        self.value = 8
        self.desc = "A small child's play-thing. "
        self.createObjectID()

class RuinedArtwork(objects.MiscItem):
    def __init__(self):
        super().__init__()
        self.name = "Ruined Artwork"
        self.value = 2
        self.desc = "A trashed peice of artwork, maybe it was beautiful once. "
        self.createObjectID()