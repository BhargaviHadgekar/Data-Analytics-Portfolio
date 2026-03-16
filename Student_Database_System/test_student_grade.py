

import unittest


from Student_Database_System.connector import DBConnector
from Student_Database_System.create import StudentCreator
from Student_Database_System.Delete import StudentDeleter
from Student_Database_System.Update import GradeUpdater
from Student_Database_System.Reports import Reports


class TestStudentGrade(unittest.TestCase):

    def test_normalize_course(self):
        self.assertEqual(DBConnector.normalize_course("python"), "Python")
        self.assertEqual(DBConnector.normalize_course("JAVA"), "Java")
        self.assertEqual(DBConnector.normalize_course("C++"), "C++")
        self.assertEqual(DBConnector.normalize_course("MySQL"), "MySQL")
        self.assertIsNone(DBConnector.normalize_course("Ruby"))

    def test_validate_email(self):
        self.assertTrue(DBConnector.validate_email("bhargavi@gmail.com"))
        self.assertFalse(DBConnector.validate_email("bhargavi@yahoo.com"))
        self.assertFalse(DBConnector.validate_email("wrongemail"))


if __name__ == "__main__":
    unittest.main()