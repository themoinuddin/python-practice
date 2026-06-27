# Author: Moin Uddin
# Simple ATM Machine
# Example: Check balance, deposit, withdraw

balance = 10000

def check_balance():
    print(f"Current Balance: Rs. {balance}")

def deposit(amount):
    global balance
    if amount <= 0:
        print("Invalid amount!")
    else:
        balance += amount
        print(f"Rs. {amount} deposited. New Balance: Rs. {balance}")

def withdraw(amount):
    global balance
    if amount <= 0:
        print("Invalid amount!")
    elif amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        print(f"Rs. {amount} withdrawn. New Balance: Rs. {balance}")

while True:
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Choose option (1/2/3/4): "))

    if choice == 1:
        check_balance()
    elif choice == 2:
        amount = float(input("Enter deposit amount: Rs. "))
        deposit(amount)
    elif choice == 3:
        amount = float(input("Enter withdrawal amount: Rs. "))
        withdraw(amount)
    elif choice == 4:
        print("Thank you for using ATM!")
        break
    else:
        print("Invalid option!")