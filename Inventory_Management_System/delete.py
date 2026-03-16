from tabulate import tabulate

from connector import DBConnector

class DeleteProduct:

    def __init__(self):
        self.db = DBConnector()

    def delete_product_interactive(self):

        pid = int(input("Enter Product ID: "))

        query = "SELECT * FROM Products WHERE id = ?" 
        data = self.db.fetch_query(query, (pid,))

        if not data:
            print("❌ Product not found")
            return
        
        pid = data[0][0]  # Extract the product ID from the fetched data

        query = """
        SELECT P.id, P.name, P.category, P.quantity,
               P.purchase_price, P.selling_price, P.supplier
               FROM Products P
               JOIN Sales S ON P.id = S.product_id
               WHERE P.id = ?"""
        self.db.execute_query(query, (pid,))

        print(f"\nProduct details")
        print(tabulate([self.db.get_product_by_id(pid)], headers=["ID","Name","Category","Qty","Purchase","Selling","Supplier"], tablefmt="grid"))

        product = self.db.get_product_by_id(pid)
        
    

        if not product:
            print("Product not found")
            return

        option = input("Delete product? (y/n): ")

        if option.lower() == 'y':
            self.db.delete_product_db(pid)
        else:
            print("❌ Deletion cancelled")
        