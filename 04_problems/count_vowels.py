# Author: Moin Uddin
# Count Vowels and Consonants in a String
# Example: "Hello" -> Vowels: 2, Consonants: 3

def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    
    for char in s:
        if char.isalpha():  # Check if it's a letter
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
                
    return vowel_count, consonant_count

user_input = input("Enter a sentence: ")
v_count, c_count = count_vowels_consonants(user_input)

print(f"Vowels: {v_count}")
print(f"Consonants: {c_count}")