class TaskManager:
    def __init__(self):
        self.tasks=[]
    def add_task(self,task_name):
        self.tasks.append(task_name)
    def show_tasks(self):
        print('name of task')
        for x in self.tasks:
            print("*",x)

TaskManager1=TaskManager()
TaskManager1.add_task('Learn Git')
TaskManager1.add_task('Practice Python')
TaskManager1.show_tasks()

