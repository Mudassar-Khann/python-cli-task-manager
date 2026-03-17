from task import Task
import json

class TaskManager:
    """
    Handles all operations on tasks.
    """

    def __init__(self):
        self.tasks = {}

        try:
            with open("src/tasks.json", "r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            data = {}

        for task_id, task_data in data.items():
            self.tasks[int(task_id)] = Task.from_dict(task_data)


    def generate_id(self):
        """

        Always generate next max ID
        """
        return max(self.tasks.keys(), default=0) + 1


    def add_task(self, title, priority):
        """
        Add new task
        """
        if priority not in {"High", "Medium", "Low"}:
            print("Invalid priority. Use High/Medium/Low.")
            return

        task = Task(title, priority)

        task_id = self.generate_id()

        self.tasks[task_id] = task

        print("Task added successfully.")


    def add_task(self, title, priority):
        """
        Creates a new task and stores it.
        """
        task = Task(title, priority)

        task_id = len(self.tasks) + 1

        self.tasks[task_id] = task

        print("Task added successfully.")

    def view_tasks(self):
        """
        Prints all tasks.
        """
        if not self.tasks:
            print("Task list is empty.")
            return

        for task_id, task in self.tasks.items():
            status = "✔" if task.completed else "❌"

            print(f"{task_id}. {task.title} [{task.priority}] {status}")

    def complete_task(self, task_id):
        """
        Marks a task as completed.
        """

        if task_id not in self.tasks:
            print("Invalid task number.")
            return

        self.tasks[task_id].mark_complete()

        print("Task marked as completed.")

    def delete_task(self, task_id):
        """
        Deletes a task.
        """

        if task_id not in self.tasks:
            print("Task does not exist.")
            return

        self.tasks.pop(task_id)

        print("Task deleted successfully.")

    def edit_task(self, task_id):

        if task_id not in self.tasks:
            print("Task does not exist.")
            return

        task = self.tasks[task_id]

        new_title = input("New title (leave blank to keep current): ")
        new_priority = input("New priority (High/Medium/Low, leave blank to keep current): ")

        if new_title:
            task.title = new_title

        if new_priority:
            if new_priority in {"High", "Medium", "Low"}:
                task.priority = new_priority
            else:
                print("Invalid priority. Keeping old value.")

        print("Task updated successfully.")





