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

        print(f"\nProduct details:{pid}({data[0][1]})")
        print(f"Category: {data[0][2]}")
        print(f"Quantity: {data[0][3]}")
        print(f"Purchase Price: {data[0][4]}")
        print(f"Selling Price: {data[0][5]}")
        print(f"Supplier: {data[0][6]}")

        product = self.db.get_product_by_id(pid)
        
    

        if not product:
            print("Product not found")
            return

        confirm = input("Delete product? (yes/no): ")

        if confirm == "yes":
            try:
                self.db.delete_product(pid)
                print("Product deleted")
            except Exception as e:
                print(f"Error deleting product: {e}")