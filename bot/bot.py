from telegram import Bot, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler
import requests
from const_data import (
    TG_TOKEN, DB_TOKEN, DEMIAN_ID, NIKITA_ID, HEADERS, ENDPOINT, OPINION,
    BUTTONS, late_button, missing_button, passing_button
)

updater = Updater(token=TG_TOKEN)
bot = Bot(token=TG_TOKEN)


def send_message(bot: Bot, message, id):
    '''
    Functions for sending message to teacher at fixed time.
    '''
    bot.send_message(id, message)


def api_answer():
    response = requests.get(ENDPOINT)
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
    bot.send_message(
        chat_id=DEMIAN_ID,
        text='Привет, почетный огурец! Сообщи, придешь ли ты',
        reply_markup=BUTTONS
    )

    for button in BUTTONS:
        late = False
        is_passing = False
        is_missing = 0
        if button == late_button:
            late = True
        elif button == passing_button:
            is_passing = True
        elif button == missing_button:
            for i in range(2, 7):
                lesson = InlineKeyboardButton(str(i))
                bot.send_message(
                    chat_id=NIKITA_ID,
                    text='К какому уроку ты изволишь приковылять?',
                    reply_markup=lesson
                    )
            user_response = update.message
            is_missing = user_response
        res = [late, is_passing, is_missing]
        bot.send_message(OPINION)
        return res


def main():
    '''
    Main script for running bot 24/7.
    '''
    updater.dispatcher.add_handler(CommandHandler('start', send_data))

    answer = api_answer()
    message = build_message(answer)

    send_message(bot=bot, message='Никита доделай бота', id=DEMIAN_ID)
    data = send_data()
    update_db(data)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
