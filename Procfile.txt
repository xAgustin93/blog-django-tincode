release: python manage.py migrate
web: gunicorn blog.wsgi