
### this repo help me create django projects faster by offering an accounts application

### follow theese steps to create django project faster:
- python3.8 -m venv <project-name-env>
- cd <project-name-env>
- source bin/activate
- copy the pre-built 'djangoproject' inside <project-name-env>
- cd djangoproject
- python -m pip install -r requirements.txt
- python manage.py makemgirations accounts
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver

