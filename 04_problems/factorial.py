# factorial.py
# Author: Moin Uddin

# Factorial of n = n * (n-1) * (n-2) * ... * 1
# Example: 5! = 5 * 4 * 3 * 2 * 1 = 120

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

number = int(input("Enter a number: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {number} is {factorial(number)}")
