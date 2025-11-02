import sys

TODO_FILE = "todo.txt"

def add_task(task):
    with open(TODO_FILE, "a") as f:
        f.write(task + "\n")
    print(f"Added: {task}")

def list_tasks():
    try:
        with open(TODO_FILE) as f:
            tasks = f.readlines()
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks yet.")

def remove_task(index):
    with open(TODO_FILE) as f:
        tasks = f.readlines()
    try:
        removed = tasks.pop(index-1)
        with open(TODO_FILE, "w") as f:
            f.writelines(tasks)
        print(f"Removed: {removed.strip()}")
    except IndexError:
        print("Invalid task number.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python todo.py add/list/remove <task/index>")
        sys.exit(1)
    command = sys.argv[1].lower()
    if command == "add":
        add_task(" ".join(sys.argv[2:]))
    elif command == "list":
        list_tasks()
    elif command == "remove":
        remove_task(int(sys.argv[2]))
    else:
        print("Unknown command.")

