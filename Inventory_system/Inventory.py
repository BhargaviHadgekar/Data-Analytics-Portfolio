from wsgiref import headers

import pyodbc
from tabulate import tabulate

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=localhost\\SQLEXPRESS;'
            'DATABASE=InventorySystem;'
            'Trusted_Connection=yes;')
cursor = conn.cursor()
        
def view_inventory():
    cursor.execute("SELECT id, name, category, quantity, purchase_price, selling_price, supplier  FROM Products ")
    products = cursor.fetchall()

    headers=["ID", "Name", "Category", "Quantity", "Purchase Price", "Selling Price", "Supplier"]

    for i in range(0,len(products),5):
        print(tabulate(products[i:i+5], headers=headers, tablefmt="grid"))
        while True:
            cont = input("View next 5 products? (y/n): ")
            if cont.lower() == "n":
                return
            elif cont.lower() == "y":
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")


def update_quantity():

    Select_id = int(input("Enter product ID to update quantity: "))

    cursor.execute("SELECT id, name, category, quantity , selling_price FROM Products WHERE id = ?", (Select_id,))
    result = cursor.fetchone()
    print(tabulate([result], headers=["ID", "Name", "Category", "Quantity", "Selling Price"], tablefmt="grid"))

    new_quantity = int(input("Enter new quantity: "))

    new_quantity += result[3]  

    cursor.execute("UPDATE Products SET quantity = ? WHERE id = ?", (new_quantity, Select_id))
    conn.commit()
    print("✅ Quantity updated successfully!")
    
    cursor.execute("SELECT id, name, category, quantity , selling_price FROM Products WHERE id = ?", (Select_id,))
    updated_result = cursor.fetchone()

    print(tabulate([updated_result], headers=["ID", "Name", "Category", "Quantity", "Selling Price"], tablefmt="grid"))
    

def delete_product():

    select_id = int(input("Enter product ID to delete: "))

    cursor.execute("SELECT id, name, category, quantity , selling_price FROM Products WHERE id = ?", (select_id,))
    result = cursor.fetchone()

    if not result:
        print("❌ Product not found!")
        return
    
    print(tabulate([result], headers=["ID", "Name", "Category", "Quantity", "Selling Price"], tablefmt="grid"))

    cursor.execute("SELECT p.id FROM Products p INNER JOIN Sales s ON p.id = s.product_id WHERE p.id = ?", (select_id,))
    sales_result = cursor.fetchone()

    if sales_result:
        print("❌ Cannot delete product: It exists in sales records!")
        return
    
    while True:
            delete_sales = input("Are you sure you want to delete this product? (y/n): ")
            if delete_sales.lower() == "y":
                cursor.execute("DELETE FROM Sales WHERE product_id = ?", (select_id,))
                cursor.execute("DELETE FROM Products WHERE id = ?", (select_id,))
                conn.commit()
                print("✅ Product deleted successfully!")
                return
            elif delete_sales.lower() == "n":
                print("Deletion cancelled.")
                return



def view_sales_records():
    

    cursor.execute("SELECT p.id,p.name,p.selling_price,s.quantity_sold,s.sale_date FROM Products p INNER JOIN Sales s ON p.id = s.product_id")
    sales_records = cursor.fetchall()

    headers=["ID", "Product Name", "Quantity Sold", "Sale Price", "Sale Date"]

    for i in range(0,len(sales_records),5):
        print(tabulate(sales_records[i:i+5], headers=headers, tablefmt="grid"))
        
        while True :
            cont = input("View next 5 sales records? (y/n): ")
            if cont.lower() == "n":
                return
            elif cont.lower() == "y":
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
    
              
def sell_product():
    select_id = int(input("Enter product ID to sell: "))

    cursor.execute("SELECT id, name, category, quantity , selling_price FROM Products WHERE id = ?", (select_id,))
    result = cursor.fetchone()

    if not result:
        print("❌ Product not found!")
        return
    
    print(tabulate([result], headers=["ID", "Name", "Category", "Quantity", "Selling Price"], tablefmt="grid"))

    quantity_to_sell = int(input("Enter quantity to sell: "))

    if quantity_to_sell > result[3]:
        print("❌ Insufficient stock!")
        return
    
    new_quantity = result[3] - quantity_to_sell

    cursor.execute("UPDATE Products SET quantity = ? WHERE id = ?", (new_quantity, select_id))
    
    cursor.execute("INSERT INTO Sales (product_id, quantity_sold, sale_date) VALUES (?, ?, GETDATE())", (select_id, quantity_to_sell))
    
    conn.commit()
    print("✅ Product sold successfully!") 

def total_sales():

    cursor.execute("SELECT p.id,p.name, p.selling_price,s.quantity_sold,s.sale_date ,(s.quantity_sold * p.selling_price)as Total_Sales FROM Sales s INNER JOIN Products p ON s.product_id = p.id")
    total = cursor.fetchall()


    headers=["ID", "Name", "Selling Price", "Quantity Sold", "Sale Date", "Total Sales"]

    print(tabulate(total, headers=headers, tablefmt="grid"))


if __name__ == "__main__":

    while True:
        print("Welcome to the Inventory Management System")
        print("1. View Inventory")
        print("2. Update Quantity")
        print("3. Delete Product")
        print("4. Sell Product")
        print("5. Sales Records")
        print("6. Total Sales")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            view_inventory()
        elif choice == '2':
            update_quantity()
        elif choice == '3':
            delete_product()
        elif choice == '4':
            sell_product()
        elif choice == '5':
            view_sales_records()
        elif choice == '6':
            total_sales()
        elif choice == '7':
            break
        else:
            print("Invalid choice! Please try again.")

            
























print("Invalid choice! Please try again.")