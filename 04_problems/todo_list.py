# Author: Moin Uddin
# Simple To-Do List
# Example: Add, view, and delete tasks

tasks = []

def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added!')

def view_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task(index):
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        print(f'Task "{removed}" deleted!')
    else:
        print("Invalid task number!")

while True:
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = int(input("Choose option (1/2/3/4): "))

    if choice == 1:
        task = input("Enter task: ")
        add_task(task)
    elif choice == 2:
        view_tasks()
    elif choice == 3:
        view_tasks()
        index = int(input("Enter task number to delete: "))
        delete_task(index)
    elif choice == 4:
        print("Goodbye!")
        break
    else:
        print("Invalid option!")