import sqlite3 as sq
async def db_start():
    db = sq.connect('tg.db')
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXIST users("
                "chat_id INTEGER PRIMARY KEY, "
                "username TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS zayavki("
                "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "date DATE, "
                "fio TEXT, "
                "school TEXT, "
                "class_ TEXT, "
                "vozrast TEXT, "
                "uspevaemost TEXT,"
                "phone TEXT,"
                "social_net TEXT,"
                "napravlenie1 TEXT,"
                "napravlenie2 TEXT,"
                "sluhi_octopus TEXT,"
                "smena TEXT,"
                "dop_sections TEXT,"
                "who_want_to_be TEXT,"
                "comp_level TEXT,"
                "uchastie_v_projects TEXT,"
                "dz_time TEXT,"
                "progress TEXT,"
                "lichost TEXT)")
    db.commit()

from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('оказываю услугу').add('получаю услугу')

async def add_user(message):
    db = sq.connect('tg.db')
    cur = db.cursor()
    cur.execute('INSERT OR IGNORE INTO users(chat_id, username) VALUES(?,?)', (message.chat.id, message.from_user.username))
    db.commit()

async def add_zapis(date, data):
    db = sq.connect('tg.db')
    cur = db.cursor()
    cur.execute('INSERT INTO zayavki(date, fio, school, class_, vozrast, uspevaemost,phone, social_net, napravlenie1, napravlenie2, sluhi_octopus, smena, dop_sections, who_want_to_be, comp_level, uchastie_v_projects, dz_time, progress, lichost) VALUES(?,?)', (message.chat.id, message.from_user.username)
