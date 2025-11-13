from .figure import GeomFigure
from .colour import Colour

class Rectangle(GeomFigure):
    def __init__(self, width, height, colour = Colour):
        self.width = width
        self.height = height
        self.colour = colour
        self.Name = "Прямоугольник"

    def figureName(self):
        return self.Name

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return f"{self.Name}: ширина {self.width},высота {self.height},цвет {self.colour},площадь {self.area()}"