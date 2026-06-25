# Author: Moin Uddin
# Password Strength Checker
# Criteria: Length >= 8, contains at least one digit, and one special character

def check_password_strength(password):
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)
    length_ok = len(password) >= 8
    
    if length_ok and has_digit and has_special:
        return "Strong 💪"
    elif length_ok and (has_digit or has_special):
        return "Moderate 😐"
    else:
        return "Weak ⚠️ (Make sure it is at least 8 characters long and has numbers/special characters)"

pwd = input("Enter a password to check strength: ")
strength = check_password_strength(pwd)
print(f"Password Strength: {strength}")