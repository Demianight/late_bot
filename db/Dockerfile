FROM python:3.10-slim

WORKDIR /app

COPY db_requirements.txt .

RUN pip3 install -r db_requirements.txt --no-cache-dir

COPY . .

RUN ls -a

RUN python3 manage.py makemigrations; python3 manage.py migrate

CMD ["gunicorn", "db.wsgi:application", "--bind", "0:8000" ]