"""
Assignment 9: Shopping Cart
"""

cart = []

def getNonEmpty(prompt):
	while True:
		value = input(prompt).strip()
		if value and any(char.isalnum() for char in value):
			return value
		print("Product name cannot be empty. Please try again.")

def addProduct():
	product = getNonEmpty("Enter Product Name: ")
	cart.append(product.lower())
	print("Product Added Successfully.")

def removeProduct():
	if not cart:
		print("Cart is empty. Nothing to remove.")
		return
	product = input("Enter product name to remove: ").strip().lower()
	if product in cart:
		cart.remove(product)
		print("Product removed successfully.")
	else:
		print("Product not found in cart.")

def viewCart():
	if not cart:
		print("Cart is empty.")
	else:
		print("\nYour Cart:")
		for i, product in enumerate(cart, 1):
			print(f"{i}, {product}")

def totalProducts():
	print(f"Toral Products in Cart: {len(cart)}")


while True:
	print()
	print("=" * 20)
	print("SHOPPING CART")
	print("=" * 20)
	print("1. Add Product")
	print("2. Remove Product")
	print("3. View Cart")
	print("4. Total Products")
	print("5. Exit")

	choice = input("Choose an option: ").strip()

	if choice == "1":
		addProduct()
	elif choice == "2":
		removeProduct()
	elif choice == "3":
		viewCart()
	elif choice == "4":
		totalProducts()
	elif choice == "5":
		print("Thank you for shopping with us.")
		break
	else:
		print("Invalid Option.")
