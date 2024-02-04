import sqlite3 as sq

db = sq.connect('tg.db')
cur = db.cursor()


async def db_start():
    cur.execute("CREATE TABLE IF NOT EXIST sellers("
                "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "chat_id INTEGER,"
                "username TEXT,"
                "caption TEXT,"
                "zapis TEXT,"
                "token TEXT,"
                "phone number)")
    cur.execute("CREATE TABLE IF NOT EXISTS buyers("
                "i_id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "username TEXT, "
                "phone_number TEXT, "
                "category TEXT, "
                "token TEXT,"
                "zapis TEXT)")
    db.commit()
