from telegram import Bot, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv
import os
import requests
from rest_framework.response import Response


load_dotenv()

TG_TOKEN = os.getenv('TG_TOKEN')
DEMIAN_ID = os.getenv('DEMIAN_ID')
NIKITA_ID = os.getenv('NIKITA_ID')
DB_TOKEN = os.getenv('DB_TOKEN')
HEADERS = {'Authorization': f'{DB_TOKEN}'}
ENDPOINT = 'http://db:8000/api/students/'

updater = Updater(token=TG_TOKEN)


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
        lesson = student.get('is_missing') 
        if lesson != 0:
            message += f' придет к {lesson} уроку.'
        if student.get('is_passing'):
            message += ' не изволит явиться.'
    return message


def update_db(student_id, late, missing):
    '''
    This functions updates DB data on receiving message.
    '''
    data = {
        'is_late': late,
        'is_missing': missing
    }
    requests.patch(
        url=ENDPOINT + f'{student_id}/',
        data=data,
    )

def send_data(bot: Bot, update):
    
    opinion = 'Ваше мнение очень важно для нас. Мы вам обязательно перезвоним.'
    bot.send_message(
        'Привет, почетный огурец! Команды: Я опоздаю, если ты опоздаешь; Я не приду, если ты ленивая попа, Я приду позже, если ты Эрик'
    )
    late_button = InlineKeyboardButton('Я опоздаю', callback_data='Спасибо за честность')
    passing_button = InlineKeyboardButton('Я не приду', callback_data='Тебя никто не и не ждал')
    missing_button = InlineKeyboardButton('Я приду позже', callback_data='Эрик, разлогинься пж')
    buttons = [late_button, passing_button, missing_button]
    

    for button in buttons:
        if button == late_button:
            late = True
            is_passing = False
            is_missing = 0
            res = [late, is_passing, is_missing]
            bot.send_message(opinion)
        elif button == passing_button:
            is_passing = True
            late = False
            is_missing = 0
            res = [late, is_passing, is_missing]
            bot.send_message(opinion)
        elif button == missing_button:
            bot.send_message('К какому уроку ты изволишь приковылять? (напиши только число)')
            for i in range(2,7):    
                lesson = InlineKeyboardButton(str(i))
            user_response = update.message
            is_missing = user_response
            is_passing = False
            late = False
            res = [late, is_passing, is_missing]
            bot.send_message(opinion)
        return res

def main():
    '''
    Main script for running bot 24/7.
    '''
    updater.dispatcher.add_handler(CommandHandler('start'), send_data)
    
    answer = api_answer()
    print(build_message(answer))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
