# sets.py
# Author: Moin Uddin

s = {1, 2, 3, 3, 4, 4}
print(s)

s.add(5)
print(s)

s.remove(1)
print(s)

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # union
print(a & b)  # intersection
print(a - b)  # difference