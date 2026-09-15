"""
Assignment 10 - Dictionary
Create a mini database.
"""

import re

database = {}

def getNonEmpty(prompt):
	while True:
		value = input(prompt).strip()
		if value:
			return value
		print("This field cannot be empty. Please try again.")

def getValidAge(prompt):
	while True:
		value = input(prompt).strip()
		if value.isdigit() and 0 < int(value) < 120:
			return value
		print("Invalid age. Please enter a whole number between 1 and 119.")

def getValidEmail(prompt):
	pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
	while True:
		value = input(prompt).strip()
		if re.match(pattern, value):
			return value
		print("Invalid email format. Example: name@example.com")

def getValidPhone(prompt):
	while True:
		value = input(prompt).strip()
		if value.isdigit() and 7 <= len(value) <= 15:
			return value
		print("Invalid phone number.")

def addStudent():
	name = getNonEmpty("Enter Student name: ")
	age = getValidAge("Enter your age: ")
	course = getNonEmpty("Enter your course: ")
	phone = getValidPhone("Enter Phone: ")
	email = getValidEmail("Enter Email: ")


	database[name] = {
		"Age": age,
		"Course": course,
		"Phone": phone,
		"Email": email,
	}
	print("Student Added Successfully.")

def retrieveStudent():
	if not database:
		print("Database is empty.")
		return
	name = input("Enter Student Name: ").strip().lower()
	if name.lower() in database:
		info = database[name]
		print(f"Name: {name}")
		print(f"Age: {info['Age']}")
		print(f"Course: {info['Course']}")
		print(f"Phone: {info['Phone']}")
		print(f"Email: {info['Email']}")
	else:
		print("Student not found.")

while True:
	print()
	print("=" * 20)
	print("MINI DATABASE")
	print("=" * 20)
	print("\n1. Add Student")
	print("2. Retrieve Student")
	print("3. Exit")

	choice = input("Choose an option: ").strip()
	if choice == "1":
		addStudent()
	elif choice == "2":
		retrieveStudent()
	elif choice == "3":
		print("Goodbye.")
		break
	else:
		print("Invalid option.Choose between 1-3")
