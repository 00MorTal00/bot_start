import sqlite3
from telegram.error import BadRequest

def send_to_subscribe(context):
    conn = sqlite3.connect('db/bot_database.db')
    cur = conn.cursor()
    sum_subscribe = cur.execute(f"SELECT user_id FROM bot_database WHERE subscribe_status = 'Yes' ").fetchall()
    for x in sum_subscribe:
        user_id = x
        try:
            context.bot.send_message(chat_id= user_id[0], text='hello ')
            print(f"Рассылка отправлена {user_id[0]}")
        except BadRequest:
            print (f"Такого пользователя нет {user_id[0]}")