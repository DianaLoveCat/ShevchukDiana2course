from .rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side, colour):
        self.side = side
        self.colour = colour
        self.Name = "Квадрат"

    def figureName(self):
        return self.Name

    def area(self):
        return self.side**2

    def __repr__(self):
        return f"{self.Name}: длина стороны {self.side},цвет {self.colour},площадь {self.area()}"