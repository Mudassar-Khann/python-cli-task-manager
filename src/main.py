from task_manager import TaskManager


def show_menu():
    """
    Displays menu options.
    """

    print("\n=== Python CLI Task Manager ===\n")

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Edit Task")
    print("6. Exit")


def main():


    manager = TaskManager()

    while True:

        show_menu()

        try:
            choice = int(input("Select option: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if choice == 1:

            title = input("Enter task title: ")
            priority = input("Enter priority (High/Medium/Low): ").strip().capitalize()

            manager.add_task(title, priority)

        elif choice == 2:

            manager.view_tasks()

        elif choice == 3:

            try:
                task_id = int(input("Enter task number to complete: "))
                manager.complete_task(task_id)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == 4:

            try:
                task_id = int(input("Enter task number to delete: "))
                manager.delete_task(task_id)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == 5:
            try:
              task_id = int(input("Enter task number to edit: "))

            except ValueError:
                print("plz enter valid number ")

            new_title = input("New title (leave blank to keep current): ")
            new_priority = input("New priority (High/Medium/Low, leave blank to keep current): ")

            manager.edit_task(task_id,new_priority,new_priority)

        elif choice == 6:

            print("Closing program...")
            print("Goodbye!")
            break

        else:
            print("Invalid option. Choose between 1–5.")


if __name__ == "__main__":
    main()
