**FANFIC PLATFORM**

A full-stack web application for publishing, reading, and managing fanfictions. Built with Django, this project demonstrates backend development, authentication systems, and deployment using Docker.

**LIVE DEMO**

https://fanfic-platform.onrender.com

**TECHNOLOGIES**

Python

Django

HTML, CSS, JavaScript

Docker

SQLite (initial version)

**FEATURES**

User authentication (signup/login)

Create, edit, and delete fanfictions

Chapter system with ordering

User profiles with avatar and bio

Like and bookmark other people's fanfics

Search functionality

Pagination

**RUNNING WITH DOCKER**

docker build -t fanfic-app .

docker run -p 8000:8000 fanfic-app

**INSTALLATION (WITHOUT DOCKER)**

git clone https://github.com/seuusuario/fanfic-platform.git

cd fanfic-platform

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

**WHAT I LEARNED**

Building full-stack applications with Django

Database modeling and relationships

Authentication systems

Docker containerization

Deployment workflow with Render

**FUTURE IMPROVEMENTS**

Chat, follow, notification

Comments in chapters

Feed in user profile

PostgreSQL integration

CI/CD pipeline

Improved UI/UX

Advanced search and filtering

API with Django REST Framework

**AUTHOR**

Luana
https://github.com/cypherLu
