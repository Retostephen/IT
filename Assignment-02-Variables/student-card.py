"""
Assignment 2: Variables
Build a student information card
"""

import datetime

fullName = "John Doe"
age = 20
department = "Computer Science"
school = "ABC University"
level = "400 Level"
state = "Plateau State"
favouriteColour = "Black"
favouriteFood = "Rice"
birthYear = 2005

print("=" * 30)
print("   STUDENT INFORMATION CARD")
print("=" * 30)
print()
print(f"Full Name: {fullName}")
print()
print(f"Age: {age}")
print()
print(f"Department: {department}")
print()
print(f"School: {school}")
print()
print(f"Level: {level}")
print()
print(f"State: {state}")
print()
print(f"Favourite Colour: {favouriteColour}")
print()
print(f"Favurite Food: {favouriteFood}")
print()

current_year = datetime.datetime.now().year
calculated_age = current_year - birthYear
print(f"Calculated Age: {calculated_age}")
