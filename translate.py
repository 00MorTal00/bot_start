import sqlite3 

from bot_db import db_input
from telegram import ReplyKeyboardMarkup


def send_cat(update, context):
    db_input(update.effective_user, update.message.chat.id)
    conn = sqlite3.connect('db/bot_database.db')
    cur = conn.cursor()
    people_id = update.effective_user.id
    language_people = cur.execute(f"SELECT language FROM bot_database WHERE user_id = {people_id}").fetchall()
    for row in language_people:
            language_user = row[0]
    if language_user == "russian":
        send_cat_translate = "Прислать котика"
        return send_cat_translate
    elif language_user == "english":
        send_cat_translate = "Send a cat"
        return send_cat_translate
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
        send_picture_translate= "Прислать картинку"
        return send_picture_translate
    elif language_user == "english":
        send_picture_translate= "Send picture"
        return send_picture_translate
    else:
        update.message.reply_text(
        reply_markup=language_keyboard()
        )

def language_keyboard():
    return ReplyKeyboardMarkup([["Перейти на Русский язык", "Switch to English"]], resize_keyboard= True)