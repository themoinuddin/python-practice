# Author: Moin Uddin
# Leap Year Checker
# Example: 2024 is a leap year, 2100 is not

def is_leap_year(year):
    # A year is leap if divisible by 4 but not by 100, unless also divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

try:
    year = int(input("Enter a year: "))
    if is_leap_year(year):
        print(f"{year} is a Leap Year!")
    else:
        print(f"{year} is not a Leap Year.")
except ValueError:
    print("Please enter a valid year.")