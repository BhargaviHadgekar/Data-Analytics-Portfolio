import pyodbc
from tabulate import tabulate

def get_connect():
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                              'SERVER=localhost;'
                              'DATABASE=InventoryDB;'
                              'Trusted_Connection=yes;')
        print("Connection to the database was successful.")
        return conn
        


# def view_inventory():
    
#     conn = get_connect()
#     cursor = conn.cursor()


#     cursor.execute("SELECT * FROM products")
#     rows = cursor.fetchall()

#     #first 10 rows then next 10 rows and so on
#     for i in range(0, len(rows), 10):
#         print(tabulate(rows[i:i+10], headers=[column[0] for column in cursor.description], tablefmt='psql'))
#         if i + 10 < len(rows):
#             input("Press Enter to view the next 10 rows...")
#     conn.close()    



if __name__ == "__main__":

    get_connect()
    # print("Welcome to the Inventory Management System!")
    # print("1. View Inventory")
    # print("2. Update Product")
    # print("3. Delete Product")
    # print("4. Exit")
    
    # while True:
    #     choice = input("Enter your choice: ")
    #     if choice == '1':
    #         view_inventory()
    #     elif choice == '2':
    #         pass
    #     elif choice == '3':
    #         pass
    #     elif choice == '4':
    #         print("Exiting the Inventory Management System. Goodbye!")
    #         break
        
