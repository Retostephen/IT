"""
Assignment 12 - Banking Application
Uses Functions, Loops, and Conditions.
"""

accounts = {
    "John": 50000,
    "Mary": 30000,
}


def get_valid_amount(prompt):
    while True:
        value = input(prompt)
        try:
            amount = float(value)
        except ValueError:
            print("Invalid input. Please enter a numeric amount.")
            continue
        if amount <= 0:
            print("Amount must be greater than zero.")
            continue
        return amount


def get_existing_account(prompt):
    while True:
        name = input(prompt).strip()
        if name in accounts:
            return name
        print("Account not found. Please enter a valid account name.")


def deposit():
    name = get_existing_account("Enter account name: ")
    amount = get_valid_amount("Enter deposit amount: ")
    accounts[name] += amount
    print(f"Deposit successful. New balance: {accounts[name]}")


def withdraw():
    name = get_existing_account("Enter account name: ")
    amount = get_valid_amount("Enter withdrawal amount: ")
    if amount > accounts[name]:
        print("Insufficient funds.")
    else:
        accounts[name] -= amount
        print(f"Withdrawal successful. New balance: {accounts[name]}")


def check_balance():
    name = get_existing_account("Enter account name: ")
    print(f"Balance for {name}: {accounts[name]}")


def transfer():
    sender = get_existing_account("Enter sender account name: ")
    while True:
        receiver = input("Enter receiver account name: ").strip()
        if receiver not in accounts:
            print("Account not found. Please enter a valid account name.")
        elif receiver == sender:
            print("Sender and receiver cannot be the same account.")
        else:
            break
    amount = get_valid_amount("Enter transfer amount: ")
    if amount > accounts[sender]:
        print("Insufficient funds.")
    else:
        accounts[sender] -= amount
        accounts[receiver] += amount
        print(f"Transfer successful. {sender}'s new balance: {accounts[sender]}")


def main():
    while True:
        print()
        print("=" * 22)
        print("BANKING APPLICATION")
        print("=" * 22)
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance")
        print("4. Transfer")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            deposit()
        elif choice == "2":
            withdraw()
        elif choice == "3":
            check_balance()
        elif choice == "4":
            transfer()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
