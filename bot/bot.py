from telegram import Bot
from dotenv import load_dotenv
import os
import requests

load_dotenv()

TG_TOKEN = os.getenv('TG_TOKEN')
DEMIAN_ID = os.getenv('DEMIAN_ID')
DB_TOKEN = os.getenv('DB_TOKEN')
HEADERS = {'Authorization': f'{DB_TOKEN}'}
ENDPOINT = 'http://db:8000/api/students/'


def send_message(bot: Bot, message, id):
    '''
    Functions for sending message to teacher at fixed time.
    '''
    bot.send_message(id, message)


def api_answer():
    response = requests.get(ENDPOINT, headers=HEADERS)
    return response.json()


def build_message(response):
    '''
    This functions parses DB response and build message for sending.
    '''
    message = ''
    for student in response:
        message += student.get('name')
        if student.get('is_late'):
            message += ' опаздывает'
    return message


def update_db(user_id, late, missing):
    '''
    This functions updates DB data on receiving message.
    '''
    ...


def main():
    '''
    Main script for running bot 24/7.
    '''
    answer = api_answer()
    print(build_message(answer))


if __name__ == '__main__':
    main()
