import unittest
from student import Student 
from datetime import timedelta
from unittest.mock import patch

class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.student = Student('john', 'doe')


    def tearDown(self):
        print('tearDown')

    def test_full_Name(self):
        print('test_full_name')
        self.assertEqual(self.student.full_name, 'john doe')


    def test_alert_santa(self):
        print("test_alert_santa")
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)


    def test_email_input(self):
        print('test_email_input')
        self.assertEqual(self.student.email, 'john.doe@email.com')

    
    def test_apply_extension(self):
        print("test_apply_extension")
        old_end_date = self.student.end_date
        self.student.apply_extension(5)

        self.assertAlmostEqual(self.student.end_date, old_end_date + timedelta(days=5))

    def test_course_schedule_success(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "something went wrong with the request")


if __name__ == '__main__':
    unittest.main()