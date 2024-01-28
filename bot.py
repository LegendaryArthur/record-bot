from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton
from dotenv import load_dotenv
from aiogram.utils.callback_data import CallbackData
from uuid import uuid4
cb = CallbackData("post", "id", "action")


load_dotenv()
bot = Bot('6458498482:AAG7k9cg3p6b_L-ttV-U6r95v9yQiU_1_T4')
dp = Dispatcher(bot=bot)


main = InlineKeyboardMarkup(row_width=2)
main.add(InlineKeyboardButton('Оказываю услугу', callback_data='btn1'))
main.add(InlineKeyboardButton('Принимаю услугу', callback_data='btn2'))


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='Оказываю услугу', callback_data="salesman"))
    keyboard.add(types.InlineKeyboardButton(text='Принимаю услугу', callback_data="buyman"))
    await message.answer('Выберите следующее', reply_markup=keyboard)


@dp.callback_query_handler(text="salesman")
async def send_start_value(call: types.CallbackQuery):
    rand_token = uuid4()
    await call.message.answer(f"Вы выбрали оказывать услуги! Вот ваш уникальный токен: {rand_token}.\nПоделитесь этим токеном со своими клиентами, чтобы они могли записаться к вам!")


@dp.callback_query_handler(text="buyman")
async def send_start_value(call: types.CallbackQuery):
    await call.message.answer(f"Вы выбрали принимать услуги!")


@dp.message_handler()
async def answer(message: types.Message):
    await message.reply('Я не понимаю вас')


if __name__ == '__main__':
    executor.start_polling(dp)
