from unittest.mock import patch
import unittest
from Student_Grades_system import average_Grade, top_students, update_student_Grades

class Test(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', "Python", '85'])
    
    def test_update_student_Grades(self, _):

        update_student_Grades()
        self.assertTrue(True)

    @patch('builtins.input', side_effect=['1'])
    def test_average_Grade(self, _):
        
        average_Grade()
        self.assertTrue(True)  

    @patch('builtins.input', side_effect=['1'])
    def test_top_students(self, _):
        
        top_students()
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
    