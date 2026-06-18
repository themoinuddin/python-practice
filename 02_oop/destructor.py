# destructor.py
# Author: Moin Uddin

class Student:
    def __init__(self, name):
        self.name = name
        print(f"Student {self.name} created")

    def __del__(self):
        print(f"Student {self.name} deleted")

s1 = Student("Moin")
s2 = Student("Ali")

del s1
print("Program ending...")