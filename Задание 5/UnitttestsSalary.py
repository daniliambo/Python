# title Unittests Salary Project
# description Unittests Salary Project
# code


import os
import Salary
import unittest


class TestConverter(unittest.TestCase):
    """
    Unittest class
    """

    def setUp(self) -> None:
        self.input_json_path = './input.json'
        self.output_json_path = './output.json'
        self.main = Salary.main
        self.main()

        with open(self.input_json_path, 'r') as f:
            content = f.read()
            self.input_json = content

        with open(self.output_json_path, 'r') as f:
            content = f.read()
            self.output_json = content

    def test_existence_of_input_path(self):
        self.assertTrue(os.path.exists(self.input_json_path))

    def test_output_json_is_not_empty(self):
        with open(self.output_json_path, 'r') as f:
            content = f.read()
            self.assertTrue(content)

    def test_json_output_contains_input(self):
        self.assertGreaterEqual(self.output_json, self.input_json)


if __name__ == '__main__':
    unittest.main()
