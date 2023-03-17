import sqlite3 

from bot_db import db_input
from utils import language_keyboard


def send_cat(update, context):
    db_input(update.effective_user, update.message.chat.id)
    conn = sqlite3.connect('db/bot_database.db')
    cur = conn.cursor()
    people_id = update.effective_user.id
    language_people = cur.execute(f"SELECT language FROM bot_database WHERE user_id = {people_id}").fetchall()
    for row in language_people:
            language_user = row[0]
    if language_user == "russian":
        send_cat_picture = f"Прислать котика"
        return send_cat_picture
    elif language_user == "english":
        send_cat_picture = f"Send a cat"
        return send_cat_picture
    else:
        update.message.reply_text(
        reply_markup=language_keyboard()
        )

def send_picture(update, context):
    db_input(update.effective_user, update.message.chat.id)
    conn = sqlite3.connect('db/bot_database.db')
    cur = conn.cursor()
    people_id = update.effective_user.id
    language_people = cur.execute(f"SELECT language FROM bot_database WHERE user_id = {people_id}").fetchall()
    for row in language_people:
            language_user = row[0]
    if language_user == "russian":
        return "Прислать котика"
    elif language_user == "english":
        return"Send a cat"
    else:
        update.message.reply_text(
        reply_markup=language_keyboard()
        )