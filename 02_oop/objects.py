# objects.py
# Author: Moin Uddin

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def info(self):
        print(f"Name: {self.name} | Age: {self.age} | Course: {self.course}")

s1 = Student("Moin", 19, "BSCS")
s2 = Student("Ali", 20, "BBA")
s3 = Student("Sara", 18, "BS Math")

s1.info()
s2.info()
s3.info()