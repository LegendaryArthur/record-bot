import sqlite3 as sq


def db_start():
    global db, cur

    db = sq.connect('new.db')
    cur = db.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS users("
                "chat_id INTEGER, "
                "user_name TEXT, "
                "fullname TEXT)")

    db.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS requests("  
                "id INTEGER,"
                "chat_id INTEGER,"
                "fullname TEXT,"
                "age INTEGER,"
                "section TEXT"
                "school TEXT,"
                "class TEXT,"
                "phone_number INTEGER,"
                "description TEXT)")
    db.commit()


async def add_user(message):
    cur.execute("INSERT OR IGNORE INTO users (chat_id, user_name, fullname) VALUES (?, ?, ?)", (message.chat.id, message.from_user.username, str(message.from_user.last_name) + str(message.from_user.first_name)))
    db.commit()

async def add_request(chat_id, fullname, age, section, school, klass, phone_number, description):
    cur.execute("INSERT INTO requests (chat_id, fullname, age, section, school, class, phone_number, description) VALUES (?, ?, ?, ?, ?, ?, ?", (chat_id, fullname, age, section, school, klass, phone_number, description))
    db.commit()

db_start()

def add_user():
    return None


def add_request():
    return None