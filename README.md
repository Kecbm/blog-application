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

- Enter in the shell: `python manage.py shell`

- Initial migration for Post model: `python manage.py makemigrations blog`
- See the SQL for the migration: `python manage.py sqlmigrate blog 0001`

- Create a superuser: `python manage.py createsuperuser`
- kleciannymelo
- Senha: my cell phone of Vivo
- Email: kleciannymelo@gmail.com

- Django administration site: http://127.0.0.1:8000/admin/

## Annotations

### Chapter 1

34
    - Python shell: commands for get or create posts and users

32
    - Facet filters are counters of show how many objects exist for each filter option in the admin site

30
    - Define configurations for customizing how models are displayed on the admin site
    - It is possible define filters, search fields, prepopulated fields, raw id fields, date hierarchy and ordering

28
    - It is possible add a model in the Django admin site, when you register the model in the admin.py file
    - After this registration, the django admin site will show a new section for this model and will be possible make the CRUD of the objects for this model

25
    - Each new model file will have a new migration file because with this, Django will be able to track the changes in the models and apply them to the database

24
    - The migration initial for the Post model, contains the SQL for create the table in the database and the index for the publish field

23
    - The on_delete parameter is used to delete the related objects when the parent object is deleted
    - The related_name parameter is used to access the related objects from the parent object
    - After create a model, is necessary to create the corresponding database table
    - Django have a migration system to get a changes in the models and apply them to the database

18
    - The indexes get to the database more efficient queries
    - Whithout indexes, the database will have to scan all the rows to find the data

14
    - Init the application Blog creating a POST model
    - A model when conect in a database, will be create a db table, with the same fields
    