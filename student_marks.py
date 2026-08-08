list=[]
students = {}

while True:
    print("\n\n\n\nStudent Marks Management System")
    print("1. Add Student")
    print("2. Edit Marks")
    print("3. Delete Student")
    print("4. View Students")
    print("5. Exit")

    choice = input("please make choice 1/2/3/4/5: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        list.append({name: marks})
        print("Student added successfully.")

    elif choice == "2":
        name = input("Enter student name to edit: ")
        if name in students:
            new_marks = int(input("Enter new marks: "))
            students[name] = new_marks
            print("Marks updated successfully.")
        else:
            print("Student not found.")

    elif choice == "3":
        name = input("Enter student name to delete: ")
        if name in students:
            del students[name]
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    elif choice == "4":
        if students:
            print("\nStudent Marks are:")
            for name, marks in students.items():
                print(f"{name}: {marks}")
        else:
            print("No students records found.")

    elif choice == "5":
        break

    else:
        print("Invalid choice. Try again.")