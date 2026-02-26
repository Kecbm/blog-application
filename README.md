<h1 id="top" align="center">📚 Welcome to the Blog Application Repository</h1>

<h2>Summary:</h2>

- [What was developed](#summary)
- [Technologies used](#tech)
- [Execute the project](#execute)
- [Features](#features)
- [Project structure](#structure)
- [Documentation](#doc)
- [Next Steps](#nextSteps)
- [Final considerations](#considerations)

---

<h2 id="summary">📝 What was developed</h2>

<br>

A complete **blog platform** built with **Django** and **PostgreSQL**, featuring advanced search capabilities, content management, and SEO optimization. This is a full-featured blog application with user authentication, post management, comments, tagging system, email notifications, RSS feeds, and intelligent search using trigram similarity.

Watch a complete demonstration of the application in action:

![📹 Watch the demo video.](assets/demo-blog-application.gif)

<br>

<p align="right"><a href="#top">Back to the top ☝</a></p>

---

<h2 id="tech">🛠️ Technologies used</h2>

<br>

<img title="Python" alt="Python" height="80" width="80" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" /> <img title="Django" alt="Django" height="80" width="80" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/django/django-plain.svg" /> <img title="PostgreSQL" alt="PostgreSQL" height="80" width="80" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-original.svg" /> <img title="HTML" alt="HTML" height="80" width="80" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-original.svg" /> <img title="CSS" alt="CSS" height="80" width="80" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/css3/css3-original.svg" />

<br>

<p align="right"><a href="#top">Back to the top ☝</a></p>

---

<h2 id="execute">🚀 Execute the project</h2>

<br>

**Clone the repository**

```bash
git clone https://github.com/Kecbm/blog-application.git
cd blog-application
```

<br>

**Create and activate virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

<br>

**Install dependencies**

```bash
pip install -r requiriments.txt
```

<br>

**Configure environment variables**

Create a `.env` file in the project root with the following variables:

```env
DB_NAME=blog
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
DEFAULT_FROM_EMAIL=your_email@gmail.com
```

<br>

**Apply migrations**

```bash
python manage.py migrate
```

<br>

**Create a superuser (admin account)**

```bash
python manage.py createsuperuser
```

<br>

**Start the development server**

```bash
python manage.py runserver
```

The server will be running at **http://127.0.0.1:8000/**

Access the admin panel at **http://127.0.0.1:8000/admin/**

<br>

<p align="right"><a href="#top">Back to the top ☝</a></p>

---

<h2 id="features">✨ Features</h2>

<br>

✅ **Post Management**: Create, read, update, and delete blog posts with rich content

✅ **Advanced Search**: Intelligent search using PostgreSQL trigram similarity for fuzzy matching

✅ **Comments System**: Readers can comment on posts with moderation support

✅ **Tagging System**: Organize posts with tags using django-taggit

✅ **Email Notifications**: Send post recommendations via email to readers

✅ **RSS Feed**: Syndication feed for blog content

✅ **Sitemap**: XML sitemap for SEO optimization

✅ **Pagination**: Efficient content pagination for better UX

✅ **SEO-Friendly URLs**: Clean, descriptive URLs using slug and date patterns

✅ **Admin Interface**: Comprehensive Django admin for content management

✅ **User Authentication**: Built-in user authentication and authorization

<br>

<p align="right"><a href="#top">Back to the top ☝</a></p>

---

<h2 id="structure">📁 Project structure</h2>

<br>

```
blog-application/
├── blogapplication/         # Django project configuration
│   ├── settings.py          # Project settings
│   ├── urls.py              # Main URL routing
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
├── blog/                    # Django application
│   ├── migrations/          # Database migrations
│   ├── templates/           # HTML templates
│   ├── static/              # CSS, JavaScript, images
│   ├── models.py            # Database models (Post, Comment)
│   ├── views.py             # View functions and classes
│   ├── urls.py              # App URL routing
│   ├── forms.py             # Django forms
│   ├── admin.py             # Admin configuration
│   ├── feeds.py             # RSS feed configuration
│   ├── sitemaps.py          # Sitemap configuration
│   └── tests.py             # Unit tests
├── manage.py                # Django management script
├── requiriments.txt         # Python dependencies
├── .env                     # Environment variables (not in repo)
└── README.md                # This file
```

<br>

<p align="right"><a href="#top">Back to the top ☝</a></p>

---

<h2 id="doc">📚 Documentation</h2>

<br>

<details><summary>Core Models</summary>

<h3>Post Model</h3>

The main model for blog posts with the following fields:

- **title**: Post title (CharField)
- **slug**: URL-friendly identifier (SlugField)
- **author**: Foreign key to User model
- **body**: Post content (TextField)
- **publish**: Publication date (DateTimeField)
- **created**: Creation timestamp (DateTimeField)
- **updated**: Last update timestamp (DateTimeField)
- **status**: Publication status - Draft (DF) or Published (PB) (CharField)
- **tags**: Many-to-many relationship using django-taggit

**Custom Manager**: `PublishedManager` - Returns only published posts

<h3>Comment Model</h3>

Model for post comments with the following fields:

- **post**: Foreign key to Post model
- **name**: Commenter name (CharField)
- **email**: Commenter email (EmailField)
- **body**: Comment content (TextField)
- **created**: Creation timestamp (DateTimeField)
- **updated**: Last update timestamp (DateTimeField)
- **active**: Comment status (BooleanField)

</details>

<br>

<details><summary>Advanced Search Feature</summary>

<h3>Trigram Similarity Search</h3>

The application implements PostgreSQL's `pg_trgm` extension for intelligent, fuzzy text search.

**How it works:**

A trigram is a sequence of 3 consecutive characters. The search compares trigrams between the user's query and post titles to calculate a similarity score, enabling matches even with typos or partial matches.

**Implementation:**

```python
from django.contrib.postgres.search import TrigramSimilarity

results = Post.published.annotate(
    similarity=TrigramSimilarity('title', query)
).filter(
    similarity__gt=0.1  # Threshold of 0.1
).order_by('-similarity')
```

**Features:**

- Handles typos and spelling variations
- Returns results ordered by relevance
- Configurable similarity threshold
- Efficient performance with large datasets

**Database Setup:**

The `pg_trgm` extension is automatically installed via Django migration `0005_trigram_ext.py`

</details>

<br>

<details><summary>Key Views and URLs</summary>

<h3>Main Views</h3>

- **post_list**: Display all published posts with pagination
- **post_detail**: Show individual post with comments
- **post_search**: Search posts using trigram similarity
- **post_share**: Email post recommendation form
- **CommentCreateView**: Class-based view for creating comments

<h3>URL Patterns</h3>

- `/blog/` - Post list
- `/blog/<year>/<month>/<day>/<slug>/` - Post detail (SEO-friendly)
- `/blog/search/` - Search posts
- `/blog/tag/<slug>/` - Posts by tag
- `/blog/feed/` - RSS feed
- `/sitemap.xml` - XML sitemap

</details>

<br>

<p align="right"><a href="#top">Back to the top ☝</a></p>

---

<h2 id="nextSteps">🎯 Next Steps</h2>

<br>

Future enhancements and features to be implemented:

<br>

- [ ] Build a modern frontend with React or Vue.js
- [ ] Implement user profiles and author pages
- [ ] Add social media sharing buttons
- [ ] Develop a REST API with Django REST Framework
- [ ] Implement full-text search with Elasticsearch
- [ ] Add image optimization and lazy loading
- [ ] Create a newsletter subscription system
- [ ] Implement analytics and view tracking
- [ ] Add dark mode support
- [ ] Deploy to production (Docker, AWS, Heroku)
- [ ] Implement caching strategies (Redis)
- [ ] Add automated testing and CI/CD pipeline
- [ ] Develop mobile-responsive design improvements
- [ ] Implement comment threading and nested replies

<br>

<p align="right"><a href="#top">Back to the top ☝</a></p>

---

<h2 id="considerations">💡 Final considerations</h2>

<br>

This blog application represents a complete learning journey through Django's core concepts and advanced features. From basic CRUD operations to sophisticated search algorithms, the project demonstrates professional development practices.

<h3>Key Learnings</h3>

- **Django ORM**: Efficient database queries and model relationships
- **PostgreSQL Integration**: Leveraging database-specific features like trigram search
- **Content Management**: Building scalable content systems with proper status management
- **SEO Optimization**: Implementing clean URLs, sitemaps, and RSS feeds
- **User Experience**: Pagination, search functionality, and email notifications
- **Code Organization**: Modular architecture with proper separation of concerns

<h3>Technology Choices</h3>

The selection of PostgreSQL with trigram similarity over traditional full-text search provides:

- **Flexibility**: Works with any text field without special indexing
- **Accuracy**: Handles typos and partial matches naturally
- **Performance**: Optimized C implementation in PostgreSQL
- **Simplicity**: Native Django ORM integration without external dependencies

<br>

<p align="right"><a href="#top">Back to the top ☝</a></p>

---

<p align="center">Project developed by <a href="https://www.linkedin.com/in/kecbm/">Klecianny Melo</a> 😁</p>
    