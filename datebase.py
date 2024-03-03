import sqlite3 as sq
async def db_start():
    db = sq.connect('tg.db')
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users("
                "chat_id INTEGER PRIMARY KEY, "
                "username TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS zayavki("
                "chat_id INTEGER,"
                "username INTEGER,"
                "date DATE, "
                "fio TEXT, "
                "school TEXT, "
                "class_ TEXT, "
                "vozvrast TEXT, "
                "uspevaemost TEXT,"
                "NumberPhone TEXT,"
                "provilSotSety TEXT,"
                "napravlenie1 TEXT,"
                "napravlenie2 TEXT,"
                "slyxiObOctopus TEXT,"
                "kakayasmena TEXT,"
                "kakiyekrushki TEXT,"
                "kemstanesh TEXT,"
                "lvlpc TEXT,"
                "YchastieVProject TEXT,"
                "timedz TEXT,"
                "progress TEXT,"
                "lichnost TEXT)")
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
    cur.execute('INSERT INTO zayavki(chat_id, username, date, fio, school, class_, vozvrast, uspevaemost, NumberPhone, provilSotSety, napravlenie1, napravlenie2, slyxiObOctopus, kakayasmena, kakiyekrushki, kemstanesh, lvlpc, YchastieVProject, timedz, progress, lichnost) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (data['chat_id'], data['username'], date, data['fio'], data['school'], data['class_'], data['vozvrast'], data['yspevaimoct'], data['NumberPhone'], data['provilSotSety'], data['napravlenie1'], data['napravlenie2'], data['slyxiObOctopus'], data['kakayasmena'], data['kakiyekrushki'], data['kemstanesh'], data['lvlpc'], data['YchastieVProject'], data['timedz'], data['progress'], data['lichnost']))
    db.commit()