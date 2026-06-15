import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

tasks = load_tasks()

while True:
    print("\n--- TO DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task_name = input("Enter task: ")
        tasks.append({"task": task_name, "done": False})
        save_tasks(tasks)
        print("Task added successfully")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available")
        else:
            for i, task in enumerate(tasks, start=1):
                status = "Done" if task["done"] else "Pending"
                print(f"{i}. {task['task']} - {status}")

    elif choice == "3":
        task_no = int(input("Enter task number to mark as done: "))
        if 1 <= task_no <= len(tasks):
            tasks[task_no - 1]["done"] = True
            save_tasks(tasks)
            print("Task marked as done")
        else:
            print("Invalid task number")

    elif choice == "4":
        task_no = int(input("Enter task number to delete: "))
        if 1 <= task_no <= len(tasks):
            tasks.pop(task_no - 1)
            save_tasks(tasks)
            print("Task deleted successfully")
        else:
            print("Invalid task number")

    elif choice == "5":
        print("Thank you")
        break

    else:
        print("Invalid choice")
