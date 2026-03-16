from reports import Reports
from tabulate import tabulate

class ProfitMenu:

    def __init__(self):
        self.reports = Reports()

    def profit_report(self):

        print("1 Daily")
        print("2 Weekly")
        print("3 Monthly")

        choice = input("Choice:")

        if choice=="1":
            data=self.reports.daily_profit()
            print(tabulate(data, headers=["ID","Name","Category","Qty","Purchase","Selling","Profit/Unit","Qty Sold","Total Profit","Supplier"], tablefmt="grid"      ))
            print("✅ Daily profit calculated")

        elif choice=="2":
            data=self.reports.weekly_profit()
            print(tabulate(data, headers=["ID","Name","Category","Qty","Purchase","Selling","Profit/Unit","Qty Sold","Total Profit","Supplier"], tablefmt="grid"      ))
            print("✅ Weekly profit calculated")

        elif choice=="3":
            data=self.reports.monthly_profit()
            print(tabulate(data, headers=["ID","Name","Category","Qty","Purchase","Selling","Profit/Unit","Qty Sold","Total Profit","Supplier"], tablefmt="grid"      ))
            print("✅ Monthly profit calculated")