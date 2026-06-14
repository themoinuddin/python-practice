# inheritance.py
# Author: Moin Uddin

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, "makes a sound")

class Dog(Animal):
    def speak(self):
        print(self.name, "says: Woof!")

class Cat(Animal):
    def speak(self):
        print(self.name, "says: Meow!")

a = Animal("Animal")
d = Dog("Bruno")
c = Cat("Kitty")

a.speak()
d.speak()
c.speak()