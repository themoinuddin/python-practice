# Author: Moin Uddin
# Caesar Cipher (basic encryption)
# Example: "HELLO" with shift 3 → "KHOOR"

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

print("Caesar Cipher")
print("1. Encrypt")
print("2. Decrypt")

choice = int(input("Choose option (1/2): "))
text = input("Enter text: ")
shift = int(input("Enter shift value: "))

if choice == 1:
    print(f"Encrypted: {encrypt(text, shift)}")
elif choice == 2:
    print(f"Decrypted: {decrypt(text, shift)}")
else:
    print("Invalid choice!")