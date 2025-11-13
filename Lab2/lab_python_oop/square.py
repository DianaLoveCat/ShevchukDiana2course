from .rectangle import Rectangle
from .colour import Colour

class Square(Rectangle):
    def __init__(self, side, colour = Colour):
        super().__init__(side, side, colour)
        self.Name = "Квадрат"

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return f"{self.Name}: длина стороны {self.width},цвет {self.colour},площадь {self.area()}"