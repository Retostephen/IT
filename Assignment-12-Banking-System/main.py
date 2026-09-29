"""
Assignment 12 - Banking Application
Uses Functions, Loops, Conditions, and JSON File Storage.
"""

import json
import os
import random


FILE_NAME = "accounts.json"



def load_accounts():
    if not os.path.exists(FILE_NAME):
        return {}

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {}



def save_accounts():
    with open(FILE_NAME, "w") as file:
        json.dump(accounts, file, indent=4)



def generate_account_number():
    while True:
        account_number = str(random.randint(1000000000, 9999999999))

        if account_number not in accounts:
            return account_number



def get_valid_amount(prompt):
    while True:
        value = input(prompt).strip()

        try:
            amount = float(value)
        except ValueError:
            print("Invalid input. Please enter a numeric amount.")
            continue

        if amount <= 0:
            print("Amount must be greater than zero.")
            continue

        return amount



def get_pin():
    while True:
        pin = input("Create a 4-digit PIN: ").strip()

        if len(pin) != 4 or not pin.isdigit():
            print("PIN must be exactly 4 digits.")
            continue

        return pin



def create_account():
    print()
    print("=" * 22)
    print("CREATE ACCOUNT")
    print("=" * 22)

    while True:
        name = input("Enter your full name: ").strip()

        if name == "":
            print("Name cannot be empty.")
        else:
            break

    pin = get_pin()
    initial_deposit = get_valid_amount("Enter initial deposit: ₦")

    account_number = generate_account_number()

    accounts[account_number] = {
        "name": name,
        "pin": pin,
        "balance": initial_deposit
    }

    save_accounts()

    print()
    print("Account created successfully!")
    print(f"Account holder: {name}")
    print(f"Your account number is: {account_number}")
    print(f"Your balance is: ₦{initial_deposit:,.2f}")
    print("Please keep your account number safe.")



def login():
    while True:
        account_number = input("Enter account number: ").strip()

        if len(account_number) != 10 or not account_number.isdigit():
            print("Account number must be exactly 10 digits.")
            continue

        if account_number not in accounts:
            print("Account not found.")
            return None

        pin = input("Enter PIN: ").strip()

        if accounts[account_number]["pin"] != pin:
            print("Incorrect PIN.")
            return None

        return account_number



def deposit():
    account_number = login()

    if account_number is None:
        return

    amount = get_valid_amount("Enter deposit amount: ₦")

    accounts[account_number]["balance"] += amount

    save_accounts()

    balance = accounts[account_number]["balance"]

    print()
    print("Deposit successful.")
    print(f"New balance: ₦{balance:,.2f}")



def withdraw():
    account_number = login()

    if account_number is None:
        return

    amount = get_valid_amount("Enter withdrawal amount: ₦")

    balance = accounts[account_number]["balance"]

    if amount > balance:
        print("Insufficient funds.")
        return

    accounts[account_number]["balance"] -= amount

    save_accounts()

    new_balance = accounts[account_number]["balance"]

    print()
    print("Withdrawal successful.")
    print(f"New balance: ₦{new_balance:,.2f}")



def check_balance():
    account_number = login()

    if account_number is None:
        return

    name = accounts[account_number]["name"]
    balance = accounts[account_number]["balance"]

    print()
    print(f"Account holder: {name}")
    print(f"Account number: {account_number}")
    print(f"Balance: ₦{balance:,.2f}")



def transfer():
    sender = login()

    if sender is None:
        return

    while True:
        receiver = input("Enter receiver's account number: ").strip()

        if len(receiver) != 10 or not receiver.isdigit():
            print("Account number must be exactly 10 digits.")
            continue

        if receiver not in accounts:
            print("Receiver account not found.")
            return

        if receiver == sender:
            print("You cannot transfer money to yourself.")
            return

        break

    amount = get_valid_amount("Enter transfer amount: ₦")

    if amount > accounts[sender]["balance"]:
        print("Insufficient funds.")
        return

    accounts[sender]["balance"] -= amount
    accounts[receiver]["balance"] += amount

    save_accounts()

    print()
    print("Transfer successful.")
    print(f"Amount transferred: ₦{amount:,.2f}")
    print(
        f"Your new balance: "
        f"₦{accounts[sender]['balance']:,.2f}"
    )



def main():
    global accounts

    accounts = load_accounts()

    while True:
        print()
        print("=" * 30)
        print("       BANKING APPLICATION")
        print("=" * 30)
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transfer")
        print("6. Exit")
        print("=" * 30)

        choice = input("Choose an option: ").strip()

        if choice == "1":
            create_account()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            check_balance()

        elif choice == "5":
            transfer()

        elif choice == "6":
            print("Thank you for using our banking application.")
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose between 1 and 6.")


if __name__ == "__main__":
    main()
