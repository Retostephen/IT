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

	choice = int(input("Choose an option(1-4): "))

	if choice == 1:
		print(f"Your balance is {balance}")
	elif choice == 2:
		amount = float(input("Enter amount to deposit: "))
		if amount <= 0:
			print("Invalid Amount to Deposit")
		else:
			balance += amount
			print(f"Deposit successful. New balance: {balance}")
	elif choice == 3:
		amount = float(input("Enter amount to withdraw: "))
		if amount <= 0:
			print("Invalid Amount to Withdraw")
		elif balance < amount:
			print("Insufficient Funds")
		else:
			balance -= amount
			print(f"Withdrawal successful. New Balance: {balance}")
	elif choice == 4:
		print("Thank you for banking with us")
		break
	else:
		print("Invalid option. Choose between 1-4.")
