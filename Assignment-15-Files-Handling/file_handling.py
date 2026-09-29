"""
Assignment 15 - File Handling
Stores student records inside students.txt
"""

FILE_NAME = "students.txt"

while True:
    print()
    print("=" * 20)
    print("FILE HANDLING")
    print("=" * 20)
    print("1. Add Student")
    print("2. Read Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        name = input("Enter Student Name: ").strip()
        while name == "":
            print("Name cannot be empty.")
            name = input("Enter Student Name: ").strip()

        with open(FILE_NAME, "a", encoding="utf-8") as f:
            f.write(name + "\n")
        print("Student Added Successfully")

    elif choice == "2":
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as f:
                lines = [line.strip() for line in f if line.strip()]
            if not lines:
                print("No students found.")
            else:
                print("\nStudent List:")
                for i in range(len(lines)):
                    print(f"{i + 1}. {lines[i]}")
        except FileNotFoundError:
            print("No students found. File does not exist yet.")

    elif choice == "3":
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as f:
                lines = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            lines = []

        if not lines:
            print("No students found.")
        else:
            name = input("Enter Student Name to delete: ").strip()
            if name not in lines:
                print("Student not found.")
            else:
                lines.remove(name)
                with open(FILE_NAME, "w", encoding="utf-8") as f:
                    for line in lines:
                        f.write(line + "\n")
                print("Student Deleted Successfully")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
