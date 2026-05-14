import os

FILE = "tasks.txt"


def add_to_file(task):
    with open(FILE, "a") as f:
        f.write(task + "\n")


def view_from_file():
    with open(FILE, "r") as f:
        for index, line in enumerate(f):
            print(f"-> {index + 1}- {line.strip()}")


def remove_from_file(index):
    with open(FILE, "r") as f:
        lines = f.readlines()

    if 0 < index <= len(lines):
        del lines[index - 1]

        # repopulate the file with existing tasks
        with open(FILE, "w") as f:
            f.writelines(lines)
        print(f"Removed task #{index}")
    else:
        print("Invalid task number!")


def main():
    while True:
        print("\n[1] Add, [2] View [3] Remove [4] Quit")
        choice = int(input("Choose: "))
        match choice:
            case 1:
                user_task = input("Task > ")
                add_to_file(user_task)
            case 2:
                view_from_file()
            case 3:
                view_from_file()
                num_to_remove = int(input("Task number to remove: "))
                remove_from_file(num_to_remove)
            case 4:
                print("Bye...")
                break
            case _:
                print("Unknown Choice!")


if __name__ == "__main__":
    main()
