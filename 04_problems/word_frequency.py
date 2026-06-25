# Author: Moin Uddin
# Word Frequency Counter
# Example: "apple banana apple" -> {"apple": 2, "banana": 1}

def count_word_frequency(sentence):
    # Remove punctuation and convert to lowercase
    cleaned_sentence = "".join(char.lower() if char.isalnum() or char.isspace() else "" for char in sentence)
    words = cleaned_sentence.split()
    
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
            
    return frequency

user_input = input("Enter a sentence: ")
result = count_word_frequency(user_input)

print("\n--- Word Frequencies ---")
for word, count in result.items():
    print(f"'{word}': {count}")