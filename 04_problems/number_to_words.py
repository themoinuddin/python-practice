# Author: Moin Uddin
# Number to Words
# Example: 21 → Twenty One

ones = ["", "One", "Two", "Three", "Four", "Five", "Six",
        "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
        "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
        "Eighteen", "Nineteen"]

tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty",
        "Sixty", "Seventy", "Eighty", "Ninety"]

def number_to_words(n):
    if n == 0:
        return "Zero"
    elif n < 0:
        return "Minus " + number_to_words(-n)
    elif n < 20:
        return ones[n]
    elif n < 100:
        return tens[n // 10] + ("" if n % 10 == 0 else " " + ones[n % 10])
    elif n < 1000:
        return ones[n // 100] + " Hundred" + ("" if n % 100 == 0 else " " + number_to_words(n % 100))
    else:
        return "Number too large!"

num = int(input("Enter a number (0-999): "))
print(f"{num} → {number_to_words(num)}")