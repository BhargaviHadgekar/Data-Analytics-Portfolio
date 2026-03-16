from connector import DBConnector

class Inventory:

    def __init__(self):
        self.db = DBConnector()

    def view_by_category(self, category):
        query = """
        SELECT id, name, category, quantity,
               purchase_price, selling_price, supplier
        FROM Products
        WHERE category = ?
        """
        return self.db.fetch_query(query, (category,))

    def get_categories(self):
        query = """
        SELECT DISTINCT category
        FROM Products
        ORDER BY category
        """
        return self.db.fetch_query(query)

    def update_quantity(self, product_id, quantity):
        query = """
        UPDATE Products
        SET quantity = quantity + ?
        WHERE id = ?
        """
        self.db.execute_query(query, (quantity, product_id))

    def delete_product(self, product_id):
        query = "SELECT * FROM Products WHERE id = ?"
        data = self.db.fetch_query(query, (product_id,))
        if not data:
            print("❌ Product not found")
            return
        
        query = "DELETE FROM Products WHERE id = ?"
        self.db.execute_query(query, (product_id,))

    def get_product_by_id(self, pid):
        query = "SELECT * FROM Products WHERE id = ?"
        data = self.db.fetch_query(query, (pid,))
        return data[0] if data else None