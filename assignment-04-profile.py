"""
Assignment 4; Simple Calculator
Build a calculator that can perform addition, subtraction, multiplication, division, modulus, power.
"""

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

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
