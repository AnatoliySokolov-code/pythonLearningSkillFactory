# Создание Telegram-бота

import telebot

TOKEN = "6257486153:AAHtdNEakiHk5-M7Nwk7f1Oad9sCJ-K-DjI"

bot = telebot.TeleBot(TOKEN)

# Обрабатываются все документы и аудиозаписи
@bot.message_handler(content_types=['voice'])
def handle_audios(message):
    bot.send_message(message.chat.id, f"К сожалению, я не умею слушать и говорить, пишите мне пожалуйста, {message.chat.username}!")
#def say_lmao(message: telebot.types.Message):
#def handle_voice(message: telebot.types.Message):
    #bot.reply_to(message, 'К сожалению, я не умею слушать и говорить, пишите мне пожалуйста, ')

    # pass
@bot.message_handler(content_types=['document'])
def handle_docs(message):
    #
    bot.send_message(message.chat.id, f"Ваш документ получен, {message.chat.username}!")
# @bot.message_handler(filters)
# def function_name(message):
    # bot.reply_to(message, "This is a message handler")
# Задание 18.3.1

# Допишите обработчик так, чтобы он из сообщения брал username и выдавал
# приветственное сообщение с привязкой к пользователю.
@bot.message_handler(commands=['start', 'help']) 
def send_welcome(message):
    bot.send_message(message.chat.id, f"Добро пожаловать, {message.chat.username}!")

# Задание 18.3.2
# Напишите обработчик, который на сообщения с фотографией будет отвечать
# сообщением «Nice meme XDD». Бот должен отвечать не отдельным сообщением,
# а с привязкой к картинке.
@bot.message_handler(content_types=['photo'])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Красивый МЭМ, ха-ха-ха!')

 # Чтобы запустить бота, нужно воспользоваться методом polling. В конце кода
bot.polling(none_stop=True)
