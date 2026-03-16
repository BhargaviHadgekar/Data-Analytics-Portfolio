from tabulate import tabulate
from connector import DBConnector

class UpdateQuantity:

    def __init__(self):
        self.db = DBConnector()

    def update_quantity_interactive(self):

        pid = int(input("Enter Product ID: "))

        product = self.db.get_product_by_id(pid)

        if not product:
            print("❌ Product not found")
            return

        print(tabulate([product],
        headers=["ID","Name","Category","Qty","Purchase","Selling","Supplier"],
        tablefmt="grid"))

        qty = int(input("Enter Quantity: "))

        self.db.update_quantity_db(pid, qty)

        print(f"\nUpdated Quantity ")
        print(tabulate([self.db.get_product_by_id(pid)],
        headers=["ID","Name","Category","Qty","Purchase","Selling","Supplier"], tablefmt="grid"))

        print("✅ Quantity Updated")