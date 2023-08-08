import unittest
from Employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp_default = Employee('Dan', 'Reza', 1000)
        self.emp_custom = Employee('Omi', 'abc', 5000, 2000)

    def test_give_default(self):
        x = self.emp_default.give_raise()
        self.assertEqual(x, 6000)

    def test_custom_raise(self):
        x = self.emp_custom.give_raise()
        self.assertEqual(x, 7000)


if __name__ == '__main__':
    unittest.main()