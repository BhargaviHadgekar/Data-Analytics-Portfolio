import unittest
from Student_system.Student_Grades_system import GradeSystem
class TestGradeSystem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.grade_system = GradeSystem()
        cls.grade_system.cursor.execute("DELETE FROM Grades")
        cls.grade_system.cursor.execute("DELETE FROM Students")
        cls.grade_system.cursor.execute("DELETE FROM Courses")
        cls.grade_system.conn.commit()

    @classmethod
    def tearDownClass(cls):
        cls.grade_system.conn.close()