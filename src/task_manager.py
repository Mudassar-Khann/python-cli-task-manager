from task import Task
class TaskManager:

    def __init__(self):
        self.storage = {}


    def add_task(self,task, priority):
            task = Task(task,priority)
            no = len(self.storage) + 1

            self.storage[no] = [task.title,task.priority,task.completed]



    def view_task(self):
        for key , value in self.storage.items():
             print(f"{key}. {value[0]} [{value[1]}] {'✔' if value[2] else '❌'}")

    def complete_task(self):
        pass

    def delete_task(self):
        pass



t = TaskManager()
print(t.storage)

t.add_task("do python", "high")
t.add_task("do cpp", "low")
t.view_task()
# print(t.view_task())



