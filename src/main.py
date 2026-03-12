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

    user_choice = input("Select Option: ")


    if user_choice == "5":
        print("Closing program.....")
        break


