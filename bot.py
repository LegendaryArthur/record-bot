from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton
from dotenv import load_dotenv
from aiogram.utils.callback_data import CallbackData
from sqlite import db_start, create_profile, edit_profile
from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

start_keyboard = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('Оставить заявку', callback_data='new'))


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    db_start()
    message.from_user.last_name + message.from_user.first_name_name
    await message.answer('Привет, здесь ты можешь оставить заявку на обучение в "Octopus"', )


@dp.callback_query_handler(text="salesman")
async def send_start_value(call: types.CallbackQuery):
    rand_token = uuid4()
    await call.message.answer(f"Вы выбрали оказывать услуги! Вот ваш уникальный токен: {rand_token}.\n"f"Поделитесь этим токеном со своими клиентами, чтобы они могли записаться к вам!")


@dp.callback_query_handler(text="buyman")
async def send_start_value(call: types.CallbackQuery):
    await call.message.answer(f"Вы выбрали принимать услуги!")


@dp.message_handler(commands="help")
async def on_message(message):
    data = {
            f'username': ("user.id"),
            f'id': ("username"),
            f'date_entry': None,
            f'phone_number': None
        }
    await message.answer('Спасибо за предоставленную информацию!')


@dp.message_handler()
async def answer(message: types.Message):
    await message.reply('Я не понимаю вас')

if __name__ == '__main__':
    executor.start_polling(dp)
