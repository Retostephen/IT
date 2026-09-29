# Assignment 18 - Django Installation

## Objective
Set up your first Django project.

## Description
A bare Django project (`config`) created with `django-admin
startproject`, ready to build on in later assignments.

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
Visit `http://127.0.0.1:8000/` to see the default Django welcome page.

## Repository Contents
- `manage.py`
- `config/` — project settings, URLs, WSGI/ASGI entry points
- `requirements.txt`
- `.gitignore`
