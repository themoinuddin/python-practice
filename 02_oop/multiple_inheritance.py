# multiple_inheritance.py
# Author: Moin Uddin

class Father:
    def money(self):
        print("Father: I have money")

class Mother:
    def intelligence(self):
        print("Mother: I have intelligence")

class Child(Father, Mother):
    def skills(self):
        print("Child: I have both!")

c = Child()
c.money()
c.intelligence()
c.skills()