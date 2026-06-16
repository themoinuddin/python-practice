# stack.py
# Author: Moin Uddin

stack = []

stack.append(1)
stack.append(2)
stack.append(3)
print("Stack:", stack)

stack.pop()
print("After pop:", stack)

print("Top:", stack[-1])
print("Empty?", len(stack) == 0)