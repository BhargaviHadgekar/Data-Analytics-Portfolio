import pyodbc

class DBConnector:

    def __init__(self):
        self.conn = pyodbc.connect(
            "DRIVER={SQL Server};"
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