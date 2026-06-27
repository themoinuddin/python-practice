# Author: Moin Uddin
# Anagram Checker
# Example: "listen" and "silent" are anagrams

def is_anagram(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())

word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

if is_anagram(word1, word2):
    print(f'"{word1}" and "{word2}" are Anagrams!')
else:
    print(f'"{word1}" and "{word2}" are NOT Anagrams!')