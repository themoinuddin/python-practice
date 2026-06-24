# Author: Moin Uddin
# Fibonacci Series Generator

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

num = int(input("Enter how many terms: "))
fibonacci(num)