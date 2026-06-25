# Author: Moin Uddin
# Rock, Paper, Scissors Game
# Example: User chooses Rock, Computer chooses Scissors -> User Wins!

import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    
    user_choice = input("Enter Rock, Paper, or Scissors: ").strip().lower()
    
    if user_choice not in choices:
        print("Invalid choice! Please choose Rock, Paper, or Scissors.")
        return

    print(f"Computer chose: {computer_choice.capitalize()}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win! 🎉")
    else:
        print("Computer wins! 🤖")

play_game()