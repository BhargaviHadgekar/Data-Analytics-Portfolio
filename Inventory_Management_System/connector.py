import pyodbc

class DBConnector:

    def __init__(self):
        self.conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost\\SQLEXPRESS;"
            "DATABASE=InventorySystem;"
            "Trusted_Connection=yes;"
        )
        self.cursor = self.conn.cursor()

    def execute_query(self, query, values=None):
        if values:
            self.cursor.execute(query, values)
        else:
            self.cursor.execute(query)

        self.conn.commit()

    def fetch_query(self, query, values=None):
        if values:
            self.cursor.execute(query, values)
        else:
            self.cursor.execute(query)

        return self.cursor.fetchall()

    def get_product_by_id(self, pid):
        query = """
        SELECT id, name, category, quantity,
               purchase_price, selling_price, supplier
        FROM Products
        WHERE id = ?
        """
        self.cursor.execute(query, (pid,))
        return self.cursor.fetchone()

    def update_quantity_db(self, pid, qty):
        query = "UPDATE Products SET quantity = quantity + ? WHERE id = ?"
        self.cursor.execute(query, (qty, pid))
        self.conn.commit()

    def delete_product_db(self, pid):

        self.cursor.execute(
            "SELECT COUNT(*) FROM Sales WHERE product_id = ?", (pid,)
        )
        count = self.cursor.fetchone()[0]

        if count > 0:
            print("❌ Cannot delete product. Sales records exist.")
            confirm = input("Delete related sales records first? (y/n): ")

            if confirm.lower() == "y":
                self.cursor.execute(
                    "DELETE FROM Sales WHERE product_id = ?", (pid,)
                )
            else:
                return

        self.cursor.execute(
            "DELETE FROM Products WHERE id = ?", (pid,)
        )

        self.conn.commit()
        print("✅ Product deleted successfully")

    def view_by_category(self, category):
        query = """
        SELECT id, name, category, quantity,
               purchase_price, selling_price, supplier
        FROM Products
        WHERE category = ?
        """
        return self.fetch_query(query, (category,))

    def get_categories(self):
        query = """
        SELECT DISTINCT category
        FROM Products
        ORDER BY category
        """
        return self.fetch_query(query)