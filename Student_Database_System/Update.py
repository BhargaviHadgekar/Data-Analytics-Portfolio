from connector import DBConnector
from tabulate import tabulate


class GradeUpdater:

    def __init__(self):
        self.db = DBConnector()

    def update_grade(self):

        email = input("Enter Gmail ID: ")

        query = "SELECT student_id, name FROM Students WHERE email = ?"
        student = self.db.fetch_one(query, (email,))

        if not student:
            print("❌ Student not found")
            return

        student_id, name = student

        query = """
        SELECT c.course_name, g.grade
        FROM Grades g
        JOIN Courses c ON g.course_id = c.course_id
        WHERE g.student_id = ?
        """

        courses = self.db.fetch_query(query, (student_id,))

        print(f"\nStudent: {name} ({email})")
        print("--------------------------------")


        if courses:
            print(tabulate(courses, headers=["Course", "Grade"], tablefmt="grid"))
        else:
            print("No courses found")
            return
        
        student_coursees = [course[0] for course in courses]
        course = self.db.choose_course()

        if course not in student_coursees:
            print("❌ Student not enrolled in this course")
            return

        if not course:
            print("Invalid course")
            return

        new_grade = float(input("Enter new grade: "))

        update_query = """
        UPDATE Grades
        SET grade = ?
        WHERE student_id = ?
        AND course_id = (SELECT course_id FROM Courses WHERE course_name = ?)
        """

        self.db.execute_query(update_query, (new_grade, student_id, course))

        print("\n✅ Grade Updated Successfully")

        course_update_query = """
        SELECT c.course_name, g.grade name
        FROM Grades g JOIN Courses c ON g.course_id = c.course_id
        WHERE g.student_id = ? AND c.course_name = ?
        """
        updated_course = self.db.fetch_one(course_update_query, (student_id, course))
        print(tabulate([updated_course], headers=["Course", "Grade"], tablefmt="grid"))