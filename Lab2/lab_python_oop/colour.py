class Colour():
    def __init__(self):
        self.Colour = None

    @property
    def colour(self):
        return self.Colour

    @colour.setter
    def colour(self, value):
        self.Colour = value