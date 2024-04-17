# Create an abstract class Shape with abstract methods calculate_area and calculate_perimeter.
# Create classes Circle (receives radius upon initialization) and Rectangle
# (receives height and width upon initialization) that implement those methods (returning the result).
# The fields of Circle and Rectangle should be private.
# Submit all the classes and your imports in the judge system

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        return None

    @abstractmethod
    def calculate_perimeter(self):
        return None


class Circle(Shape):
    def __init__(self, radius: int) -> None:
        self.__radius = radius

    def calculate_area(self) -> float:
        return (self.__radius ** 2) * pi

    def calculate_perimeter(self) -> float:
        return 2 * pi * self.__radius
    
    
class Rectangle(Shape):
    def __init__(self, height: int, width: int) -> None:
        self.__height = height
        self.__width = width

    def calculate_area(self) -> int:
        return self.__width * self.__height

    def calculate_perimeter(self) -> int:
        return 2 * (self.__height + self.__width)


# Test1:
circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())
# 78.53981633974483
# 31.41592653589793

# Test2:
rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
# 200
# 60
