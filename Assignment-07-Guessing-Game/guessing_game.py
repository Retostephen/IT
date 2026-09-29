"""
Assignment 7: Number Guessing Game
"""
import random

secretNumber =  random.randint(1, 100)
maxAttempts = 5

print("I'm having the thought of a number between 1 - 100")
print("You have {maxAttempts} attempts to guess it.")

for attempt in range (1, maxAttempts + 1):
	guess = int(input(f"\nAttempt {attempt}/{maxAttempts} - Enter your guess: "))

	if guess < secretNumber:
		print("Too Low")
	elif guess > secretNumber:
		print("Too High")
	else:
		print("Correct!")
else:
	print(f"\nOut of attempts! The number was {secretNumber}.")
