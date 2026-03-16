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

        elif choice=="2":
            data=self.reports.weekly_profit()

        elif choice=="3":
            data=self.reports.monthly_profit()

        print(tabulate(data))