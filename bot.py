from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton
from dotenv import load_dotenv
from aiogram.utils.callback_data import CallbackData
cb = CallbackData("post", "id", "action")
import os


load_dotenv()
bot = Bot('6458498482:AAG7k9cg3p6b_L-ttV-U6r95v9yQiU_1_T4')
dp = Dispatcher(bot=bot)


main = InlineKeyboardMarkup(row_width=2)
main.add(InlineKeyboardButton('Оказываю услугу', callback_data='btn1'))
main.add(InlineKeyboardButton('Принимаю услугу', callback_data='btn2'))


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Оказываю услугу", callback_data="start_value"))
    keyboard.add(types.InlineKeyboardButton(text="Принимаю услугу", callback_data="start_value"))
    await message.answer("Выберите следующее", reply_markup=keyboard)
    button = types.InlineKeyboardButton(text="Оказываю услугу", callback_data="start_value")
    text = "Вы оказываете услуги! ",
    callback_data = cb.new(id=5, action="rendering")
    button = types.InlineKeyboardButton(text="Принимаю услугу", callback_data="start_value")
    text = "Вы принимаете услуги! ",
    callback_data = cb.new(id=5, action="adoption")


@dp.callback_query_handler(text="start_value")
async def send_start_value(call: types.CallbackQuery):
    await call.message.answer("Вы выбрали")


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAMGZZpEq7jJwkFLe-bGW7ilUq5bi8sAAjgLAAJO5JlLMrFH0tlPjNA0BA')
    await message.answer(f'{message.from_user.first_name}, приветстсвую вас!',
                         reply_markup=main)


@dp.message_handler(content_types=['sticker'])
async def check_sticker(message: types.Message):
    await message.answer(message.sticker.file_id)
    await bot.send_message(message.from_user.id, message.chat.id)


@dp.message_handler(content_types=['document', 'photo'])
async def forward_message(message: types.Message):
    await bot.forward_message(os.getenv('GROUP_AD'), message.from_user.id, message.message_id)


@dp.message_handler()
async def answer(message: types.Message):
    await message.reply('Я не понимаю вас')


if __name__ == '__main__':
    executor.start_polling(dp)
