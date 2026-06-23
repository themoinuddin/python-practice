# armstrong_number.py
# Author: Moin Uddin

# A number is Armstrong if sum of its digits
# each raised to the power of number of digits equals the number itself.
# Example: 153 = 1^3 + 5^3 + 3^3 = 153

def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == n

number = int(input("Enter a number: "))

if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
