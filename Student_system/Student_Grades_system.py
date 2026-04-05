import pyodbc
from tabulate import tabulate

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=localhost\\SQLEXPRESS;'
            'DATABASE=StudentGrades;'
            'Trusted_Connection=yes;')
cursor = conn.cursor()


def view_Students():
        cursor.execute("SELECT s.student_id, s.name,s.email,c.course_name, g.grade FROM Students as s JOIN Grades as g On s.student_id = g.student_id JOIN Courses as c ON g.course_id = c.course_id")
        students = cursor.fetchall()
        print(tabulate(students, headers=["Student ID", "Name", "Email", "Course", "Grade"], tablefmt="grid"))



def add_Student():
    name = input("Enter student name: ")
    email = input("Enter student email: ")

    c = ["Python", "Java", "C++", "MySQL"]
    course = input("Enter course name (Python,Java,C++,MySQL): ")
    if course not in c:
        print("❌ Invalid course name!")
        return
    grade = float(input("Enter grade (0-100): "))

    cursor.execute("SELECT * FROM Students WHERE email = ?", (email,))
    existing = cursor.fetchone()

    if existing:
        print("❌ Student with this email already exists!")
        return
    
    cursor.execute("INSERT INTO Students (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    
    cursor.execute("SELECT student_id FROM Students WHERE email=?", (email,))
    student_id = cursor.fetchone()[0]
    
    cursor.execute("IF NOT EXISTS (SELECT * FROM Courses WHERE course_name=?) INSERT INTO Courses (course_name) VALUES (?)", (course, course))
    conn.commit()
    
    cursor.execute("SELECT course_id FROM Courses WHERE course_name=?", (course,))
    course_id = cursor.fetchone()[0]
    
    cursor.execute("INSERT INTO Grades (student_id, course_id, grade) VALUES (?, ?, ?)", (student_id, course_id, grade))
    conn.commit()
    print("Student added successfully!")
    print(f"Student ID: {student_id}\n, Name: {name}\n, Course: {course}\n, Grade: {grade}")



def delete_Student():
    student_id = int(input("Enter student ID to delete: "))
    cursor.execute("DELETE FROM Grades WHERE student_id=?", (student_id,))
    cursor.execute("DELETE FROM Students WHERE student_id=?", (student_id,))
    conn.commit()
    print("Student deleted successfully!")



def update_student_Grades():
    student_id = int(input("Enter student ID to update: "))
    course = input("Enter course name: ")
    new_grade = float(input("Enter new grade (0-100): "))
    cursor.execute("SELECT course_id FROM Courses WHERE course_name=?", (course,))
    course_id = cursor.fetchone()
    if not course_id:
        print("Course not found!")
        return
    course_id = course_id[0]
    cursor.execute("UPDATE Grades SET grade=? WHERE student_id=? AND course_id=?", (new_grade, student_id, course_id))
    conn.commit()
    print("Grade updated successfully!")

def average_Grade():
    cursor.execute("SELECT c.course_name, AVG(g.grade) FROM Grades g JOIN Courses c ON g.course_id = c.course_id GROUP BY c.course_name")
    averages = cursor.fetchall()
    print(tabulate(averages, headers=["Course", "Average Grade"], tablefmt="grid"))

def top_students():

    cursor.execute("SELECT TOP 5 s.name, c.course_name, g.grade FROM Grades g JOIN Students s ON g.student_id = s.student_id JOIN Courses c ON g.course_id = c.course_id ORDER BY g.grade DESC ")

    top_students = cursor.fetchall()


    print(tabulate(top_students, headers=["Name", "Course", "Grade"], tablefmt="grid"))


if __name__ == "__main__":

    while True:
        print("\nStudent Grades Management System")
        print("1. View Students")
        print("2. Add Student")
        print("3. Delete Student")
        print("4. Update Student Grades")
        print("5. View Average Grades")
        print("6. View Top Students")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
              view_Students()
        elif choice == '2':
            add_Student()
        elif choice == '3':
            delete_Student()
        elif choice == '4':
            update_student_Grades()
        elif choice == '5':
            average_Grade()
        elif choice == '6':
            top_students()
        elif choice == '7':
            break
        else:
            print("Invalid choice! Please try again.")
            print("Invalid choice! Please try again.")