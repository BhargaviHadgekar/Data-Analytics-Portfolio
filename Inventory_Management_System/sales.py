from datetime import datetime
from connector import DBConnector
from inventory import Inventory
from tabulate import tabulate

class Sales:

    def __init__(self):
        self.db = DBConnector()
        self.inventory = Inventory()

    def add_sale(self):

        product_id = int(input("Enter Product ID: "))

        product = self.inventory.get_product_by_id(product_id)

        if not product:
            print("❌ Product not found")
            return

        print(tabulate([product],
              headers=["ID","Name","Category","Qty",
                       "Purchase","Selling","Supplier"],
              tablefmt="grid"))

        quantity = int(input("Enter Quantity Sold: "))

        query = """
        INSERT INTO Sales (product_id, quantity_sold, sale_date)
        VALUES (?, ?, ?)
        """

        self.db.execute_query(query, (product_id, quantity, datetime.now()))

        self.db.execute_query(
            "UPDATE Products SET quantity = quantity - ? WHERE id = ?",
            (quantity, product_id)
        )

        print("✅ Sale recorded")

    def view_sales(self):

        query = """
        SELECT 
        s.sale_id,
        p.name,
        s.quantity_sold,
        s.sale_date
        FROM Sales s
        JOIN Products p
        ON s.product_id = p.id
        """

        return self.db.fetch_query(query)