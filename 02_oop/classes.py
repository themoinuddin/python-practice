# classes.py
# Author: Moin Uddin

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hi, I am", self.name, "and I am", self.age, "years old.")

s1 = Student("Moin", 19)
s1.greet()