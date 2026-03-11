class TaskManager:


    @classmethod
    def storage(cls, no , Task, priority, status):
        record = {no: {1 : Task, 2: priority, 3:status  }}

    def add_task(self):
        title = input("Enter Task tltle: ")
        priority = input("Enter Task priority (Low/Midium/High): ")
        Task(title, priority )

    def view_task(self):
        pass








