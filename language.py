import sqlite3
from utils import main_keyboard
from bot_db import emoji_of_the_user, db_input


def en_language(update, context):
    db_input(update.effective_user, update.message.chat.id)
    conn = sqlite3.connect('db/bot_database.db')
    cur = conn.cursor()
    people_id = update.effective_user.id
    language_people = cur.execute("SELECT language FROM bot_database WHERE user_id = ?", (people_id,)).fetchall()
    for row in language_people:
            language_user = row[0]
    if language_user is None:
        cur.execute('UPDATE bot_database SET language = ? WHERE user_id= ?',("english", people_id))
        conn.commit()
        update.message.reply_text(
        f"Selected English {emoji_of_the_user(update.effective_user)}",
        reply_markup=main_keyboard(update, context)
        )
    elif language_user == "russian":
        cur.execute('UPDATE bot_database SET language = ? WHERE user_id= ?',("english", people_id))
        conn.commit()
        update.message.reply_text(
        f"You changed the Russian language to English {emoji_of_the_user(update.effective_user)}",
        reply_markup=main_keyboard(update, context)
        )
    else:
        update.message.reply_text(
        f"You already have English selected {emoji_of_the_user(update.effective_user)}",
        reply_markup=main_keyboard(update, context)
        )


def ru_language(update, context):
    db_input(update.effective_user, update.message.chat.id)
    conn = sqlite3.connect('db/bot_database.db')
    cur = conn.cursor()
    people_id = update.effective_user.id
    language_people = cur.execute(f"SELECT language FROM bot_database WHERE user_id = {people_id}").fetchall()
    for row in language_people:
            language_user = row[0]
    if language_user is None:
        cur.execute('UPDATE bot_database SET language = ? WHERE user_id= ?',("russian", people_id))
        conn.commit()
        update.message.reply_text(
        f"Вы выбрали Русский язык {emoji_of_the_user(update.effective_user)}",
        reply_markup=main_keyboard(update, context)
        )
    elif language_user == "english":
        cur.execute('UPDATE bot_database SET language = ? WHERE user_id= ?',("russian", people_id))
        conn.commit()
        update.message.reply_text(
        f"Вы поменяли язык с Английского на Русский {emoji_of_the_user(update.effective_user)}",
        reply_markup=main_keyboard(update, context)
        )
    else:
        cur.execute('UPDATE bot_database SET language = ? WHERE user_id= ?',("russian", people_id))
        conn.commit()
        update.message.reply_text(
        f"У вас уже выбран Русский язык {emoji_of_the_user(update.effective_user)}",
        reply_markup=main_keyboard(update, context)
        )

