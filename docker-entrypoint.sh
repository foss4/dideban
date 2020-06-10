python manage.py migrate
gunicorn -c gunicorn_conf.py config.wsgi:application