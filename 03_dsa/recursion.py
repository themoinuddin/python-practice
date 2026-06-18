# recursion.py
# Author: Moin Uddin

def factorial(n):
    if n == 1:      # base case
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:      # base case
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(factorial(5))   # 120
print(fibonacci(7))   # 13