from tkinter import Button

import telebot
from telebot import types

bot = telebot.TeleBot('8119513486:AAEmBTdAO81PGm5_jUBMIXQduqXNDS1y2Dc')


@bot.message_handler(commands = ['start'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='🌍 World News', url='https://t.me/+YMVVyF6oFbkyYzIy')
    btn2 = types.InlineKeyboardButton(text='Тест', url='https://habr.com/ru/all/')
    markup.add(btn1)
    markup.add(btn2)
    bot.send_message(message.from_user.id, "🌍 World News – твой портал в эпицентр событий!", reply_markup = markup)



bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть