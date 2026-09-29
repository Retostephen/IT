"""
Assignment 11 - Contact Book
Store contacts using dictionaries.
"""

contacts = {}

while True:
    print()
    print("=" * 20)
    print("CONTACT BOOK")
    print("=" * 20)
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View Contacts")
    print("5. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        name = input("Enter Contact Name: ").strip()
        while name == "":
            print("Name cannot be empty.")
            name = input("Enter Contact Name: ").strip()

        phone = input("Enter Phone Number: ").strip()
        while not phone.isdigit() or len(phone) < 7 or len(phone) > 15:
            print("Invalid phone number. Digits only, 7-15 digits.")
            phone = input("Enter Phone Number: ").strip()

        email = input("Enter Email: ").strip()
        while "@" not in email or "." not in email.split("@")[-1] or email.startswith("@") or email.endswith("@"):
            print("Invalid email. Example: name@example.com")
            email = input("Enter Email: ").strip()

        contacts[name] = {"Phone": phone, "Email": email}
        print("Contact Added Successfully")

    elif choice == "2":
        if not contacts:
            print("No contacts saved.")
        else:
            name = input("Enter Contact Name to search: ").strip()
            if name in contacts:
                info = contacts[name]
                print(f"\nName: {name}")
                print(f"Phone: {info['Phone']}")
                print(f"Email: {info['Email']}")
            else:
                print("Contact not found.")

    elif choice == "3":
        if not contacts:
            print("No contacts saved.")
        else:
            name = input("Enter Contact Name to delete: ").strip()
            if name in contacts:
                del contacts[name]
                print("Contact Deleted Successfully")
            else:
                print("Contact not found.")

    elif choice == "4":
        if not contacts:
            print("No contacts saved.")
        else:
            print("\nAll Contacts:")
            for name in contacts:
                print(f"- {name}: {contacts[name]['Phone']}, {contacts[name]['Email']}")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
