from click import MissingParameter


release: python manage.py migrate
web: gunicorn prenatal.wagi --preload --log-file -