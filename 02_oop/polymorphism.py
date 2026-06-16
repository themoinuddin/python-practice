# polymorphism.py
# Author: Moin Uddin

class Shape:
    def area(self):
        print("Area unknown")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"Circle area: {3.14 * self.radius * self.radius}")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print(f"Rectangle area: {self.width * self.height}")

shapes = [Circle(5), Rectangle(4, 6)]

for shape in shapes:
    shape.area()