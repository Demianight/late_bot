FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip3 install -r bot_requirements.txt --no-cache-dir

CMD ["python3", "bot.py"]