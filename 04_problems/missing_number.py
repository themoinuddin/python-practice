# Author: Moin Uddin
# Find the Missing Number in a Sequence from 1 to N
# Formula: Sum of first N numbers = N * (N + 1) / 2

def find_missing_number(lst, n):
    # Calculate what the total sum should be
    expected_sum = n * (n + 1) // 2
    
    # Calculate actual sum of current elements
    actual_sum = sum(lst)
    
    # The difference is the missing number
    return expected_sum - actual_sum

try:
    print("Example: If N is 5, enter 4 numbers from 1 to 5 (e.g., 1 2 4 5)")
    n = int(input("Enter the total count of numbers (N): "))
    
    user_input = input(f"Enter {n-1} numbers separated by spaces: ")
    num_list = [int(x) for x in user_input.split()]
    
    if len(num_list) != n - 1:
        print(f"Error: Please enter exactly {n-1} numbers.")
    else:
        missing = find_missing_number(num_list, n)
        print(f"The missing number is: {missing}")
        
except ValueError:
    print("Invalid input! Please enter proper integers.")