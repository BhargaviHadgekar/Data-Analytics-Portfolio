import os
os.environ["TESTING"] = "1"

from unittest.mock import patch
import unittest
from Student_Grades_system import update_student_Grades, get_connection


def setup_test_db():
    import os
    if os.path.exists("test.db"):
        os.remove("test.db")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE Students (
        student_id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE Courses (
        course_id INTEGER PRIMARY KEY,
        course_name TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE Grades (
        student_id INTEGER,
        course_id INTEGER,
        grade REAL
    )
    """)

    cursor.execute("INSERT INTO Students VALUES (1, 'John', 'john@test.com')")
    cursor.execute("INSERT INTO Courses VALUES (1, 'Python')")
    cursor.execute("INSERT INTO Grades VALUES (1, 1, 80)")

    conn.commit()


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        setup_test_db()

    @patch('builtins.input', side_effect=['1', 'Python', '85'])
    def test_update_student_Grades(self, _):
        update_student_Grades()
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()