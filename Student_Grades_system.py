import pyodbc
from tabulate import tabulate

class GradeSystem:
    def __init__(self):
        self.conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=localhost\\SQLEXPRESS;'
            'DATABASE=Studentgrades;'
            'Trusted_Connection=yes;'
        )
        self.cursor = self.conn.cursor()

    def view_Students(self):
            self.cursor.execute("SELECT s.student_id, s.name,s.email,c.course_name, g.grade FROM Students as s JOIN Grades as g On s.student_id = g.student_id JOIN Courses as c ON g.course_id = c.course_id")
            students = self.cursor.fetchall()
            print(tabulate(students, headers=["Student ID", "Name", "Email", "Course", "Grade"], tablefmt="grid"))


    def add_Student(self):
        name = input("Enter student name: ")
        email = input("Enter student email: ")
        course = input("Enter course name: ")
        grade = float(input("Enter grade (0-100): "))

        
        self.cursor.execute("INSERT INTO Students (name, email) VALUES (?, ?)", (name, email))
        self.conn.commit()

        
        self.cursor.execute("SELECT student_id FROM Students WHERE email=?", (email,))
        student_id = self.cursor.fetchone()[0]

        
        self.cursor.execute("IF NOT EXISTS (SELECT * FROM Courses WHERE course_name=?) INSERT INTO Courses (course_name) VALUES (?)", (course, course))
        self.conn.commit()

        
        self.cursor.execute("SELECT course_id FROM Courses WHERE course_name=?", (course,))
        course_id = self.cursor.fetchone()[0]

        
        self.cursor.execute("INSERT INTO Grades (student_id, course_id, grade) VALUES (?, ?, ?)", (student_id, course_id, grade))
        self.conn.commit()

        print("Student added successfully!")
        print(f"Student ID: {student_id}\n, Name: {name}\n, Course: {course}\n, Grade: {grade}")

    def delete_Student(self):
        student_id = int(input("Enter student ID to delete: "))
        self.cursor.execute("DELETE FROM Grades WHERE student_id=?", (student_id,))
        self.cursor.execute("DELETE FROM Students WHERE student_id=?", (student_id,))
        self.conn.commit()
        print("Student deleted successfully!")

    def update_student_Grades(self):
        student_id = int(input("Enter student ID to update: "))
        course = input("Enter course name: ")
        new_grade = float(input("Enter new grade (0-100): "))

        self.cursor.execute("SELECT course_id FROM Courses WHERE course_name=?", (course,))
        course_id = self.cursor.fetchone()
        if not course_id:
            print("Course not found!")
            return
        course_id = course_id[0]

        self.cursor.execute("UPDATE Grades SET grade=? WHERE student_id=? AND course_id=?", (new_grade, student_id, course_id))
        self.conn.commit()
        print("Grade updated successfully!")

grade_system = GradeSystem()

print("Welcome to the Student Grade System!")
print("1. View Students")
print("2. Add Student")
print("3. Update Student Grades")
print("4. Delete Student")
choice = input("Enter your choice (1-4): ")

if choice == "1":
    grade_system.view_Students()
elif choice == "2":
    grade_system.add_Student()
elif choice == "3":
    grade_system.update_student_Grades()
elif choice == "4": 
    grade_system.delete_Student()
else:
    print("Invalid choice! Please enter a number between 1 and 4.")
