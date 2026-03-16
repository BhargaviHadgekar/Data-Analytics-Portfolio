from tabulate import tabulate

from connector import DBConnector
from collections import defaultdict


class Reports:

    def __init__(self):
        self.db = DBConnector()

    def view_students_grouped(self):

        query = """
        SELECT s.name, s.email, c.course_name, g.grade
        FROM Grades g
        JOIN Students s ON g.student_id = s.student_id
        JOIN Courses c ON g.course_id = c.course_id
        ORDER BY s.name
        """

        rows = self.db.fetch_query(query)

        student_data = defaultdict(list)

        for name, email, course, grade in rows:
            student_data[(name, email)].append((course, grade))

        for (name, email), courses in student_data.items():

            print(f"\n{name} ({email})")
            print("--------------------------------")

            for course, grade in courses:
                print(course, grade)

    def course_averages(self):

        query = """
        SELECT c.course_name, AVG(g.grade)
        FROM Grades g
        JOIN Courses c ON g.course_id = c.course_id
        GROUP BY c.course_name
        """

        rows = self.db.fetch_query(query)

        table = [(course, round(avg, 2)) for course, avg in rows]
        print(tabulate(table, headers=["Course", "Average Grade"], tablefmt="grid"))


    def top_performers(self):

        query = """
        WITH max_grades AS (
            SELECT course_id, MAX(grade) AS max_grade
            FROM Grades
            GROUP BY course_id
        )
        SELECT c.course_name, s.name, g.grade
        FROM Grades g
        JOIN max_grades mg
        ON g.course_id = mg.course_id AND g.grade = mg.max_grade
        JOIN Students s ON g.student_id = s.student_id
        JOIN Courses c ON g.course_id = c.course_id
        """

        rows = self.db.fetch_query(query)

        print("\nTop Performers")

        table = [(course, student, grade) for course, student, grade in rows]
        print(tabulate(table, headers=["Course", "Student", "Grade"], tablefmt="grid"))

    