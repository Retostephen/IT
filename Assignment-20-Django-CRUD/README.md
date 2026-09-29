# Assignment 20 - Capstone: Student Management System (CRUD)

## Objective
Build a full CRUD web application in Django, bringing together
models, forms, authentication, and templates styled with Bootstrap.

## Description
A login-protected Student Management System:
- **Sign Up / Login / Logout** — using Django's built-in auth system
- **Dashboard** — lists all students, shows total count, supports
  search by name
- **Add Student** — form to create a new student record
- **View Student** — detail page for a single student
- **Edit Student** — update an existing record
- **Delete Student** — confirmation page before removing a record
- **Admin Panel** — students are registered in Django admin with
  search and filters

Every page except Login/Sign Up requires authentication — anonymous
users are redirected to the login page.

## Data Model
`Student`: full_name, email (unique), department, level (100-400,
dropdown), phone_number, created_at, updated_at.

## Prerequisites
- Python 3.x installed

## How to Run
```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser   # optional, for /admin/
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` — you'll be redirected to `/login/`.
Click "Sign up" to create an account, or log in with a superuser.

## Repository Contents
- `manage.py`
- `config/` — project settings and URL routing (SQLite by default)
- `students/` — the app: `models.py`, `forms.py`, `views.py`,
  `urls.py`, `admin.py`, `migrations/`
- `templates/` — `base.html` (Bootstrap layout with nav + logout) and
  `students/` templates for login, signup, dashboard, add/edit form,
  detail, and delete confirmation
- `requirements.txt`, `.gitignore`

## Notes
- Bootstrap 5 is loaded via CDN in `base.html` — no separate install needed.
- Search on the dashboard filters by name using `?q=<term>` in the URL.
- All create/update forms use Django's `ModelForm` for built-in validation
  (e.g. required fields, unique email, valid email format).
