# Author: Moin Uddin
# Even/Odd Checker
# Example: 4 is Even, 7 is Odd

def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number: "))
print(f"{num} is {check_even_odd(num)}")