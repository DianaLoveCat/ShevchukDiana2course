from sys import exit

import numpy as np

from lab_python_oop.circle import Circle
from lab_python_oop.color import Color
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.square import Square


def main() -> int:
    rectangle = Rectangle(3, 3, Color(0, 0, 255))
    circle = Circle(3, Color(0, 255, 0))
    square = Square(3, Color(255, 0, 0))

    print(rectangle, circle, square, sep='\n\n', end='\n\n')

    print(f"Rectangle area - {rectangle.calculate_area()}")
    print(f"Circle area - {circle.calculate_area()}")
    print(f"Square area - {square.calculate_area()}", end='\n\n')

    data = np.array([1, 1, 3, 3, 2, 4, 5, 2, 3, 4])
    print(data.std(ddof=1))

    return 0


if __name__ == "__main__":
    exit(main())