from create import StudentCreator
from Delete import StudentDeleter
from Update import GradeUpdater
from Reports import Reports

Creator = StudentCreator()
deletor = StudentDeleter()
Updater = GradeUpdater()
report = Reports()

def main():

    while True:
        print("\n === STUDENT GRADE SYSTEM ===")

        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student Grade")
        print("4. Delete Student Courses")
        print("5. Course Averages")
        print("6. Top Performars")
        print("7. Exit")

        choice = input("Enter choice number: " )

        if choice == "1":
            Creator.add_student()
        elif choice == "2":
            report.view_students_grouped()
        elif choice == "3":
            Updater.update_grade()
        elif choice == "4":
            deletor.delete_student()
        elif choice == "5":
            report.course_averages()
        elif choice == "6":
            report.top_performers()
        elif choice == "7":
            print("Exiting...")
            break
if __name__ == "__main__":
    main()