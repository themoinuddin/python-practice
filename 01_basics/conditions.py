# conditions.py
# Author: Moin Uddin

age = int(input("Enter age: "))

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")