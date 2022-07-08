import sqlite3
from utils import main_keyboard
from bot_db import emoji_of_the_user

def subscribe(update, context):
    conn = sqlite3.connect('db/bot_database.db')
    cur = conn.cursor()
    people_id = update.effective_user.id
    subscribe_people = cur.execute("SELECT subscribe_status FROM bot_database WHERE user_id = ?", (people_id,)).fetchall()
    for row in subscribe_people:
            subscribe_user = row[0]
    if subscribe_user is None:
        cur.execute('UPDATE bot_database SET subscribe_status = ? WHERE user_id= ?',(1, people_id))
        conn.commit()
        update.message.reply_text(
        f"Теперь вы подписаны {emoji_of_the_user(update.effective_user)}",
        reply_markup=main_keyboard()
        )
    elif subscribe_user == 0:
        cur.execute('UPDATE bot_database SET subscribe_status = ? WHERE user_id= ?',(1, people_id))
        conn.commit()
        update.message.reply_text(
        f"Теперь вы подписаны {emoji_of_the_user(update.effective_user)}",
        reply_markup=main_keyboard()
        )
    else:
        update.message.reply_text(
        f"Вы уже подписаны {emoji_of_the_user(update.effective_user)}",
        reply_markup=main_keyboard()
        )


def unsubscribe(update, context):
    conn = sqlite3.connect('db/bot_database.db')
    cur = conn.cursor()
    people_id = update.effective_user.id
    subscribe_people = cur.execute(f"SELECT subscribe_status FROM bot_database WHERE user_id = {people_id}").fetchall()
    for row in subscribe_people:
            subscribe_user = row[0]
    if subscribe_user is None:
        update.message.reply_text(
        f"Вы еще не подписаны {emoji_of_the_user(update.effective_user)}",
        reply_markup=main_keyboard()
        )
    elif subscribe_user == 0:
        update.message.reply_text(
        f"Вы уже отписаны {emoji_of_the_user(update.effective_user)}",
        reply_markup=main_keyboard()
        )
    else:
        cur.execute('UPDATE bot_database SET subscribe_status = ? WHERE user_id= ?',(0, people_id))
        conn.commit()
        update.message.reply_text(
        f"Вы отписались {emoji_of_the_user(update.effective_user)}",
        reply_markup=main_keyboard()
        )