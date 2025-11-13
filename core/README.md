✅ Django CRUD – Step-by-Step Roadmap (Beginner Friendly)

This guide explains how to build a Django CRUD project from zero using SQLite3.
All code files are accessible through GitHub links below.

🚀 Project Setup
1) Create main folder
PS C:\Users\Alvin\Desktop\CRUD-roadmap> mkdir core
PS C:\Users\Alvin\Desktop\CRUD-roadmap> cd .\core\

2) Create and activate virtual environment
PS C:\Users\Alvin\Desktop\CRUD-roadmap\core> python -m venv .venv
PS C:\Users\Alvin\Desktop\CRUD-roadmap\core> .venv\Scripts\activate

3) Install Django
PS C:\Users\Alvin\Desktop\CRUD-roadmap\core> pip install Django

4) Create Django project
PS C:\Users\Alvin\Desktop\CRUD-roadmap\core> django-admin startproject core .

5) Create app (home)
PS C:\Users\Alvin\Desktop\CRUD-roadmap\core> python manage.py startapp home

6) Test run (optional)
PS C:\Users\Alvin\Desktop\CRUD-roadmap\core> python manage.py runserver

✅ Step-1 — Add App to INSTALLED_APPS

core/core/settings.py:
🔗 https://github.com/elvin-babanli/Django-CRUD/blob/main/core/core/settings.py

Add:
'home',

✅ Step-2 — Database & Model
Run initial migration
PS C:\Users\Alvin\Desktop\CRUD-roadmap\core> python manage.py migrate

Model file

core/home/models.py:
🔗 https://github.com/elvin-babanli/Django-CRUD/blob/main/core/home/models.py

Make migrations
PS C:\Users\Alvin\Desktop\CRUD-roadmap\core> python manage.py makemigrations
PS C:\Users\Alvin\Desktop\CRUD-roadmap\core> python manage.py migrate

✅ Step-3 — Create Superuser
PS C:\Users\Alvin\Desktop\CRUD-roadmap\core> python manage.py createsuperuser


Admin registration file:
🔗 https://github.com/elvin-babanli/Django-CRUD/blob/main/core/home/admin.py

✅ Step-4 — Add URLs
Project URLs

core/core/urls.py:
🔗 https://github.com/elvin-babanli/Django-CRUD/blob/main/core/core/urls.py

App URLs

core/home/urls.py:
🔗 https://github.com/elvin-babanli/Django-CRUD/blob/main/core/home/urls.py

✅ Step-5 — Templates & Static

Templates:

base.html
🔗 https://github.com/elvin-babanli/Django-CRUD/blob/main/core/home/templates/base.html

index.html
🔗 https://github.com/elvin-babanli/Django-CRUD/blob/main/core/home/templates/index.html

data.html
🔗 https://github.com/elvin-babanli/Django-CRUD/blob/main/core/home/templates/data.html

update.html
🔗 https://github.com/elvin-babanli/Django-CRUD/blob/main/core/home/templates/update.html

Static file:

styless.css
🔗 https://github.com/elvin-babanli/Django-CRUD/blob/main/core/home/static/styless.css

✅ Step-6 — CRUD Logic (Views)

core/home/views.py:
🔗 https://github.com/elvin-babanli/Django-CRUD/blob/main/core/home/views.py

✅ Step-7 — Bootstrap Templates (Optional)

Docs:
https://getbootstrap.com/

✅ Step-8 — Run & Test Project
Start server:
PS C:\Users\Alvin\Desktop\CRUD-roadmap\core> python manage.py runserver

Check SQLite DB:

https://sqliteviewer.app/

🎉 Project Completed

You now have a fully working Django CRUD application.
