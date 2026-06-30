# Author: Moin Uddin
# Palindrome Checker
# Example: "radar" is a palindrome, "hello" is not

def is_palindrome(s):
    # Removing spaces and converting to lowercase for accurate check
    clean_str = "".join(s.split()).lower()
    return clean_str == clean_str[::-1]

user_input = input("Enter a string: ")

if is_palindrome(user_input):
    print(f"'{user_input}' is a Palindrome!")
else:
    print(f"'{user_input}' is not a Palindrome.")