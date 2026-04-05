import unittest
from Inventory import get_connection
class TestInventory(unittest.TestCase):
    def test_connection(self):
        try:
            conn = get_connection()
            self.assertIsNotNone(conn)
            print("Connection to the database was successful.")
        except Exception as e:
            self.fail(f"Connection to the database failed: {e}")