import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('setUp Class')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDown Class')

    def setUp(self):
        print('setUp called')
        self.emp_1 = Employee('John', 'Doe', 10000)
        self.emp_2 = Employee('Jane', 'Doe', 20000)

    def tearDown(self):
        print('tearDown called')


    def test_email(self):
        # emp_1 = Employee('John', 'Doe', 10000)
        # emp_2 = Employee('Jane', 'Doe', 20000)

        print('test_email called')

        self.assertEqual(self.emp_1.email, 'John.Doe@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Doe@email.com')

        self.emp_1.first_name = 'Mary'
        self.emp_2.first_name = 'Harry'

        self.assertEqual(self.emp_1.email, 'Mary.Doe@email.com')
        self.assertEqual(self.emp_2.email, 'Harry.Doe@email.com')

    def test_fullname(self):
        # emp_1 = Employee('John', 'Doe', 10000)
        # emp_2 = Employee('Jane', 'Doe', 20000)

        print('test_fullname called')

        self.assertEqual(self.emp_1.full_name, 'John Doe')
        self.assertEqual(self.emp_2.full_name, 'Jane Doe')

        self.emp_1.first_name = 'Mary'
        self.emp_2.first_name = 'Harry'

        self.assertEqual(self.emp_1.full_name, 'Mary Doe')
        self.assertEqual(self.emp_2.full_name, 'Harry Doe')

    def test_apply_raise(self):
        # emp_1 = Employee('John', 'Doe', 10000)
        # emp_2 = Employee('Jane', 'Doe', 20000)

        print('test_apply_raise called')

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.salary, 10500)
        self.assertEqual(self.emp_2.salary, 21000)


if __name__ == '__main__':
    unittest.main()