import configparser
from loguru import logger
import mysql.connector
import telebot
from telebot import types
import game


# Підключення до бази даних
db = mysql.connector.connect(
    host="localhost",
    user="administration",
    password="329600",
    database="it-sprout"
)

# Ініціалізація телеграм-бота
config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

bot = telebot.TeleBot(config['Telegram']['token'])
logger.add('error.log', rotation='10 MB', level='ERROR', format='{time} - {level} - {message}')


# Обробник команди /start
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Привіт 👋")
    item2 = types.KeyboardButton("Допомога ❓")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Вітаю! Я тут, щоб допомогти вам з IT-навичками 🚀", reply_markup=markup)


# Обробник команди /help
@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, "Тут буде ваша допомога з гейміфікованим навчанням IT!")


# Обробник відповіді на повідомлення "Привіт 👋"
@bot.message_handler(func=lambda message: message.text == 'Привіт 👋')
def handle_hello(message):
    bot.send_message(message.chat.id, "Привіт! Я радий бачити вас тут 🌟")


# Обробник відповіді на повідомлення "Допомога ❓"
@bot.message_handler(func=lambda message: message.text == 'Допомога ❓')
def handle_help(message):
    bot.send_message(message.chat.id, "Я завжди тут, щоб допомогти вам з IT-навичками! 🚀")


# Запуск бота
bot.polling(none_stop=True)
