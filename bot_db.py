import sqlite3 
import emoji
import settings
from emoji import emojize
from random import choice


def db_input (effective_user, chat_id):
    conn = sqlite3.connect('db/bot_database.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS bot_database(
        user_id      INTEGER NOT NULL,
        chat_id      INTEGER NOT NULL,
        user_name    TEXT,
        user_surname TEXT,
        username     STRING,
        emoji_status STRING
    )""")
    conn.commit()
    people_id = effective_user.id
    cur.execute(f"SELECT user_id FROM bot_database WHERE user_id = {people_id}")
    data_user = cur.fetchone()
    emoji = emojize(choice(settings.USER_EMOJI), use_aliases=True)
    if data_user is None:
        user_data =  [effective_user.id, chat_id, effective_user.first_name, effective_user.last_name, effective_user.username, emoji]
        cur.execute("INSERT INTO bot_database VALUES(?, ?, ?, ?, ?, ?);", user_data)
        conn.commit()

def emoji_of_the_user(effective_user):
    conn = sqlite3.connect('db/bot_database.db')
    cur = conn.cursor()
    people_id = effective_user.id
    data_id = """select * from bot_database where user_id = ?"""
    cur.execute(data_id, (people_id,))
    emoji_user = cur.fetchall()
    for row in emoji_user:
            emoji_of_user = row[-1]
    if emoji_of_user is None:
        update_emoji(people_id)    
    return emoji_of_user    

def update_emoji(people_id):
    conn = sqlite3.connect('db/bot_database.db')
    cur = conn.cursor()
    emoji = emojize(choice(settings.USER_EMOJI), use_aliases=True)
    new_emoji = cur.execute(f'SELECT emoji_status FROM bot_database WHERE user_id ={people_id}').fetchall()
    for x in new_emoji:
        emoji_status = x
        cur.execute('UPDATE bot_database SET emoji_status = ? WHERE user_id= ?',(emoji, people_id))
    conn.commit()