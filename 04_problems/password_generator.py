# Author: Moin Uddin
# Random Password Generator
# Example: length=8 → "aB3$kL9#"

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter password length: "))
if length < 4:
    print("Password length should be at least 4!")
else:
    password = generate_password(length)
    print(f"Generated Password: {password}")