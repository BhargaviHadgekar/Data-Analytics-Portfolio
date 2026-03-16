from create import StudentCreator
from Delete import StudentDeleter
from Update import GradeUpdater
from Reports import Reports


creator = StudentCreator()
deleter = StudentDeleter()
updater = GradeUpdater()
report = Reports()


def main():

    while True:

        print("\n===== STUDENT GRADE SYSTEM =====")

        print("1. Add Student")
        print("2. View Students")
        print("3. Update Grade")
        print("4. Delete Student")
        print("5. Course Averages")
        print("6. Top Performers")
        print("7. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            creator.add_student()

        elif choice == "2":
            report.view_students_grouped()

        elif choice == "3":
            updater.update_grade()

        elif choice == "4":
            deleter.delete_student()

        elif choice == "5":
            report.course_averages()

        elif choice == "6":
            report.top_performers()

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()