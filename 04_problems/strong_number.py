# Author: Moin Uddin
# Strong Number Checker
# Example: 145 = 1! + 4! + 5! = 1 + 24 + 120 = 145 (Strong!)

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def is_strong(n):
    return sum(factorial(int(d)) for d in str(n)) == n

num = int(input("Enter a number: "))
if is_strong(num):
    print(f"{num} is a Strong Number!")
else:
    print(f"{num} is NOT a Strong Number!")