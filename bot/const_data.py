import os
from telegram import InlineKeyboardButton
from dotenv import load_dotenv


load_dotenv()


# Telegram stuff
TG_TOKEN = os.getenv('TG_TOKEN')
DEMIAN_ID = os.getenv('DEMIAN_ID')
NIKITA_ID = os.getenv('NIKITA_ID')


# Db stuff
DB_TOKEN = os.getenv('DB_TOKEN')
HEADERS = {'Authorization': f'{DB_TOKEN}'}


# Endpoints stuff
ENDPOINT = 'http://db:8000/api/students/'
# Local endpoint
# ENDPOINT = 'http://127.0.0.1:8000/api/students/'


# Bot stuff
OPINION = 'Ваше мнение очень важно для нас. Мы вам обязательно перезвоним.'

late_button = InlineKeyboardButton(
    'Я опоздаю', callback_data='Спасибо за честность'
)
passing_button = InlineKeyboardButton(
    'Я не приду', callback_data='Тебя никто не и не ждал'
)
missing_button = InlineKeyboardButton(
    'Я приду позже', callback_data='Эрик, разлогинься пж'
)
BUTTONS = [late_button, passing_button, missing_button]
