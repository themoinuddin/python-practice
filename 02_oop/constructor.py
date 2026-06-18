# constructor.py
# Author: Moin Uddin

class Student:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age
        print(f"Student created: {self.name}")

    def info(self):
        print(f"Name: {self.name} | Age: {self.age}")

s1 = Student()
s1.info()

s2 = Student("Moin", 19)
s2.info()

s3 = Student("Ali", 20)
s3.info()