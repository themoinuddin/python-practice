# Author: Moin Uddin
# Area Calculator
# Example: Circle r=7 → Area=153.94

import math

def circle_area(r):
    return math.pi * r ** 2

def rectangle_area(l, w):
    return l * w

def triangle_area(b, h):
    return 0.5 * b * h

print("Area Calculator")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = int(input("Choose shape (1/2/3): "))

if choice == 1:
    r = float(input("Enter radius: "))
    print(f"Area of Circle: {circle_area(r):.2f}")
elif choice == 2:
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    print(f"Area of Rectangle: {rectangle_area(l, w):.2f}")
elif choice == 3:
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    print(f"Area of Triangle: {triangle_area(b, h):.2f}")
else:
    print("Invalid choice!")