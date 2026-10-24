students = {}

while True:
    print("\n--- Menu ---")
    print("A. Add a student")
    print("B. Update marks")
    print("C. Search for a student")
    print("D. Display all students and marks")
    print("E. Exit")

    choice = input("Enter your choice (A/B/C/D/E): ").strip().upper()

    if choice == 'A':
        name = input("Enter student name: ").strip()
        marks = int(input("Enter marks: "))
        students[name] = marks
        print(f"Added {name} with {marks} marks.")

    elif choice == 'B':
        name = input("Enter student name to update: ").strip()
        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
            print(f"Updated marks for {name}.")
        else:
            print("Student not found.")

    elif choice == 'C':
        name = input("Enter student name to search: ").strip()
        if name in students:
            print(f"{name}'s marks: {students[name]}")
        else:
            print("Student not found.")

    elif choice == 'D':
        if students:
            print("\nStudent Records:")
            for name, marks in students.items():
                print(f"{name}: {marks}")
        else:
            print("No records found.")

    elif choice == 'E':
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Please select A, B, C, D, or E.")