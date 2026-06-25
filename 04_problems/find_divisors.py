# Author: Moin Uddin
# Find All Divisors of a Given Number
# Example: 12 -> 1, 2, 3, 4, 6, 12

def get_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

try:
    num = int(input("Enter a positive integer: "))
    if num <= 0:
        print("Please enter a number greater than 0.")
    else:
        result = get_divisors(num)
        print(f"The divisors of {num} are: {result}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")