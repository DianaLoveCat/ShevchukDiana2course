from .figure import Figure
from .colour import Colour
import math

class Circle(Figure):
    def __init__(self, radius, colour = Colour):
        self.radius = radius
        self.colour = colour
        self.Name = "Круг"

    def area(self):
        return math.pi * self.radius**2

    def __repr__(self):
        return f"{self.Name}: радиус {self.radius}, цвет {self.colour}, площадь {round(self.area(),3)}"