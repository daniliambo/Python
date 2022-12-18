# title Converter csv to json
# description Unittests
# code


import os
import Converter
import unittest
from Converter import Converter


# to test:
# 1. csv_path exists and not empty
# 2. read return is type of list
# 3. read return == 'content'
# 4. creates non-empty file

class TestConverter(unittest.TestCase):
    """
    Unittest class
    """

    def setUp(self) -> None:
        csv_path = './input.csv'
        json_path = './output.json'
        test_csv_path = 'unittest.json'
        self.conv = Converter(csv_path=csv_path, json_path=json_path)

        with open(test_csv_path) as f:
            content = f.read()
            self.test_csv = content

    # init
    def test_existence_of_csv_path(self):
        self.assertTrue(os.path.exists(self.conv.ipath))

    def test_csv_is_not_empty(self):
        with open(self.conv.ipath, 'r') as f:
            content = f.read()
            self.assertTrue(content)

    # hm?
    def test_content_of_output_json(self):
        print(self.conv.read())
        print(self.test_csv)
        self.assertEqual(self.test_csv, self.conv.read())

    def test_json_path_exists_and_not_empty(self):
        self.assertFalse(os.stat(self.conv.opath).st_size == 0)
        self.assertTrue(os.path.exists(self.conv.opath))


if __name__ == '__main__':
    unittest.main()
