# Author: Moin Uddin
# Coin Flip Simulator
# Example: Heads or Tails randomly

import random

def flip_coin():
    return random.choice(["Heads", "Tails"])

while True:
    input("Press Enter to flip the coin...")
    result = flip_coin()
    print(f"Result: {result}!")
    
    again = input("Flip again? (y/n): ").lower()
    if again != 'y':
        print("Thanks for playing!")
        break