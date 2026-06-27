# Author: Moin Uddin
# Multiplication Table
# Example: Table of 5 → 5 x 1 = 5, 5 x 2 = 10...

def multiplication_table(n):
    print(f"\nMultiplication Table of {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

num = int(input("Enter a number: "))
multiplication_table(num)