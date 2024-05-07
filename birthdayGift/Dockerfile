from python:3.10

env pythonunbuffered=1

workir /code

copy requirements.txt

run pip install -r requirements.txt

copy . .requirements

expose 8000

cmd ["python", "manage.py", "runserver"]