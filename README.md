**FANFIC PLATFORM**

A full-stack web application for publishing, reading, and managing fanfictions. Built with Django, this project demonstrates backend development, authentication systems, and deployment using Docker.

**LIVE DEMO**

https://fanfic-platform.onrender.com

**TECHNOLOGIES**

-Python

-Django

-Html, css, javascript

-Docker

-SQLite

**FEATURES**

-User authentication (signup/login/logout)

-Create, edit and delete fanfictions

-Chapter system with ordering

-User profile with avatar

-Like and Bookmark other people's fanfictions

-Search Funcionality

-Pagination

**RUNNING WITH DOCKER**

docker built -t fanfic-app

docker run -p 8000:8000 fanfic-app

**NSTALLATION (WITHOUT DOCKER)**

git clone https://github.com/seuusuario/fanfic-platform.git

cd fanfic-platform

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

**WHAT I LEARNED**

-Building full-stack applications with Django

-Database modeling and relationships

-Authentication systems

-Docker containerization

-Deployment workflow with Render

**FUTURE IMPROVEMENTS**

-PostgreSQL integration

-CI/CD pipeline

-Improved UI/UX

-Advanced search and filtering with explore dropdown, etc

-Adjust the inclusion of tags, fandoms and categories, as well as text boxes with bold, underline, and italics for writing fanfiction and chapters.

-Include age rating

-Implement chat, followers, profile feed and comments.

-API with Django REST Framework

**AUTHOR**

Luana
https://github.com/cypherLu
