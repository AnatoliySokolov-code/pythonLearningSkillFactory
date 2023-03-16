#Создание Telegram-бота

import telebot

TOKEN = "6257486153:AAHtdNEakiHk5-M7Nwk7f1Oad9sCJ-K-DjI"

bot = telebot.TeleBot(TOKEN)
 #Чтобы запустить бота, нужно воспользоваться методом polling.

bot.polling(none_stop=True)

import telebot

TOKEN = "6257486153:AAHtdNEakiHk5-M7Nwk7f1Oad9sCJ-K-DjI"

bot = telebot.TeleBot(TOKEN)
# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    pass


# Обрабатываются все документы и аудиозаписи
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    pass
#Задание 18.3.1

#Допишите обработчик так, чтобы он из сообщения брал username и выдавал
# приветственное сообщение с привязкой к пользователю.
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Welcome, \ c{message.chat.username}")
#Задание 18.3.2
#Напишите обработчик, который на сообщения с фотографией будет отвечать
# сообщением «Nice meme XDD». Бот должен отвечать не отдельным сообщением,
# а с привязкой к картинке.
import telebot

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')


bot.polling(none_stop=True)
