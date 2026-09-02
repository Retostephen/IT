"""
Assignment 5: Student Result Checker
"""

name = input("Enter Name: ")
score = float(input("Enter Score: "))

if 70 <= score <= 100:
	remark = "Excellent"
	grade = "A"
elif 60 <= score <=69:
	remark = "Very Good"
	grade = "B"
elif 50 <= score <= 59:
	remark = "Good"
	grade = "C"
elif 45 <= score <= 49:
	remark = "Pass"
	grade = "D"
elif 40 <= score <= 44:
	remark = "Pass"
	grade = "E"
elif score <= 39:
	remark = "Fail"
	grade = "F"
else:
	"Invalid Score"
print()
print("Name: " ,name)
print()
print("Score:" ,score)
print()
print("Grade: " ,grade)
print()
print("Remark: ",remark)
print()

if score >= 40:
	print("Congratulations")
else:
	print("Better Luck Next Time") 
