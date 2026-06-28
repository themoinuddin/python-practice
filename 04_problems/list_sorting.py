# Author: Moin Uddin
# List Sorting
# Example: [3, 1, 4, 1, 5] → [1, 1, 3, 4, 5]

def get_list():
    nums = input("Enter numbers separated by spaces: ")
    return list(map(int, nums.split()))

numbers = get_list()

print(f"Original List: {numbers}")
print(f"Ascending Order: {sorted(numbers)}")
print(f"Descending Order: {sorted(numbers, reverse=True)}")