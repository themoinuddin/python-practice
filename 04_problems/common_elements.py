# Author: Moin Uddin
# Find Common Elements Between Two Lists
# Example: [1, 2, 3] and [2, 3, 4] -> Common: [2, 3]

def find_common(list1, list2):
    common = []
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
    return common

# Input for first list
input1 = input("Enter first list elements (separated by spaces): ")
list_a = input1.split()

# Input for second list
input2 = input("Enter second list elements (separated by spaces): ")
list_b = input2.split()

result = find_common(list_a, list_b)
print(f"Common elements: {result}")