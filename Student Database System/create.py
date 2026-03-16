from connector import DBConnector


class StudentCreator:

    def __init__(self):
        self.db = DBConnector()

    def add_student(self):

        name = input("Enter student name: ").strip()
        email = input("Enter Gmail ID: ").strip()

        if not self.db.validate_email(email):
            print("❌ Invalid Email! Only @gmail.com allowed.")
            return

        course = self.db.choose_course()

        if not course:
            print("❌ Invalid course selection.")
            return

        grade = float(input("Enter grade (0-100): "))

        query = """
        IF NOT EXISTS (SELECT * FROM Students WHERE email=?)
        INSERT INTO Students (name, email) VALUES (?, ?)
        """

        self.db.execute_query(query, (email, name, email))

        query = "SELECT student_id FROM Students WHERE email=?"
        student_id = self.db.fetch_one(query, (email,))[0]

        query = """
        IF NOT EXISTS (SELECT * FROM Courses WHERE course_name=?)
        INSERT INTO Courses (course_name) VALUES (?)
        """

        self.db.execute_query(query, (course, course))

        query = "SELECT course_id FROM Courses WHERE course_name=?"
        course_id = self.db.fetch_one(query, (course,))[0]

        insert_query = """
        INSERT INTO Grades (student_id, course_id, grade)
        VALUES (?, ?, ?)
        """

        self.db.execute_query(insert_query, (student_id, course_id, grade))

        print("✅ Student Added Successfully")