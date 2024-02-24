from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardButton
from dotenv import load_dotenv
from aiogram.utils.callback_data import CallbackData
from sqlite import db_start, add_user, add_request
from aiogram.dispatcher.filters import Text
from config import TOKEN
from aiogram.dispatcher.filters.state import State, StatesGroup

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add('Направление').add('Оставить заявку')
napravlenie_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add('Курс "Коммерческий дизайн"')
zayavka_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add('Готов')
napravlenie_keyboard.add('Образовательный курс "Wed-разработка" ')
napravlenie_keyboard.add('"Unity"')
napravlenie_keyboard.add('"Python"')
napravlenie_keyboard.add('"БПЛА"')
napravlenie_keyboard.add('"Компьютерная грамотность"')
napravlenie_keyboard.add('"3D-моделирование"')
napravlenie_keyboard.add('"2D-моделирование"')
class zayavka(StatesGroup):
    waiting_for_food_name = State()
async def zayavka(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for name in zayavka_keyboard:
        keyboard.add(name)
    await message.answer("Выберите блюдо:", reply_markup=keyboard)
    await state.set_state(OrderFood.waiting_for_food_name.state)


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer('Привет, здесь ты можешь оставить заявку на обучение в "Octopus" или выбрать другое направление в информационном мире', reply_markup=start_keyboard)


@dp.message_handler(Text(equals='Направление'))
async def napravlenie(message: types.Message):
    await message.answer("Информацию о каком направлении вы хотите узнать?", reply_markup=napravlenie_keyboard)


@dp.message_handler(Text(equals='Оставить заявку'))
async def zayavka(message: types.Message):
    await message.answer('Здравствуйте готовы ли вы заполнить анкету чтобы попасть в команду "OCTOPUS"', reply_markup=zayavka_keyboard)


@dp.message_handler()
async def answer(message: types.Message):
    await message.reply('Я не понимаю вас')

if __name__ == '__main__':
    executor.start_polling(dp)