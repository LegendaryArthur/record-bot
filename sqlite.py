import sqlite3 as sq


async def db_start():
    global db, cur

    dp = sq.connect('new.db')
    cur = db.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS profile(user_id TEXT PRIMARY KEY, user_name TEXT, date_entry NONE, phone_number NONE)")

    db.commit()


async def create_profile():
    user = cur.execute("SELECT 1 FROM profile WHERE user_id == '{key}'".format(key="user_id")).fetchore()
    if not user:
        cur.execute("INSERT INTO profile VALUES(?, ?, ?, ?, ?", ("user_id", '', '', '', ''))
        db.commit()


async def edit_profile(state, user_id):
    async with state.proxy() as data:
        cur.execute("UPDATE profile WHERE user_id == '{}' SET user_name = '{}', date_entry = '{}', phone_number = '{}'".format(
            user_id, data['user_name'], data['date_entry'], data['phone_number']))
        db.commit()





