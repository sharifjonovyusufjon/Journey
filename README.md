Run step:

1: python3 -m venv explore
2: source explore/bin/activate
3: python3 requirements.txt
0: python3 manage.py runserver

Skill:

{!}: python3 manage.py startapp travel
{!}: python3 manage.py collectstatic
{!}: python3 manage.py shell
{!}: python3 -m pip freeze > requirements.txt
{!}: python3 -m pip install Django

Create user step:

1: python3 manage.py migrate
2: python3 manage.py createsuperuser
