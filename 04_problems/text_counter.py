# Author: Moin Uddin
# Text Counter (Lines, Words, and Characters)
# Example: Multi-line text input analysis

def analyze_text(text):
    # If text is empty
    if not text.strip():
        return 0, 0, 0
        
    lines = text.splitlines()
    line_count = len(lines)
    
    words = text.split()
    word_count = len(words)
    
    char_count = len(text)
    
    return line_count, word_count, char_count

print("Enter your text (Type 'END' on a new line to finish):")
lines = []
while True:
    line = input()
    if line == "END":
        break
    lines.append(line)

user_text = "\n".join(lines)
l, w, c = analyze_text(user_text)

print("\n--- Text Analysis ---")
print(f"Total Lines: {l}")
print(f"Total Words: {w}")
print(f"Total Characters (including spaces): {c}")