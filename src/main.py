from task import Task
from task_manager import TaskManager


while True:
    print("=== python cli Task Manager ===", end="\n\n")

    print("""
1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Exit

                """)

    user_choice = int(input("Select Option: "))


    if user_choice == 5:
        print("Closing program.....")
        print("Godbye!")
        break

    if user_choice == 1:
        pick_title = input("Enter task title: ")
        pick_priority = input("Enter priority (High/Medium/Low): ").strip().capitalize()
        TaskManager.add_task(pick_title,pick_priority)

    elif user_choice == 2:
        TaskManager.view_task()

    elif user_choice == 3:
        TaskManager.complete_task()

    elif user_choice == 4:
        TaskManager.delete_task()




