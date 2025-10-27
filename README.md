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

44
    - `get_object_or_404`: If the object exists, it will be returned, if not, a 404 error will be returned
    - url patterns: map url to views

43
    - View for get one post is in the `blog/views.py` file > `post_detail`

42
    - Django view is a Python function that receives a web request and returns a web response
    - First view to list the posts is in the `blog/views.py` file > `post_list`

41
    - Creating model managers: whithout a custom model manager: `Post.objects.my_manager()`; with a custom model manager: `Post.my_manager.all()`

40
    - Queries with OR statments, using the Q object
    - Ex.: `from django.db.models import Q` > `Post.objects.filter(Q(title__startswith='carlo') | Q(title__startswith='example'))`

39
    - Limiting QuerySets: for see 5 first posts: `Post.objects.all()[:5]`
    - Counting objects: `Post.objects.count()`
    - Check if exists objects: `Post.objects.filter(title__startswith='carlo').exists()`
    - Deleting objects: `Post.objects.filter(title__startswith='carlo').delete()`

38
    - Excluding objects: `Post.objects.filter(publish__year=2025).exclude(title__startswith='carlo')`
    - Ordering objects: `Post.objects.order_by('publish')`

36
    - See the SQL Query for the command: `all_posts = Post.objects.all()` > `print(all_posts.query)`
    - Field lookups for filter objects. Ex.: `Post.objects.filter({id__exact=1}, {title__contains='example'}, {publish__date='2025-08-28'})`

35
    - Update a object, is necessary use the save() method before the changes
    - Ex.: `post.title = 'A totally different title'` > `post.save()`
    - Get all objects: `all_posts = Post.objects.all()`
    - See the response: `all_posts`
    - Filter objects: `Post.objects.filter(title='Example')`

34
    - Python shell: commands for get or create posts and users
    - `Post(key='value')` create a new post in memory; `Post.objects.create(key='value')` create a new post in the database
    - `get_or_create(key='value')` get the object if it exists, or create a new one if it doesn't

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
    