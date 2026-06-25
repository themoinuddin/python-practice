# Author: Moin Uddin
# Rotate a List by N Positions (Right Rotation)
# Example: [1, 2, 3, 4, 5] rotated by 2 -> [4, 5, 1, 2, 3]

def rotate_list(lst, n):
    if not lst:
        return lst
    
    # Handle rotations larger than list length
    n = n % len(lst)
    
    # Slice logic: last n elements + everything before them
    return lst[-n:] + lst[:-n]

# Input for the list
user_list = input("Enter list elements separated by spaces: ").split()

try:
    rotations = int(input("Enter number of positions to rotate: "))
    result = rotate_list(user_list, rotations)
    print(f"Rotated List: {result}")
except ValueError:
    print("Please enter a valid integer for rotations.")