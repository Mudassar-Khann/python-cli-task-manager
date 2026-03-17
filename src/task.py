class Task:
    """
    Represents a single task
    """

    def __init__(self, title: str, priority: str, status: bool = False):
        self.title = title
        self.priority = priority
        self.completed = status

    def mark_complete(self):

        self.completed = True

   
