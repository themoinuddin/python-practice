# Author: Moin Uddin
# Simple Calculator
# Example: 5 + 3 = 8

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        return "Error! Division by zero"
    return a / b

print("Simple Calculator")
print("1. Add  2. Subtract  3. Multiply  4. Divide")

choice = int(input("Choose operation (1/2/3/4): "))
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == 1:
    print(f"Result: {add(a, b)}")
elif choice == 2:
    print(f"Result: {subtract(a, b)}")
elif choice == 3:
    print(f"Result: {multiply(a, b)}")
elif choice == 4:
    print(f"Result: {divide(a, b)}")
else:
    print("Invalid choice!")