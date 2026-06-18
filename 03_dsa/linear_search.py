# linear_search.py
# Author: Moin Uddin

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [3, 7, 1, 9, 4]
result = linear_search(arr, 9)

if result != -1:
    print(f"Found at index: {result}")
else:
    print("Not found")