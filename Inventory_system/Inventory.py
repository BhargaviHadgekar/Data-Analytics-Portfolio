import pyodbc
import datetime
from tabulate import tabulate

def get_connection():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;DATABASE=InventorySystem;Trusted_Connection=yes;'
    )
print("Welcome to the Inventory Management System!")