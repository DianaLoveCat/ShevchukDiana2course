from math import pi

from .color import Color
from .figure import Figure


class Circle(Figure):
    def __init__(self, radius: float=0., color: Color | None=None):
        super().__init__(color)

        self.radius = radius
        self.object_name = "Circle"

    def __repr__(self) -> str:
        return f"{self.object_name}:\n  radius - {self.radius}\n  color - {self.color}"

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float):
        self._radius = value if value >= 0 else 0

    def calculate_area(self) -> float:
        return pi * self.radius ** 2