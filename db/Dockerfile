FROM python:3.10-slim

WORKDIR /app

COPY db_requirements.txt .

RUN pip3 install pip --upgrade

RUN pip3 install -r db_requirements.txt --no-cache-dir

COPY . .

RUN python3 manage.py makemigrations; python3 manage.py migrate; python3 manage.py loaddata fixtures.json

CMD ["gunicorn", "db.wsgi:application", "--bind", "0.0.0.0"]