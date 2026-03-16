from tabulate import tabulate

from connector import DBConnector


class StudentDeleter:

    def __init__(self):
        self.db = DBConnector()

    def delete_student(self):

        email = input("Enter Gmail ID to delete: ")

        query = "SELECT student_id, name FROM Students WHERE email = ?"
        student = self.db.fetch_one(query, (email,))

        if not student:
            print("❌ No student found with this email.")
            return

        student_id, name = student

        query = """
        SELECT c.course_name, g.grade
                FROM Grades g
                JOIN Courses c ON g.course_id = c.course_id
                WHERE g.student_id = ?"""

        courses = self.db.fetch_query(query, (student_id,))

        print(f"\nStudent: {name} ({email})")
        print("--------------------------------")

        for course_name, grade in courses:
            print(tabulate([(course_name, grade)], headers=["Course", "Grade"], tablefmt="grid"))

        student_coursees = [course[0] for course in courses]
        course = self.db.choose_course()

        if course not in student_coursees:
            print("❌ Student not enrolled in this course")
            return

        if not course:
            print("Invalid course")
            return

        delete_query = """
        DELETE FROM Grades
        WHERE student_id = ?
        AND course_id = (SELECT course_id FROM Courses WHERE course_name = ?)
        """

        self.db.execute_query(delete_query, (student_id, course))

        print("Course deleted successfully")