# Author: Moin Uddin
# Simple and Compound Interest Calculator
# Formulas: 
# Simple Interest = (P * R * T) / 100
# Compound Interest = P * (1 + R/100)^T - P

def calculate_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    
    # Compound interest formula
    compound_interest = principal * ((1 + rate / 100) ** time) - principal
    
    return simple_interest, compound_interest

try:
    p = float(input("Enter Principal amount (P): "))
    r = float(input("Enter Annual Interest Rate in % (R): "))
    t = float(input("Enter Time in years (T): "))
    
    si, ci = calculate_interest(p, r, t)
    
    print("\n--- Interest Calculation Results ---")
    print(f"Simple Interest: {si:.2f}")
    print(f"Compound Interest: {ci:.2f}")
    print(f"Total Amount (with Compound Interest): {(p + ci):.2f}")

except ValueError:
    print("Please enter valid numbers for the calculation.")