import pandas as pd
from connector import DBConnector

class CSVImporter:

    def __init__(self):
        self.db = DBConnector()

    def import_products(self, file_path="Inventory_100_Products.csv"):

        try:

            df = pd.read_csv(file_path)

            for _, row in df.iterrows():

                query = """
                IF NOT EXISTS
                (SELECT 1 FROM Products WHERE name=?)
                INSERT INTO Products
                (name,category,quantity,purchase_price,selling_price,supplier)
                VALUES (?,?,?,?,?,?)
                """

                values = (
                    row['name'],
                    row['name'],
                    row['category'],
                    row['quantity'],
                    row['purchase_price'],
                    row['selling_price'],
                    row['supplier']
                )

                self.db.execute_query(query, values)

        except Exception as e:
            print("CSV Import Error:", e)