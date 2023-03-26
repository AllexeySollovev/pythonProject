import telebot
from telebot import types
bot = telebot.TeleBot('6105768624:AAFTBo3WP8UpDMJZ8tEwLeBfv_cRO-HKCJE')
#УЧИМ БОТА РЕАГИРОВАТЬ НА СООБЩЕНИЯ
# @bot.message_handler(content_types=['text']) #метод получения текстовых сообщений
# def get_text_messages(message):
#     if message.text == "Привет" or message.text == 'привет':
#         bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
#     elif message.text == "/help":
#         bot.send_message(message.from_user.id, "Напиши привет")
#     else:
#         bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
#

#ВНЕСЕНИЕ ДАННЫХ КОТОРЫЕ ВПИШЕТ ПОЛЬЗОВАТЕЛЬ В ПЕРЕМЕННЫЕ
name = ''
surname = ''
age = 0
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, 'Как тебя зовут?')
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')
def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)
def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)
def get_age(message):
    global age
    while:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Введите возраст цифрами!!!')
    #СОЗДАНИЕ КНОПОК
    keyboard = types.InlineKeyboardMarkup() #наша клавиатура
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')  # кнопка «Да»
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_yes)  # добавляем кнопки в клавиатуру
    keyboard.add(key_no)
    question = 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + ' ' + surname + '?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'yes':
        bot.send_message(call.message.chat.id, 'Заполнил твои данные в базу...')
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, 'Ты мошенник тупой')

bot.polling(none_stop=True, interval=0)


