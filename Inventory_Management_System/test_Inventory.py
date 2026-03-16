import unittest

from connector import DBConnector
from reports import Reports
from sales import Sales


class TestInventory(unittest.TestCase):

    def setUp(self):
        """
        Runs before every test.
        Creates class objects used in tests.
        """
        self.db = DBConnector()
        self.reports = Reports()
        self.sales = Sales()


    # Test database connection
    def test_database_connection(self):

        result = self.db.fetch_query("SELECT 1")

        self.assertEqual(result[0][0], 1)


    # Test viewing products by category
    def test_view_category(self):

        data = self.db.view_by_category("Electronics")

        self.assertIsInstance(data, list)


    # Test updating product quantity
    def test_update_quantity(self):

        old = self.db.fetch_query(
            "SELECT quantity FROM Products WHERE id = 1"
        )[0][0]

        self.inventory.update_quantity(1, 5)

        new = self.db.fetch_query(
            "SELECT quantity FROM Products WHERE id = 1"
        )[0][0]

        self.assertEqual(new, old + 5)


    # Test weekly profit report
    def test_weekly_profit(self):

        data = self.reports.weekly_profit()

        self.assertIsInstance(data, list)


    # Test monthly profit report
    def test_monthly_profit(self):

        data = self.reports.monthly_profit()

        self.assertIsInstance(data, list)


    # Test viewing sales
    def test_view_sales(self):

        data = self.sales.view_sales()

        self.assertIsInstance(data, list)


    # Test inserting a sale
    def test_insert_sale(self):

        self.db.execute_query("""
            INSERT INTO Sales (product_id, quantity_sold, sale_date)
            VALUES (1, 2, GETDATE())
        """)

        result = self.db.fetch_query("""
            SELECT TOP 1 quantity_sold
            FROM Sales
            WHERE product_id = 1
            ORDER BY sale_date DESC
        """)

        self.assertEqual(result[0][0], 2)


if __name__ == "__main__":
    unittest.main()