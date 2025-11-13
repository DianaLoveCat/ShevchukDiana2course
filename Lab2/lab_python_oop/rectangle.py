from .figure import Figure
from .colour import Colour

class Rectangle(Figure):
    def __init__(self, width, height, colour = Colour):
        self.width = width
        self.height = height
        self.colour = colour
        self.Name = "Прямоугольник"

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return f"{self.Name}: ширина {self.width},высота {self.height},цвет {self.colour},площадь {self.area()}"