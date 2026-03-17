class Task:
    def __init__(self, title, priority, status=False):
        self.title = title
        self.priority = priority
        self.completed = status

    def mark_complete(self):
        self.completed = True




