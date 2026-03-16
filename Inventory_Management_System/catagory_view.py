from connector import DBConnector
from tabulate import tabulate

class CategoryView:

    def __init__(self):
        self.db = DBConnector()

    def view_products_by_category(self):

        categories = [c[0] for c in self.db.get_categories()]

        for i, c in enumerate(categories,1):
            print(i,c)

        choice = int(input("Select category: "))

        category = categories[choice-1]

        products = self.db.view_by_category(category)

        page_size = 10
        start=0

        while True:
            page = products[start:start+page_size]

            if not page:
                print("No more products")
                break

            print(tabulate(page, headers=["ID","Name","Category","Qty","Purchase","Selling","Supplier"], tablefmt="grid"))
            start += page_size      
            if start >= len(products):
                print("End of products")
                break
            
            option = input("Press Enter for next page or 'q' to quit: ")
            if option.lower() == 'q':
                break
