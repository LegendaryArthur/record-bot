from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

from app import database as db
async def on_startup(_):
    await db.db_start()
    print('Бот успешно запущен!')
    import sqlite3 as sq

db = sq.connect('tg.db')
cur = db.cursor()

async def db_start():
    cur.execute("CREATE TABLE IF NOT EXIST accounts("
                "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "cart_id TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS items("
                "i_id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "name TEXT, "
                "desc TEXT, "
                "price TEXT, "
                "photo TEXT, "
                "brand TEXT)")
db.commit()
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('оказываю услугу').add('получаю услугу')