import json


# Load students from file
try:
    with open("students.json", "r") as file:
        students = json.load(file)

except FileNotFoundError:
    students = []


# Input validation functions
def get_valid_int(message):

    while True:
        try:
            return int(input(message))

        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_valid_float(message):

    while True:
        try:
            return float(input(message))

        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Save students to JSON file
def save_students():

    with open("students.json", "w") as file:
        json.dump(students, file)


# Display one student
def display_student(student):

    print("ID:", student["id"])
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Department:", student["department"])
    print("CGPA:", student["cgpa"])
    print("------------------------")


# Get student details
def get_student_details(student_id):
    print(">>> get_student_details() was called")
    student_name = input("Enter student Name: ")
    student_age = get_valid_int("Enter student Age: ")
    student_department = input("Enter student Department: ")
    student_cgpa = get_valid_float("Enter student CGPA: ")

    student = {
        "id": student_id,
        "name": student_name,
        "age": student_age,
        "department": student_department,
        "cgpa": student_cgpa
    }

    return student


# Add student
def add_student():

    student_id = get_valid_int("Enter student ID: ")

    for student in students:

        if student["id"] == student_id:
            print("Student with this ID already exists.")
            return

    student = get_student_details(student_id)

    students.append(student)

    save_students()

    print("Student added successfully!")


# Search student
def search_student():

    search_id = get_valid_int("Enter the student ID to search: ")

    for student in students:

        if student["id"] == search_id:
            return student

    return None


# Update student
def update_student():

    update_id = get_valid_int("Enter the ID to update: ")

    for student in students:

        if student["id"] == update_id:

            new_id = get_valid_int("Enter new ID: ")

            for other_student in students:

                if other_student["id"] == new_id and other_student != student:
                    print("Student with this ID already exists.")
                    return

            updated_student = get_student_details(new_id)
            print("Returned from get_student_details()")
            student["id"] = updated_student["id"]
            student["name"] = updated_student["name"]
            student["age"] = updated_student["age"]
            student["department"] = updated_student["department"]
            student["cgpa"] = updated_student["cgpa"]

            save_students()

            print("Student updated successfully!")
            return

    print("Student not found.")


# Delete student
def delete_student():

    delete_id = get_valid_int("Enter ID to delete: ")

    for student in students:

        if student["id"] == delete_id:

            students.remove(student)

            save_students()

            print("Student deleted successfully!")
            return

    print("Student not found.")


# Find highest CGPA student
def highest_cgpa_student():

    if not students:
        return None

    top_student = students[0]

    for student in students:

        if student["cgpa"] > top_student["cgpa"]:
            top_student = student

    return top_student


# Sort students by CGPA
def sort_students_descending():

    students.sort(
        key=lambda student: student["cgpa"],
        reverse=True
    )

    return students


# Main menu
choice = 0


while choice != 8:

    print("\n--------Welcome-------")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Highest CGPA Student")
    print("7. Sort Students by CGPA")
    print("8. Exit")


    choice = get_valid_int("Choice: ")


    if choice == 1:

        add_student()


    elif choice == 2:

        if not students:
            print("No student records found.")

        else:
            for student in students:
                display_student(student)


    elif choice == 3:

        student = search_student()

        if student:
            print("Student Found!")
            display_student(student)

        else:
            print("Student not found.")


    elif choice == 4:

        update_student()


    elif choice == 5:

        delete_student()


    elif choice == 6:

        student = highest_cgpa_student()

        if student:
            print("Highest CGPA Student:")
            display_student(student)

        else:
            print("No student records found.")


    elif choice == 7:

        sorted_students = sort_students_descending()

        if sorted_students:

            print("Students Sorted by CGPA:")

            for student in sorted_students:
                display_student(student)

        else:
            print("No student records found.")


    elif choice == 8:

        save_students()

        print("Thank you for using Student Management System!")


    else:

        print("Invalid choice. Please try again.")