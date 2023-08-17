class Task:
    def set_task_detail(self, task_name, priority):
        self.task_name = task_name
        self.priority = priority
        self.completed = False

    def mark_as_complete(self):
        self.completed = True

    def display_task_info(self):
        status = "Completed" if self.completed else "Not Completed"
        print(f"Task: {self.task_name}")
        print(f"Priority: {self.priority}")
        print(f"Status: {status}")
        print()
task1 = Task()
task2 = Task()
task3 = Task()
task1.set_task_detail("Complete project proposal", "High")
task2.set_task_detail("Buy groceries", "Medium")
task3.set_task_detail("Call customer support", "Low")
task1.mark_as_complete()
task3.mark_as_complete()
print("ToDo List:")
task1.display_task_info()
task2.display_task_info()
task3.display_task_info()
