from unittest.mock import patch
import unittest
from Student_Grades_system import average_Grade

class Test(unittest.TestCase):
    @patch('Student_Grades_system.cursor')
    
    def test_average(self, mock_cursor):
        mock_cursor.fetchall.return_value = [("Python", 80)]
        average_Grade()
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
    