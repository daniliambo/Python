# title Unittests Converter to README.md
# description Unittests Converter to README.md
# code


import unittest

from Converter import prepare_md_titles


# from converter import *

class TestConverter(unittest.TestCase):

    def test_prepare_md_titles(self):
        data = '# title Hello world\n# description Some description for out task'
        title, description = prepare_md_titles(data)
        self.assertEqual(title, 'Hello world')
        self.assertEqual(description, 'Some description for out task')

    def test_prepare_md_titles_with_empty_data(self):
        data = ''
        title, description = prepare_md_titles(data)
        self.assertEqual(title, None)
        self.assertEqual(description, None)

    def test_prepare_md_titles_with_extra_data(self):
        data = '# title Hello world\n# description Some description for out task\n# tag set, list'
        title, description = prepare_md_titles(data)
        self.assertEqual(title, 'Hello world')
        self.assertEqual(description, 'Some description for out task')


if __name__ == "__main__":
    unittest.main()
