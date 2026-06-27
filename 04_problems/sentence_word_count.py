# Author: Moin Uddin
# Count Words in Sentence
# Example: "Hello World" → 2 words

def count_words(sentence):
    words = sentence.strip().split()
    return len(words)

sentence = input("Enter a sentence: ")
count = count_words(sentence)
print(f"Word count: {count}")