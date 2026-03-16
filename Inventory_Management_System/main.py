from auto_stock import AutoStock
from csvImport import CSVImporter
from catagory_view import CategoryView
from update_quantity import UpdateQuantity
from delete import DeleteProduct
from profit import ProfitMenu
from sales import Sales
from tabulate import tabulate

auto = AutoStock()
csv = CSVImporter()
category = CategoryView()
update = UpdateQuantity()
delete = DeleteProduct()
profit = ProfitMenu()
sales = Sales()

auto.monthly_stock_check()
csv.import_products()

while True:

    print("\n===== INVENTORY SYSTEM =====")
    print("1 View Category")
    print("2 Update Quantity")
    print("3 Delete Product")
    print("4 Profit Report")
    print("5 Record Sale")
    print("6 View Sales")
    print("7 Exit")

    ch=input("Choice:")

    if ch=="1":
        category.view_products_by_category()

    elif ch=="2":
        update.update_quantity_interactive()

    elif ch=="3":
        delete.delete_product_interactive()

    elif ch=="4":
        profit.profit_report()

    elif ch=="5":
        sales.add_sale()

    elif ch=="6":
        data=sales.view_sales()
        print(tabulate(data, headers=["Sale ID","Product Name","Quantity Sold","Sale Date"], tablefmt="grid"      ))
        print("✅ Sales data retrieved")

    elif ch=="7":
        break