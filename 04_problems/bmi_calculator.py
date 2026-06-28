# Author: Moin Uddin
# BMI Calculator
# Example: weight=70kg, height=1.75m → BMI=22.9 (Normal)

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (meters): "))

bmi = calculate_bmi(weight, height)
category = bmi_category(bmi)

print(f"Your BMI: {bmi:.2f}")
print(f"Category: {category}")