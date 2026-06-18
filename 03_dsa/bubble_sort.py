# bubble_sort.py
# Author: Moin Uddin

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [5, 3, 1, 4, 2]
print("Before:", arr)
bubble_sort(arr)
print("After:", arr)