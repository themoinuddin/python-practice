# Author: Moin Uddin
# Temperature Converter

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def kelvin_to_celsius(k):
    return k - 273.15

print("Temperature Converter")
print("1. Celsius to Fahrenheit & Kelvin")
print("2. Fahrenheit to Celsius")
print("3. Kelvin to Celsius")

choice = int(input("Choose option (1/2/3): "))

if choice == 1:
    c = float(input("Enter Celsius: "))
    print(f"{c}°C = {celsius_to_fahrenheit(c)}°F = {celsius_to_kelvin(c)}K")
elif choice == 2:
    f = float(input("Enter Fahrenheit: "))
    print(f"{f}°F = {fahrenheit_to_celsius(f):.2f}°C")
elif choice == 3:
    k = float(input("Enter Kelvin: "))
    print(f"{k}K = {kelvin_to_celsius(k):.2f}°C")
else:
    print("Invalid option!")