# encapsulation.py
# Author: Moin Uddin

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.__balance}")

    def get_balance(self):
        print(f"Balance: {self.__balance}")

acc = BankAccount("Moin", 1000)
acc.get_balance()
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(2000)