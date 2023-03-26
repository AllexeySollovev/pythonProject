import telebot
from telebot import types
bot = telebot.TeleBot('6105768624:AAFTBo3WP8UpDMJZ8tEwLeBfv_cRO-HKCJE')
@bot.message_handler(commands=['start'])
def start_message(message):
        bot.send_message(message.chat.id, 'Привет😎')
@bot.message_handler(commands=['button'])
def button_message(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Кнопка")
        markup.add(item1)
        bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)
@bot.message_handler(content_types='text')
def message_reply(message):
        if message.text == "Кнопка":
                bot.send_message(message.chat.id, "https://www.youtube.com/channel/UClv-Dx_8uvgRltX6j-uqwqw")

bot.infinity_polling()


