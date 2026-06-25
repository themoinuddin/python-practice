# Author: Moin Uddin
# Find Max and Min in a List (Without built-in functions)
# Example: [3, 1, 9, 4] -> Max: 9, Min: 1

def find_max_min(numbers):
    if not numbers:
        return None, None
        
    max_num = numbers[0]
    min_num = numbers[0]
    
    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
            
    return max_num, min_num

# Taking multiple numbers as input from user
user_input = input("Enter numbers separated by spaces: ")
num_list = [int(x) for x in user_input.split()]

max_val, min_val = find_max_min(num_list)

print(f"Largest Number: {max_val}")
print(f"Smallest Number: {min_val}")