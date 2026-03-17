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


    def to_dict(self):
        """
        NEW: convert object to dictionary for JSON
        """
        return {
            "title": self.title,
            "priority": self.priority,
            "completed": self.completed
        }


    @staticmethod
    def from_dict(data):
      
        return Task(data["title"], data["priority"], data["completed"])

