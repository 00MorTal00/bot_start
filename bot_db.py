import sqlite3 
import os
import emoji_from_dev
from emoji import emojize
from random import choice


def db_input (effective_user, chat_id):
    os.makedirs('db', exist_ok=True)
    conn = sqlite3.connect('db/bot_database.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS bot_database(
        user_id          INTEGER NOT NULL,
        chat_id          INTEGER NOT NULL,
        user_name        TEXT,
        user_surname     TEXT,
        username         STRING,
        emoji_status     STRING,
        subscribe_status TEXT,
        language         TEXT
    )""")
    conn.commit()
    people_id = effective_user.id
    cur.execute(f"SELECT user_id FROM bot_database WHERE user_id = {people_id}")
    data_user = cur.fetchone()
    emoji = emojize(choice(emoji_from_dev.USER_EMOJI), use_aliases=True)
    sub = "No"
    lang = None
    if data_user is None:
        user_data =  [effective_user.id, chat_id, effective_user.first_name, effective_user.last_name, effective_user.username, emoji, sub, lang]
        cur.execute("INSERT INTO bot_database VALUES(?, ?, ?, ?, ?, ?, ?, ?);", user_data)
        conn.commit()

def emoji_of_the_user(effective_user):
    conn = sqlite3.connect('db/bot_database.db')
    cur = conn.cursor()
    people_id = effective_user.id
    data_id = """select emoji_status from bot_database where user_id = ?"""
    cur.execute(data_id, (people_id,))
    emoji_user = cur.fetchall()
    for row in emoji_user:
            emoji_of_user = row[0]
    if emoji_of_user is None:
        update_emoji(people_id)    
    return emoji_of_user    

def update_emoji(people_id):
    conn = sqlite3.connect('db/bot_database.db')
    cur = conn.cursor()
    emoji = emojize(choice(emoji_from_dev.USER_EMOJI), use_aliases=True)
    cur.execute('UPDATE bot_database SET emoji_status = ? WHERE user_id= ?',(emoji, people_id))
    conn.commit()