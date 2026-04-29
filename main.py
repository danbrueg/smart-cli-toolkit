import json
import os
import shutil
from pathlib import Path

# ----------------------------
# FILE PATHS
# ----------------------------
NOTES_FILE = "data/notes.json"
TASK_FILE = "data/tasks.json"


# ----------------------------
# MENU
# ----------------------------
def show_menu():
    print("\nSMART CLI TOOLKIT")
    print("1. File Organizer")
    print("2. Notes System")
    print("3. Task Tracker")
    print("4. Exit")


# ----------------------------
# NOTES SYSTEM
# ----------------------------
def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []

    try:
        with open(NOTES_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)


def notes_system():
    notes = load_notes()

    print("\nNOTES SYSTEM")
    print("1. Add Note")
    print("2. View Notes")

    choice = input("Choose: ")

    if choice == "1":
        note = input("Enter note: ")
        notes.append(note)
        save_notes(notes)
        print("Note saved!")

    elif choice == "2":
        print("\nYOUR NOTES:")
        if len(notes) == 0:
            print("No notes yet.")
        else:
            for i, note in enumerate(notes):
                print(f"{i+1}. {note}")


# ----------------------------
# FILE ORGANIZER
# ----------------------------
def file_organizer():
    folder = input("Enter full folder path to organize: ")

    path = Path(folder)

    if not path.exists():
        print("Folder not found.")
        return

    for file in path.iterdir():
        if file.is_file():
            ext = file.suffix.lower()

            if ext in [".jpg", ".png", ".jpeg"]:
                target = path / "Images"
            elif ext in [".pdf", ".docx", ".txt"]:
                target = path / "Documents"
            else:
                target = path / "Others"

            target.mkdir(exist_ok=True)
            shutil.move(str(file), str(target / file.name))

    print("Files organized successfully!")


# ----------------------------
# TASK TRACKER
# ----------------------------
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []

    try:
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def task_tracker():
    tasks = load_tasks()

    print("\nTASK TRACKER")
    print("1. Add Task")
    print("2. View Tasks")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append({"task": task, "done": False})
        save_tasks(tasks)
        print("Task added!")

    elif choice == "2":
        print("\nTASKS:")
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            for i, t in enumerate(tasks):
                status = "✓" if t["done"] else "✗"
                print(f"{i+1}. [{status}] {t['task']}")


# ----------------------------
# MAIN LOOP
# ----------------------------
def main():
    while True:
        show_menu()
        choice = input("Select an option: ")

        if choice == "1":
            file_organizer()

        elif choice == "2":
            notes_system()

        elif choice == "3":
            task_tracker()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()