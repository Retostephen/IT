"""
Assignment 6: ATM Machine
"""

balance = 100000

while True:
	print()
	print("=" * 20)
	print("ATM MENU")
	print("=" * 20)
	print()
	print("1. Check Balance")
	print("2. Deposit")
	print("3. Withdraw")
	print("4. Exit")

	choice = input("Choose an option(1-4): ")

	if choice == "1":
		print(f"Your balance is {balance}")
	elif choice == "2":
		amountInput = input("Enter amount to deposit: ")
		while True:
			try:
				amount = float(amountInput)
				if amount <= 0:
					print("Amount must be greater than zero.")
					amountInput = input("Enter amount to deposit: ")
				else:
					break
			except ValueError:
				print("Invalid input. Please enter a number.")
				amountInput = input("Enter amount to deposit: ")
		balance += amount
		print(f"Deposit successful. New balance: {balance}")
	elif choice == "3":
		amountInput = input("Enter amount to withdraw: ")
		while True:
			try:
				amount = float(amountInput)
				if amount <= 0:
					print("Invalid Amount to Withdraw. Amount must be greater than Zero.")
					amountInput = input("Enter amount to withdraw: ")
				else:
					break
			except ValueError:
				print("Invalid input. Please enter a number.")
				amountInput = input("Enter amount to withdraw")
		if balance < amount:
			print("Insufficient Funds")
		else:
			balance -= amount
			print(f"Withdrawal successful. New Balance: {balance}")
	elif choice == "4":
		print("Thank you for banking with us")
		break
	else:
		print("Invalid option. Choose between 1-4.")
