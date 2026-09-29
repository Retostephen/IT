"""
Assignment 16 - Expense Tracker
Stores expenses inside a file (expenses.txt).
"""

FILE_NAME = "expenses.txt"

while True:
    print()
    print("=" * 20)
    print("EXPENSE TRACKER")
    print("=" * 20)
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        description = input("Enter Expense Description: ").strip()
        while description == "" or "," in description:
            if "," in description:
                print("Description cannot contain a comma.")
            else:
                print("Description cannot be empty.")
            description = input("Enter Expense Description: ").strip()

        amount_input = input("Enter Amount: ")
        while True:
            try:
                amount = float(amount_input)
                if amount <= 0:
                    print("Amount must be greater than zero.")
                    amount_input = input("Enter Amount: ")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")
                amount_input = input("Enter Amount: ")

        with open(FILE_NAME, "a", encoding="utf-8") as f:
            f.write(f"{description},{amount}\n")
        print("Expense Added Successfully")

    elif choice == "2":
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as f:
                lines = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            lines = []

        if not lines:
            print("No expenses found.")
        else:
            print("\nExpenses:")
            for i in range(len(lines)):
                description, amount = lines[i].split(",")
                print(f"{i + 1}. {description} - {float(amount):,.2f}")

    elif choice == "3":
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as f:
                lines = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            lines = []

        if not lines:
            print("No expenses found.")
        else:
            total = 0
            for line in lines:
                total += float(line.split(",")[1])
            print(f"Total Expenses: {total:,.2f}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
