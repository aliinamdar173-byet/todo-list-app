# Simple To-Do List App
# Author: Inamdar Mohammad Ali

import os

FILE_NAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        tasks = [line.strip() for line in f.readlines() if line.strip()]
    return tasks

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def display_tasks(tasks):
    print("\n" + "=" * 40)
    print("         YOUR TO-DO LIST")
    print("=" * 40)
    if not tasks:
        print("  No tasks yet! Add some tasks.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"  {i}. {task}")
    print("=" * 40)

def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f'Task "{task}" added successfully!')
    else:
        print("Task cannot be empty.")

def delete_task(tasks):
    display_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f'Task "{removed}" deleted successfully!')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    print("\nWelcome to the To-Do List App!")

    while True:
        print("\nWhat would you like to do?")
        print("  1. View tasks")
        print("  2. Add a task")
        print("  3. Delete a task")
        print("  4. Exit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye! Stay productive!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
