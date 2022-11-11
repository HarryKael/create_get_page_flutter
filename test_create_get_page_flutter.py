from create_get_page_flutter import renaming
import unittest

class TestRenaming(unittest.TestCase):
    def test_with_underscore_version_1(self):
        test_case = 'list_detail'
        expected = 'ListDetail'
        self.assertEqual(renaming(test_case), expected)

    def test_without_underscore_version_1(self):
        test_case = 'list'
        expected = 'List'
        self.assertEqual(renaming(test_case), expected)

    def test_with_underscore_version_2(self):
        test_case = 'list_detail'
        expected = 'listDetail'
        self.assertEqual(renaming(test_case, 2), expected)
    
    def test_without_underscore_version_2(self):
        test_case = 'list'
        expected = 'list'
        self.assertEqual(renaming(test_case, 2), expected)


if __name__ == '__main__':
    unittest.main()