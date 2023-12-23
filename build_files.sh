command python -m venv venv
command . venv/bin/activate
command python manage.py migrate
command python manage.py runserver