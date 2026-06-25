# Author: Moin Uddin
# Move All Zeroes to the End of the List
# Example: [0, 1, 0, 3, 12] -> [1, 3, 12, 0, 0]

def move_zeroes(lst):
    # Filter all non-zero elements
    non_zeroes = [x for x in lst if x != 0]
    
    # Count how many zeroes were there
    zero_count = lst.count(0)
    
    # Combine non-zeroes with the zeroes added at the end
    return non_zeroes + [0] * zero_count

# Input for the list
user_input = input("Enter numbers separated by spaces: ")
try:
    num_list = [int(x) for x in user_input.split()]
    result = move_zeroes(num_list)
    print(f"Result after moving zeroes: {result}")
except ValueError:
    print("Please enter valid integers only.")