from connector import DBConnector

class Reports:

    def __init__(self):
        self.db = DBConnector()

    def daily_profit(self):

        query = """
        SELECT p.id,p.name,p.category,p.quantity,
        p.purchase_price,p.selling_price,
        (p.selling_price-p.purchase_price),
        SUM(s.quantity_sold),
        SUM(s.quantity_sold*(p.selling_price-p.purchase_price)),
        p.supplier
        FROM Products p
        JOIN Sales s ON p.id=s.product_id
        WHERE DATEDIFF(DAY,s.sale_date,GETDATE())=0
        GROUP BY p.id,p.name,p.category,p.quantity,
        p.purchase_price,p.selling_price,p.supplier
        """

        return self.db.fetch_query(query)

    def weekly_profit(self):

        query = """
        SELECT p.id,p.name,p.category,p.quantity,
        p.purchase_price,p.selling_price,
        (p.selling_price-p.purchase_price),
        SUM(s.quantity_sold),
        SUM(s.quantity_sold*(p.selling_price-p.purchase_price)),
        p.supplier
        FROM Products p
        JOIN Sales s ON p.id=s.product_id
        WHERE DATEDIFF(WEEK,s.sale_date,GETDATE())=0
        GROUP BY p.id,p.name,p.category,p.quantity,
        p.purchase_price,p.selling_price,p.supplier
        """

        return self.db.fetch_query(query)

    def monthly_profit(self):

        query = """
        SELECT p.id,p.name,p.category,p.quantity,
        p.purchase_price,p.selling_price,
        (p.selling_price-p.purchase_price),
        SUM(s.quantity_sold),
        SUM(s.quantity_sold*(p.selling_price-p.purchase_price)),
        p.supplier
        FROM Products p
        JOIN Sales s ON p.id=s.product_id
        WHERE DATEDIFF(MONTH,s.sale_date,GETDATE())=0
        GROUP BY p.id,p.name,p.category,p.quantity,
        p.purchase_price,p.selling_price,p.supplier
        """

        return self.db.fetch_query(query)