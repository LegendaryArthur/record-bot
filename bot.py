from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import  ReplyKeyboardMarkup
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot('6458498482:AAG7k9cg3p6b_L-ttV-U6r95v9yQiU_1_T4')
dp = Dispatcher(bot=bot)


main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('1').add('2').add('3')


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
