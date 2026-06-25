# Author: Moin Uddin
# Find Greatest Common Divisor (GCD) of Two Numbers
# Example: 12 and 18 -> GCD is 6

def compute_gcd(a, b):
    # Select the smaller number
    smaller = min(a, b)
    gcd = 1
    
    for i in range(1, smaller + 1):
        if (a % i == 0) and (b % i == 0):
            gcd = i
            
    return gcd

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    if num1 <= 0 or num2 <= 0:
        print("Please enter positive integers greater than 0.")
    else:
        result = compute_gcd(num1, num2)
        print(f"The GCD/HCF of {num1} and {num2} is: {result}")
except ValueError:
    print("Invalid input! Please enter valid integers.")