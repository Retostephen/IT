"""
Assinment 8: Student Management System
Using Lists
"""

students = []

def getNonEmpty(prompt):
	while True:
		value = input(prompt).strip()
		if value:
			return value
		print("Name cannot be empty. Please try again.")

def addStudent():
	name = getNonEmpty("Enter Students Name: ")
	if name.lower() in [s.lower() for s in students]:
		print("Student already exists.")
		return
	students.append(name)
	print("Student added Successfully")

def removeStudent():
	if not students:
		print("No students to remove.")
		return
	name = input("Enter students name to remove: ").strip()
	if name in students:
		students.remove(name)
		print("Student removed successsfully.")
	else:
		print("Student not found.")
	
def viewStudents():
	if not students:
		print("No students yet.")
	else:
		print("\nStudent List:")
		for i, student in enumerate(students, 1):
			print(f"{i}, {student}")
	
def countStudents():
	print(f"Total Students: {len(students)}")

while True:
	print()
	print("=" * 25)
	print("STUDENT MANAGEMENT SYSTEM")
	print("=" * 25)	
	print("1. Add Student")
	print("2. Remove Student")
	print("3. View Students")
	print("4. Count Students")
	print("5. Exit")


	choice = input("Choose an option: ").strip()

	if choice == "1":
		addStudent()
	elif choice == "2":
		removeStudent()
	elif choice == "3":
		viewStudents()
	elif choice == "4":
		countStudents()
	elif choice == "5":
		print("Goodbye.")
		break
	else:
		print("Invalid option.")
