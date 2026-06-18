# operators.py
# Author: Moin Uddin

# Arithmetic
a, b = 10, 3
print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.33
print(a % b)   # 1
print(a ** b)  # 1000
print(a // b)  # 3

# Comparison
print(a > b)   # True
print(a == b)  # False
print(a != b)  # True

# Logical
print(a > 5 and b < 5)   # True
print(a > 15 or b < 5)   # True
print(not a > 5)          # False

# Assignment
x = 10
x += 5
print(x)  # 15
x *= 2
print(x)  # 30