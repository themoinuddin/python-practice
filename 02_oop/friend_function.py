# friend_function.py
# Author: Moin Uddin

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private

    def get_balance(self):
        return self.__balance

def show_balance(account):
    # accessing private data via public method — Python style friend function
    print(f"{account.owner}'s balance: {account.get_balance()}")

def compare_balance(acc1, acc2):
    if acc1.get_balance() > acc2.get_balance():
        print(f"{acc1.owner} has more balance")
    else:
        print(f"{acc2.owner} has more balance")

acc1 = BankAccount("Moin", 5000)
acc2 = BankAccount("Ali", 3000)

show_balance(acc1)
show_balance(acc2)
compare_balance(acc1, acc2)