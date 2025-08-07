import json
import os
from rep_card_app.student import Student

FILE_NAME = 'report_cards.json'

def save_data(students):
    with open(FILE_NAME, 'w') as file:
        json.dump([s.__dict__ for s in students], file, indent=4)
    print("Student data saved successfully.")

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            students_data = json.load(file)
            return [Student(**data) for data in students_data]
    return []

def add_student(students):
    name = input("Enter student name: ")
    scores = {}
    while True:
        subject = input("Enter subject (or 'done' to finish): ")
        if subject.lower() == 'done':
            break
        try:
            score = float(input(f"Enter score for {subject}: "))
            scores[subject] = score
        except ValueError:
            print("Invalid score. Please enter a number.")
    
    new_student = Student(name, scores)
    students.append(new_student)
    print(f"Student {name} added.")

def view_all_students(students):
    if not students:
        print("No student records found.")
        return
    for student in students:
        print(student)

def update_score(students):
    name = input("Enter student name to update: ")
    for student in students:
        if student.name.lower() == name.lower():
            subject = input("Enter subject to update: ")
            try:
                new_score = float(input(f"Enter new score for {subject}: "))
                student.scores[subject] = new_score
                student.average = student.calculate_average()
                student.grade = student.assign_grade()
                print(f"Score for {subject} updated for {name}.")
                return
            except ValueError:
                print("Invalid score. Please enter a number.")
    print("Student not found.")

def main():
    students = load_data()

    while True:
        print("\nStudent Report Card App")
        print(".......................")
        print("\n1. Add student")
        print("2. View all students")
        print("3. Update a student's score")
        print("4. Save & Exit")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_all_students(students)
        elif choice == '3':
            update_score(students)
        elif choice == '4':
            save_data(students)
            print("\nExiting........")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()