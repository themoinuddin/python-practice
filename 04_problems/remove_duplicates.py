# Author: Moin Uddin
# Remove Duplicates from a List (Without using set)
# Example: [1, 2, 2, 3, 4, 4] -> [1, 2, 3, 4]

def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Taking multiple elements as input from user
user_input = input("Enter elements separated by spaces: ")
elements = user_input.split()

result = remove_duplicates(elements)
print(f"List after removing duplicates: {result}")