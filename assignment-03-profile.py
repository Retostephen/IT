"""
Assignment 3: User Input
Student Registeration System
"""

name = input("Enter Name: ").strip()
while name == "":
	print("Name cannot be empty.")
	name = input("Enter Name: ").strip()
age = input("Enter your age (They must be integers): ").strip()
while not age.isdigit() or int(age) <= 0 or int(age) > 119:
	print("Invalid age. Please enter a whole number between 1 and 119.")
	age = input("Enter your age: ").strip()
department = input("Enter your Department: ").strip()
while department == "":
	print("Department cannot be empty.")
	department = input("Enter your department: ").strip()
email = input("Enter your Email: ").strip()
while "@" not in email or "." not in email.split("@")[-1] or email.startswith("@") or email.endswith("@"):
	print("Invalid email. Example: name@example.com")
	email = input("Enter email: ").strip()
phoneNumber = input("Enter your Phone Number: ").strip()
while not phoneNumber.isdigit() or len(phoneNumber) < 11 or len(phoneNumber) > 13:
	print("Invalid phone number. Digits only, 11-13(+234) digits.")
	phoneNumber = input("Enter your Phone Number: ").strip()
school = input("Enter name of school: ").strip()
while school == "":
	print("School cannot be empty.")
	school = input("Enter School: ").strip()

print()
print("=" * 26)
print("STUDENT REGISTERATION")
print("=" * 26)
print()
print(f"Welcome {name}")
print()
print("You have successfully regisetred.")
print()
print("Department:")
print(department)
print()
print("Email:")
print(email)

