# Student Management System using CRUD operations

students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    if roll in students:
        print("Student already exists!")
        return
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    students[roll] = {"name": name, "marks": marks}
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students found.")
        return
    for roll, data in students.items():
        print(f"Roll: {roll}, Name: {data['name']}, Marks: {data['marks']}")

def update_student():
    roll = input("Enter Roll Number to update: ")
    if roll not in students:
        print("Student not found.")
        return
    name = input("Enter new Name: ")
    marks = input("Enter new Marks: ")
    students[roll] = {"name": name, "marks": marks}
    print("Student updated successfully!")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    if roll in students:
        del students[roll]
        print("Student deleted successfully!")
    else:
        print("Student not found.")

def menu():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Thank you!")
            break
        else:
            print("Invalid choice!")

menu()
