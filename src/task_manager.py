from task import Task

class TaskManager:
    """
    Handles all operations on tasks.
    """

    def __init__(self):
        self.tasks = {}

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
