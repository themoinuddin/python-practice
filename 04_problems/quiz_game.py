# Author: Moin Uddin
# Simple Quiz Game
# Example: Asks questions, tracks score

questions = {
    "What is the capital of Pakistan?": "islamabad",
    "Which language is used for web styling?": "css",
    "What does CPU stand for?": "central processing unit",
    "Which planet is known as the Red Planet?": "mars",
    "What is 5 + 7?": "12"
}

score = 0

print("Welcome to the Quiz Game!\n")

for question, answer in questions.items():
    user_answer = input(question + " ").strip().lower()
    if user_answer == answer:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! Correct answer: {answer}\n")

print(f"Quiz Over! Your Score: {score}/{len(questions)}")