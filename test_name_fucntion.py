import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    "Test for name_function.py"
    def test_first_last_name(self):
        formatted_name = get_formatted_name('Janis', 'Joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name('Mohammed', 'Reza', 'Danish')
        self.assertEqual(formatted_name, 'Mohammed Danish Reza')


if __name__ == '__main__':
    unittest.main()