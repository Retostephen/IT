# Assignment 19 - Django Multi-Page Website

## Objective
Build a multi-page website using Django views, URLs, and templates.

## Description
A small Django site with four pages sharing a common navigation bar
and layout (`base.html`):
- **Home** (`/`) — welcome page
- **About** (`/about/`) — about the site
- **Contact** (`/contact/`) — contact details
- **Register** (`/register/`) — a form that saves a `Registration`
  (full name, email, department) to the database and shows a
  success message on submit

## Prerequisites
- Python 3.x installed

## How to Run
```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` and use the nav bar to move between pages.

## Repository Contents
- `manage.py`
- `config/` — project settings and URL routing
- `pages/` — the app: `models.py` (Registration model), `forms.py`,
  `views.py`, `urls.py`, `admin.py`, `migrations/`
- `templates/` — `base.html` layout + `pages/home.html`,
  `about.html`, `contact.html`, `register.html`
- `requirements.txt`, `.gitignore`

## Notes
To view saved registrations in the admin panel, create a superuser
first:
```bash
python manage.py createsuperuser
```
Then log in at `/admin/`.
