from unittest import TestCase
from Student_Grades_system import average_Grade, top_students

class TestStudentGradesSystem(TestCase):
    def test_average_Grade(self):
        
        average_Grade()
        self.assertTrue(True)  

    def test_top_students(self):
        
        top_students()
        self.assertTrue(True)
    