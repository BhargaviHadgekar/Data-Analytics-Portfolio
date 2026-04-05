import unittest
from unittest.mock import patch
from Inventory import sell_product, cursor

class Test(unittest.TestCase):

    @patch('builtins.input', side_effect=['4', '2'])
    def test_sell(self, _):

        cursor.execute("SELECT quantity FROM Products WHERE id = 4")
        initial = cursor.fetchone()[0]

        sell_product()

      
        cursor.execute("SELECT quantity FROM Products WHERE id = 4")
        updated = cursor.fetchone()[0]

        self.assertEqual(updated, initial - 2)

if __name__ == "__main__":
    unittest.main()