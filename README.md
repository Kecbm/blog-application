# Blog Application

This is a blog application created with Django.

# Structure

**blogapplication**: is a Django project

**blog**: is a Django application

## Commands

- Create virtual environment: `python -m venv venv`
- Activate virtual environment: `source venv/bin/activate`
- Deactivate virtual environment: `deactivate`
- Install requirements: `pip install -r requiriments.txt`
- Apply migrations: `python manage.py migrate`

- Start the server: `python manage.py runserver`
    - The server it willbe running in the url: http://127.0.0.1:8000/

- Create an application: `python manage.py startapp blog`

## Annotations

### Chapter 1

Page 14
    - Init the application Blog creating a POST model
    - A model when conect in a data base, will be create a db table, with the same fields
    