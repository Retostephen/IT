# IT

This repository documents my Industrial Training (SIWES) placement at
PICTDA, covering a self-paced software development curriculum built
around Python. It progresses from core language fundamentals through
object-oriented programming and into building a full web application
with Django, alongside supporting notes on networking and system
architecture concepts studied along the way.

## About

The training was structured to build up gradually: starting with basic
Python syntax and control flow, moving into functions and data
structures through a series of small applied programs (an ATM
simulation, a banking system, a library system, and others), then
introducing object-oriented programming as a bridge into Django, where
the same underlying concepts (structured data, validation, persistence)
reappear in the form of models, views, and a full authenticated CRUD
application.

Each folder below corresponds to one stage of that progression and
contains its own README with the objective, a description of what was
built, and instructions for running it.

## Contents

- `Assignment-01-Hello-World` — basic syntax and output
- `Assignment-02-Variables` — variable assignment and data types
- `Assignment-03-Input` — collecting and casting user input
- `Assignment-04-Calculator` — conditional branching with arithmetic operators
- `Assignment-05-Grading-System` — chained conditionals for grade bands
- `Assignment-06-ATM` — menu-driven loop with deposit/withdraw/balance logic
- `Assignment-07-Guessing-Game` — loops with the `random` module
- `Assignment-08-Student-Management` — functions managing a list of records
- `Assignment-09-Shopping-Cart` — dictionaries as key-value storage
- `Assignment-10-Dictionaries` — nested dictionaries and iteration
- `Assignment-11-Contact-Book` — functions for search, update, and delete
- `Assignment-12-Banking-System` — shared helper functions across operations
- `Assignment-13-Library-System` — function-based structure applied to a new domain
- `Assignment-14-Payroll` — calculations across multiple records
- `Assignment-15-Files-Handling` — reading and writing to text files
- `Assignment-16-Expense-Tracker` — persistent data storage using files
- `Assignment-17-Virtual-Environment` — `venv` and `requirements.txt`
- `Mini OOP Project` — a class-based inventory management system, consolidating earlier concepts under object-oriented design
- `Assignment-18-Django-Setup` — first Django project and app structure
- `Assignment-19-Django-Website` — multi-page site with templates and a registration form
- `Assignment-20-Django-CRUD` — capstone: authentication and full CRUD Student Management System
- `system_architechure.md` — OSI vs TCP/IP models, and the full path from a GUI click down to the kernel and back

## Running the Assignments

Each `Assignment-XX` folder is self-contained. Navigate into it and run:
```bash
python3 <script_name>.py
```
For `Assignment-17-Virtual-Environment` onward, activate a virtual
environment and install dependencies from `requirements.txt` before
running. The Django assignments (`18`–`20`) require running
`python manage.py runserver` from within their respective folders after
installing Django and applying migrations.

## Requirements

- Python 3.x
- Django (for Assignments 18–20)
- See `requirements.txt` in `Assignment-17-Virtual-Environment` for the
  full dependency list
