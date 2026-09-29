"""
Assignment 4; Simple Calculator
Build a calculator that can perform addition, subtraction, multiplication, division, modulus, power.
"""

firstInput = input("Enter first number: ")
while True:
	try:
		num1 = float(firstInput)
		break
	except ValueError:
		print("Invalid input. PLease enter a number.")
		firstInput = input("Enter first Number: ")
secondInput = (input("Enter second number: "))
while True:
	try:
		num2 = float(secondInput)
		break
	except ValueError:
		print("Invalid input. Please enter a number.")
		secondInput = input("Enter second Number: ")

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
modulus = num1 % num2 if num2 != 0 else "undefined (division by zero)"
power = num1 ** num2

if num2 != 0:
	division = num1 / num2
else:
	division = "Undefined (division by zero)"

print()
print(f"Addition: {addition:g}")
print(f"Subtraction: {subtraction:g}")
print(f"Multipliction: {multiplication}")
print(f"Division: {division if isinstance(division,str) else f"{division:g}"}")
print(f"Modulus: {modulus if isinstance(modulus,str) else f"{modulus:g}"}")
print(f"Power: {power:g}")
