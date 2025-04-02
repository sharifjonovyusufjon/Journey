# Django Project

A Django-based web application for journey/travel experiences.

## Setup Instructions

### Run Step:

1. Create a virtual environment:

   ```
   python3 -m venv explore
   ```

2. Activate the virtual environment:

   ```
   source explore/bin/activate
   ```

3. Install requirements:

   ```
   python3 -m pip install -r requirements.txt
   ```

4. Start the development server:
   ```
   python3 manage.py runserver
   ```

### Create User Step:

1. Apply database migrations:

   ```
   python3 manage.py migrate
   ```

2. Create an admin superuser:
   ```
   python3 manage.py createsuperuser
   ```

## Useful Commands

```
python3 manage.py startapp travel
python3 manage.py collectstatic
python3 manage.py shell
python3 -m pip freeze > requirements.txt
python3 -m pip install Django
```
