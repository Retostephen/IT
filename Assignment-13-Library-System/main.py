"""
Assignment 13 - Library Management System
"""

library = {}  # title -> {"author": str, "available": bool}

while True:
    print()
    print("=" * 25)
    print("LIBRARY MANAGEMENT SYSTEM")
    print("=" * 25)
    print("1. Add Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Delete Book")
    print("5. Search Book")
    print("6. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        title = input("Enter Book Title: ").strip()
        while title == "":
            print("Title cannot be empty.")
            title = input("Enter Book Title: ").strip()

        if title in library:
            print("A book with this title already exists.")
        else:
            author = input("Enter Author: ").strip()
            while author == "":
                print("Author cannot be empty.")
                author = input("Enter Author: ").strip()

            library[title] = {"author": author, "available": True}
            print("Book Added Successfully")

    elif choice == "2":
        if not library:
            print("No books in the library.")
        else:
            title = input("Enter Book Title to borrow: ").strip()
            if title not in library:
                print("Book not found.")
            elif not library[title]["available"]:
                print("Book is currently unavailable.")
            else:
                library[title]["available"] = False
                print(f"You have borrowed '{title}'.")

    elif choice == "3":
        if not library:
            print("No books in the library.")
        else:
            title = input("Enter Book Title to return: ").strip()
            if title not in library:
                print("Book not found.")
            elif library[title]["available"]:
                print("This book was not borrowed.")
            else:
                library[title]["available"] = True
                print(f"You have returned '{title}'.")

    elif choice == "4":
        if not library:
            print("No books in the library.")
        else:
            title = input("Enter Book Title to delete: ").strip()
            if title in library:
                del library[title]
                print("Book Deleted Successfully")
            else:
                print("Book not found.")

    elif choice == "5":
        if not library:
            print("No books in the library.")
        else:
            title = input("Enter Book Title to search: ").strip()
            if title in library:
                status = "Available" if library[title]["available"] else "Borrowed"
                print(f"\nTitle: {title}")
                print(f"Author: {library[title]['author']}")
                print(f"Status: {status}")
            else:
                print("Book not found.")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
