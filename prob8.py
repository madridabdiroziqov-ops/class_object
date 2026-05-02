class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title: str):
        self.tasks.append(title)

    def complete_task(self, task_id: int):
        self.tasks.pop(task_id-1)
        print(self.tasks)

    def delete_task(self, task_id: int):
        self.tasks.pop(task_id-1)
        print(self.tasks)

    def list_tasks(self):
        print(self.tasks)

manager = TaskManager()

manager.add_task("Python loyihasini tugatish")
manager.add_task("MySQL bilan ishlashni o'rganish")

manager.complete_task(1)

manager.delete_task(2)

manager.list_tasks()