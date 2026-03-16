from datetime import datetime
from connector import DBConnector

class AutoStock:

    def __init__(self):
        self.db = DBConnector()

    def monthly_stock_check(self):

        today = datetime.now()

        if today.day == 1:

            query = """
            UPDATE Products
            SET quantity = quantity + 10
            """

            self.db.execute_query(query)

            print("✅ Monthly stock updated")