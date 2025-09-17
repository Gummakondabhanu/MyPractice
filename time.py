import time
from datetime import datetime
class Task:
    def __init__(self, name, execution_time):
        self.name = name
        self.execution_time = execution_time
class TaskScheduler:
    def __init__(self):
        self.tasks = []
    def add_task(self, name, execution_time):
        task = Task(name, execution_time)
        self.tasks.append(task)
    def run(self):
        for task in self.tasks:
            print(f"Starting task: {task.name}")
            start_time = datetime.now()
            time.sleep(task.execution_time)
            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()
            print(f"Completed task: {task.name}")
            print(f"Time taken: {duration:.2f} seconds\n")
scheduler = TaskScheduler()
scheduler.add_task("Backup Database", 2)
scheduler.add_task("Generate Reports", 3)
scheduler.add_task("Send Emails", 1)
scheduler.run()