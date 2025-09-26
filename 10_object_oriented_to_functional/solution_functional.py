from typing import Callable
from math import pi


ShapeFn = Callable[..., float]
Shape = tuple[float, float, ShapeFn, ShapeFn]
ShapeOneDegree = tuple[float, ShapeFn, ShapeFn]
ShapeCalculator = tuple[ShapeFn, ShapeFn]


def rectangle(width: float, height: float) -> Shape:
    def area():
        return width * height

    def perimeter():
        return 2 * (width + height)

    return width, height, area, perimeter 

def square(side_length: float) -> Shape:
    def area():
        return side_length**2

    def perimeter():
        return 4 * (side_length)

    return side_length, side_length, area, perimeter 

def circle(radius: float) -> Shape:
    def area():
        return pi * radius**2

    def perimeter():
        return 2 * pi * radius

    return radius, radius, area, perimeter 


def shape_calculator(shapes: list[Shape]) -> ShapeCalculator:

    def total_area():
        return sum([shape[2]() for shape in shapes])

    def total_perimeter():
        return sum([shape[3]() for shape in shapes])

    return total_area, total_perimeter



def main() -> None:
    shapes: list[Shape] = [rectangle(4, 5), square(3), circle(2)]
    calculator = shape_calculator(shapes)
    print("Total Area:", calculator[0]())
    print("Total Perimeter:", calculator[1]())


if __name__ == "__main__":
    main()

