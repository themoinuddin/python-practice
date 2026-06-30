# Author: Moin Uddin
# Dice Roll Simulator
# Example: Rolls a number between 1-6

import random

def roll_dice():
    return random.randint(1, 6)

while True:
    input("Press Enter to roll the dice...")
    result = roll_dice()
    print(f"You rolled: {result}")

    again = input("Roll again? (y/n): ").lower()
    if again != 'y':
        print("Thanks for playing!")
        break