"""
Assignment 10 - Dictionary
Create a mini database.
"""

database = {}

while True:
    print()
    print("=" * 20)
    print("MINI DATABASE")
    print("=" * 20)
    print("1. Add Student")
    print("2. Retrieve Student")
    print("3. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        name = input("Enter Student Name: ").strip()
        while name == "":
            print("Name cannot be empty.")
            name = input("Enter Student Name: ").strip()

        age = input("Enter Age: ").strip()
        while not age.isdigit() or int(age) <= 0 or int(age) > 119:
            print("Invalid age. Please enter a whole number between 1 and 119.")
            age = input("Enter Age: ").strip()

        course = input("Enter Course: ").strip()
        while course == "":
            print("Course cannot be empty.")
            course = input("Enter Course: ").strip()

        phone = input("Enter Phone: ").strip()
        while not phone.isdigit() or len(phone) < 7 or len(phone) > 15:
            print("Invalid phone number. Digits only, 7-15 digits.")
            phone = input("Enter Phone: ").strip()

        email = input("Enter Email: ").strip()
        while "@" not in email or "." not in email.split("@")[-1] or email.startswith("@") or email.endswith("@"):
            print("Invalid email. Example: name@example.com")
            email = input("Enter Email: ").strip()

        database[name] = {
            "Age": age,
            "Course": course,
            "Phone": phone,
            "Email": email,
        }
        print("Student Added Successfully")

    elif choice == "2":
        if not database:
            print("Database is empty.")
        else:
            name = input("Enter Student Name\n").strip()
            if name in database:
                info = database[name]
                print(f"\nName : {name}")
                print(f"Age : {info['Age']}")
                print(f"Course : {info['Course']}")
                print(f"Phone : {info['Phone']}")
                print(f"Email : {info['Email']}")
            else:
                print("Student not found.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
