"""
Assignment 14 - Employee Payroll
"""

TAX_RATE = 0.075  # 7.5%

# Get Employee Name (cannot be empty)
employee_name = input("Enter Employee Name: ").strip()
while employee_name == "":
    print("Name cannot be empty.")
    employee_name = input("Enter Employee Name: ").strip()

# Get Salary (must be a non-negative number)
salary_input = input("Enter Salary: ")
while True:
    try:
        salary = float(salary_input)
        if salary < 0:
            print("Salary cannot be negative.")
            salary_input = input("Enter Salary: ")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a number.")
        salary_input = input("Enter Salary: ")

# Get Bonus (must be a non-negative number)
bonus_input = input("Enter Bonus: ")
while True:
    try:
        bonus = float(bonus_input)
        if bonus < 0:
            print("Bonus cannot be negative.")
            bonus_input = input("Enter Bonus: ")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a number.")
        bonus_input = input("Enter Bonus: ")

gross_salary = salary + bonus
tax = gross_salary * TAX_RATE
net_salary = gross_salary - tax

print()
print("=" * 25)
print("PAYROLL SUMMARY")
print("=" * 25)
print(f"Employee Name : {employee_name}")
print(f"Gross Salary  : {gross_salary:,.2f}")
print(f"Tax           : {tax:,.2f}")
print(f"Net Salary    : {net_salary:,.2f}")
