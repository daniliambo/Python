# title TaskManager Project
# description TaskManager Project
# code

import enum


class TaskStatus(enum.Enum):
    AWAIT = 0
    IN_PROGRES = 1
    COMPLETED = 2
    POSTPONED = 3


# init classes
class Task:
    def __init__(self, name, description, status):
        self.id = id
        self.name = name
        self.description = description
        self.status = status


class Subtask(Task):
    def __init__(self, name, description, status, parent_id):
        super().__init__(name, description, status)
        self.parent_id = parent_id


class ComplexTask(Task):
    def __init__(self, name, description, status, subtasks):
        super().__init__(id, name, description, status)
        self.subtasks = subtasks


class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.subtasks = {}
        self.complex_tasks = {}

    def create_task(self, task):
        self.tasks[id(task)] = task

    def create_subtask(self, subtask):
        self.subtasks[id(subtask)] = subtask

    def create_complex_task(self, complex_task):
        self.complex_tasks[id(complex_task)] = complex_task

    def get_tasks(self):
        return self.tasks

    def get_subtasks(self):
        return self.subtasks

    def get_complex_tasks(self):
        return self.complex_tasks

    def get_tasks_by_id(self, id):
        return self.tasks.get(id)

    def get_subtasks_by_id(self, id):
        return self.subtasks.get(id)

    def get_complex_tasks_by_id(self, id):
        return self.complex_tasks.get(id)

    def remove_tasks(self):
        self.tasks.clear()

    def remove_subtasks(self):
        self.subtasks.clear()

    def remove_complex_tasks(self):
        self.complex_tasks.clear()

    def remove_task_by_id(self, id):
        self.tasks.pop(id)

    def remove_subtask_by_id(self, id):
        self.subtasks.pop(id)

    def remove_complex_task_by_id(self, id):
        self.complex_tasks.pop(id)

    def update_status(self, task, new_status):
        self.get_tasks_by_id(id(task)).status = new_status

    def print_tasks(self):
        for id, task in self.tasks.items():
            print("Task", id)
            print("Name:", (task.name))
            print("Description:", task.description)
            print("Status:", task.status.name)

    def print_subtasks(self):
        for id, subtask in self.subtasks.items():
            print("Task", id)
            print("Name:", subtask.name)
            print("Description:", subtask.description)
            print("Status:", subtask.status.name)
            print("Parent id:", subtask.parent_id)

    def print_complex_tasks(self):
        for id_complex_tasks, complex_tasks in self.complex_tasks.items():
            for subtask in complex_tasks:
                print("Task", id_complex_tasks)
                print("Name:", subtask.name)
                print("Description:", subtask.description)
                print("Status:", subtask.status.name)
                print("Parent id:", subtask.parent_id)


# CREATE TASK MANAGER
manager = TaskManager()

# GENERATE TASKS
# tasks
task1 = Task("Clean your house", "Make dishes", TaskStatus.AWAIT)
task2 = Task("Find yourself a girlfriend", "Ask out Alice on a date", TaskStatus.COMPLETED)

# subtasks
task2_substask1 = Subtask("Buy milk", "Buy milk for a cat", TaskStatus.IN_PROGRES, id(task2))

# complex tasks
complex_task = [Subtask("Buy flowers", "Buy roses", TaskStatus.IN_PROGRES, id(task2)),
                Subtask("Buy drinks", "Buy wine and juices", TaskStatus.IN_PROGRES, id(task1))]

# create tasks
manager.create_task(task1)
manager.create_task(task2)

# create subtasks
manager.create_subtask(task2_substask1)

# create complex task
manager.create_complex_task(complex_task)

# printout the results
manager.print_tasks()
manager.print_subtasks()
manager.print_complex_tasks()
