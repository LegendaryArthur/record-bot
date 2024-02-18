import sqlite3

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import  MemoryStorage
from aiogram.dispatcher import FSMContext

bot = Bot('6797314417:AAEIJjJe4p0zK883fmUGwYcNJ5kP8UAas')
connection = sqlite3.connect('tg.db')
cursor = connection.cursor()

Fio = ''
age = 0


def start(message):
    if message.text == '/start':
        await bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_Fio) #следующий шаг – функция get_age
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')


def get_Fio(message): #получаем ФИО
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    global age
    while age == 0: #проверяем что возраст изменился
        try:
             age = int(message.text) #проверяем, что возраст введен корректно
        except Exception:
             bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
    bot.send_message(message.from_user.id, 'Тебе '+str(age)+' лет, тебя зовут '+name+'?')

    bot.polling(none_stop=True, interval=0)
