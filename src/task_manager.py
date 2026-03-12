from task import Task
class TaskManager:

    def __init__(self):
        self.storage = {}


    def add_task(self,task, priority):
            task = Task(task,priority)
            no = len(self.storage) + 1

            self.storage[no] = [task.title,task.priority,task.completed]



    def view_task(self):
        if len(self.storage) == 0:
             print("Task list is empty")
        else:
            for key , value in self.storage.items():
                print(f"{key}. {value[0]} [{value[1]}] {'✔' if value[2] else '❌'}")

    def complete_task(self):
         no = int(input("Enter Task no to complete: "))
         if  no > len(self.storage) or no < 0:
              print("Invalid no")
         else:
              self.storage[no][2] = True
              print("Task marked as completed.")



    def delete_task(self):
        pass


def main():
    t = TaskManager()
    # print(t.storage)



    t.add_task("do python", "high")
    t.add_task("do cpp", "low")
    t.view_task()

    t.complete_task()

    t.view_task()

if __name__ == "__main__":
     main()



