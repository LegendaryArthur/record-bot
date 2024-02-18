from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton
from dotenv import load_dotenv
from aiogram.utils.callback_data import CallbackData
from sqlite import db_start, add_user, add_request
from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

start_keyboard = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('Оставить заявку', callback_data='new'))


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    db_start()
    await add_user(message)
    await message.answer('Привет, здесь ты можешь оставить заявку на обучение в "Octopus"', reply_markup=start_keyboard)


@dp.message_handler()
async def answer(message: types.Message):
    await message.reply('Я не понимаю вас')

if __name__ == '__main__':
    executor.start_polling(dp)
