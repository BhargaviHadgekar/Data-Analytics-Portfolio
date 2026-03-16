import pyodbc
import re


class DBConnector:

    def __init__(self):

        # Database connection
        self.conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=localhost\\SQLEXPRESS;'
            'DATABASE=StudentGrades;'
            'Trusted_Connection=yes;'
        )

        self.cursor = self.conn.cursor()

        # Course list
        self.VALID_COURSES = {
            "python": "Python",
            "java": "Java",
            "c++": "C++",
            "mysql": "MySQL"
        }

    # ---------- DATABASE METHODS ----------

    def execute_query(self, query, values=None):

        if values:
            self.cursor.execute(query, values)
        else:
            self.cursor.execute(query)

        self.conn.commit()

    def fetch_query(self, query, values=None):

        if values:
            self.cursor.execute(query, values)
        else:
            self.cursor.execute(query)

        return self.cursor.fetchall()
    
    def fetch_one(self, query, values=None):
        if values:
            self.cursor.execute(query, values)
        else:
            self.cursor.execute(query)

        return self.cursor.fetchone()

    # ---------- COURSE METHODS ----------

    def normalize_course(self, course_input):
        return self.VALID_COURSES.get(course_input.lower())

    def choose_course(self):

        print("\nChoose Course:")

        course_list = list(self.VALID_COURSES.values())

        for index, course in enumerate(course_list, start=1):
            print(f"{index}. {course}")

        choice = input("Enter choice number: ")

        if not choice.isdigit():
            return None

        choice = int(choice)

        if 1 <= choice <= len(course_list):
            return course_list[choice - 1]

        return None

    # ---------- EMAIL VALIDATION ----------

    def validate_email(self, email):

        pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'

        return re.match(pattern, email)