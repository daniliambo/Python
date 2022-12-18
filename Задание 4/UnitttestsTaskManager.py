# title Unittests TaskManager Project
# description Unittests TaskManager Project
# code

import os
import TaskManager
import unittest


class TestConverter(unittest.TestCase):
    """
    Unittest class
    """

    def setUp(self) -> None:
        self.input_json_path = './input.json'
        self.output_json_path = './output.json'
        self.TaskManager = TaskManager

        # prepare TaskManager

        # tasks
        self.task1 = self.TaskManager.Task("Clean your house", "Make dishes", self.TaskManager.TaskStatus.AWAIT)
        self.task2 = self.TaskManager.Task("Find yourself a girlfriend", "Ask out Alice on a date",
                                           self.TaskManager.TaskStatus.COMPLETED)

        # subtasks
        self.task2_substask1 = self.TaskManager.Subtask("Buy milk", "Buy milk for a cat",
                                                        self.TaskManager.TaskStatus.IN_PROGRES, id(self.task2))

        # complex tasks
        self.complex_task = [
            self.TaskManager.Subtask("Buy flowers", "Buy roses", self.TaskManager.TaskStatus.IN_PROGRES,
                                     id(self.task2)),
            self.TaskManager.Subtask("Buy drinks", "Buy wine and juices", self.TaskManager.TaskStatus.IN_PROGRES,
                                     id(self.task1))]

        # create tasks
        self.TaskManager.manager.create_task(self.task1)
        self.TaskManager.manager.create_task(self.task2)

        # create subtasks
        self.TaskManager.manager.create_subtask(self.task2_substask1)

        # create complex task
        self.TaskManager.manager.create_complex_task(self.complex_task)

    # test is instance
    def test_is_instance_subtask(self):
        self.assertIsInstance(self.task2_substask1, self.TaskManager.Subtask)

    # test inequality
    def test_inequality_of_different_tasks(self):
        self.assertNotEqual(first=self.task1, second=self.task2)

if __name__ == '__main__':
    unittest.main()
