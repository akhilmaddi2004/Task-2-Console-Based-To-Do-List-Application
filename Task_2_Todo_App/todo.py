# todo.py
# Console-based To-Do List with file storage

import os

FILE_NAME="tasks.txt"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    
    with open(FILE_NAME,"r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        for t in tasks:
            f.write(t + "\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\nYour Tasks:")
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task}")

def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if not task:
        print("Empty task ignored.")
        return
    tasks.append(task)
    print("Task added.")

def remove_task(tasks):
    show_tasks(tasks)
    try:
        index=int(input("Enter task number to remove:"))
        tasks.pop(index-1)
        print("Task removed.")
    except:
        print("Invalid task number.")

def mark_done(tasks):
    show_tasks(tasks)
    try:
        index=int(input("Enter a task number to mark as done:"))
        tasks[index-1] = tasks[index-1] + "[DONE]"
        print("Task marked as done.")
    except:
        print("Invalid task number.")

def clear_all(tasks):
    tasks.clear()
    print("All tasks cleared.")

def main():
    tasks = load_tasks()

    while True:
        print("""
===== TO-DO LIST MENU =====
1. View Tasks
2. Add Task
3. Remove Task
4. Mark Task as Completed
5. Clear All Tasks
6.Exit
""")
        
        choice =input("Enter your choice:")
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            mark_done(tasks)
        elif choice == "5":
            clear_all(tasks)
        elif choice == "6":
            save_tasks(tasks)
            print("Tasks saved. Exiting.")
            break
        else:
            print("Invalid choive. Try again.")

if __name__ == "__main__":
    main()