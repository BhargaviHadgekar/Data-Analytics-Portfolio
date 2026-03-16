from inventory import Inventory
from tabulate import tabulate

class CategoryView:

    def __init__(self):
        self.inventory = Inventory()

    def view_products_by_category(self):

        categories = [c[0] for c in self.inventory.get_categories()]

        for i, c in enumerate(categories,1):
            print(i,c)

        choice = int(input("Select category: "))

        category = categories[choice-1]

        products = self.inventory.view_by_category(category)

        print(tabulate(products,
        headers=["ID","Name","Category","Qty",
        "Purchase","Selling","Supplier"],
        tablefmt="grid"))