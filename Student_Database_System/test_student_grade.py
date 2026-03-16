import unittest
from connector import DBConnector

class TestStudentGrade(unittest.TestCase):

    def setUp(self):
        self.db = DBConnector()

    def test_normalize_course(self):
        self.assertEqual(self.db.normalize_course("python"), "Python")
        self.assertEqual(self.db.normalize_course("JAVA"), "Java")
        self.assertEqual(self.db.normalize_course("C++"), "C++")
        self.assertEqual(self.db.normalize_course("MySQL"), "MySQL")
        self.assertIsNone(self.db.normalize_course("Ruby"))

    def test_validate_email(self):
        self.assertTrue(self.db.validate_email("bhargavi@gmail.com"))
        self.assertFalse(self.db.validate_email("bhargavi@yahoo.com"))
        self.assertFalse(self.db.validate_email("wrongemail"))

if __name__ == "__main__":
    unittest.main()