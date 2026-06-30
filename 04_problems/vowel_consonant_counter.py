# Author: Moin Uddin
# Vowel/Consonant Counter
# Example: "Hello World" → Vowels: 3, Consonants: 7

def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count

text = input("Enter a string: ")
v, c = count_vowels_consonants(text)
print(f"Vowels: {v}")
print(f"Consonants: {c}")