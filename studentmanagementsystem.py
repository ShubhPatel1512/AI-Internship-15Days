import json

students = []

# Load records from JSON file
def load_data():
    global students
    try:
        with open("students.json", "r") as file:
            students = json.load(file)
        print("Data loaded successfully!")
    except FileNotFoundError:
        students = []
        print("No existing records found.")

# Save records to JSON file
def save_data():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)
    print("Data saved successfully!")

# Add Student
def add_student():

    while True:
        sid = input("Enter Student ID: ")

        if any(student["id"] == sid for student in students):
            print("Student ID already exists!")
            print("Please enter a unique ID.\n")
        else:
            break

    name = input("Enter Student Name: ")

    while True:
        try:
            age = int(input("Enter Age: "))
            break
        except ValueError:
            print("Invalid Age! Enter a number.")

    course = input("Enter Course: ")

    student = {
        "id": sid,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    print("Student added successfully!")

# View Students
def view_students():

    if len(students) == 0:
        print("No student records found.")
        return

    print("\n----- STUDENT RECORDS -----")

    for student in students:
        print(f"""
Student ID : {student['id']}
Name       : {student['name']}
Age        : {student['age']}
Course     : {student['course']}
----------------------------
""")

# Search Student
def search_student():

    choice = input("Search by ID or Name (id/name): ").lower()

    if choice == "id":

        sid = input("Enter Student ID: ")

        for student in students:
            if student["id"] == sid:
                print(student)
                return

    elif choice == "name":

        name = input("Enter Student Name: ").lower()

        for student in students:
            if student["name"].lower() == name:
                print(student)
                return

    else:
        print("Invalid Choice!")
        return

    print("Student not found!")

# Update Student
def update_student():

    sid = input("Enter Student ID to update: ")

    for student in students:

        if student["id"] == sid:

            student["name"] = input("Enter New Name: ")

            while True:
                try:
                    student["age"] = int(input("Enter New Age: "))
                    break
                except ValueError:
                    print("Invalid Age!")

            student["course"] = input("Enter New Course: ")

            print("Record updated successfully!")
            return

    print("Student not found!")

# Delete Student
def delete_student():

    sid = input("Enter Student ID to delete: ")

    for student in students:

        if student["id"] == sid:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found!")

# Main Menu
def menu():

    load_data()

    while True:

        print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Save Records")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            save_data()

        elif choice == "7":
            save_data()
            print("Thank You!")
            print("Program Closed.")
            break

        else:
            print("Invalid Choice! Try Again.")

# Start Program
menu()