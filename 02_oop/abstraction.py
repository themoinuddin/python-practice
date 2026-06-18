# abstraction.py
# Author: Moin Uddin

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print(f"Area: {self.width * self.height}")

    def perimeter(self):
        print(f"Perimeter: {2 * (self.width + self.height)}")

r = Rectangle(5, 3)
r.area()
r.perimeter()