import sqlite3 

from bot_db import db_input
from telegram import ReplyKeyboardMarkup


def send_cat_translate_sentence(update):
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

def send_picture_translate_sentence(update):
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

def game_guess_namber_translate_sentence(update):
    db_input(update.effective_user, update.message.chat.id)
    conn = sqlite3.connect('db/bot_database.db')
    cur = conn.cursor()
    people_id = update.effective_user.id
    language_people = cur.execute(f"SELECT language FROM bot_database WHERE user_id = {people_id}").fetchall()
    for row in language_people:
            language_user = row[0]
    if language_user == "russian":
        game_guess_namber_translate= "Игра у кого число больше"
        return game_guess_namber_translate
    elif language_user == "english":
        game_guess_namber_translate= "Game guess whose number higher"
        return game_guess_namber_translate
    else:
        update.message.reply_text(
        reply_markup=language_keyboard()
        )

def insert_namber_translate_sentence(update):
    db_input(update.effective_user, update.message.chat.id)
    conn = sqlite3.connect('db/bot_database.db')
    cur = conn.cursor()
    people_id = update.effective_user.id
    language_people = cur.execute(f"SELECT language FROM bot_database WHERE user_id = {people_id}").fetchall()
    for row in language_people:
            language_user = row[0]
    if language_user == "russian":
        insert_namber_translate= "Введите целое число"
        return insert_namber_translate
    elif language_user == "english":
        insert_namber_translate= "Write an integer number"
        return insert_namber_translate
    else:
        update.message.reply_text(
        reply_markup=language_keyboard()
        )

def dont_wanna_play_translate_sentence(update):
    db_input(update.effective_user, update.message.chat.id)
    conn = sqlite3.connect('db/bot_database.db')
    cur = conn.cursor()
    people_id = update.effective_user.id
    language_people = cur.execute(f"SELECT language FROM bot_database WHERE user_id = {people_id}").fetchall()
    for row in language_people:
            language_user = row[0]
    if language_user == "russian":
        dont_wanna_play_translate= "Я не хочу играть"
        return dont_wanna_play_translate
    elif language_user == "english":
        dont_wanna_play_translate= "I don't want to play"
        return dont_wanna_play_translate
    else:
        update.message.reply_text(
        reply_markup=language_keyboard()
        )

def ok_translate_word(update):
    db_input(update.effective_user, update.message.chat.id)
    conn = sqlite3.connect('db/bot_database.db')
    cur = conn.cursor()
    people_id = update.effective_user.id
    language_people = cur.execute(f"SELECT language FROM bot_database WHERE user_id = {people_id}").fetchall()
    for row in language_people:
            language_user = row[0]
    if language_user == "russian":
        ok_translate= "Хорошо"
        return ok_translate
    elif language_user == "english":
        ok_translate= "Ok"
        return ok_translate
    else:
        update.message.reply_text(
        reply_markup=language_keyboard()
        )

def one_namber_translate_sentence(update):
    db_input(update.effective_user, update.message.chat.id)
    conn = sqlite3.connect('db/bot_database.db')
    cur = conn.cursor()
    people_id = update.effective_user.id
    language_people = cur.execute(f"SELECT language FROM bot_database WHERE user_id = {people_id}").fetchall()
    for row in language_people:
            language_user = row[0]
    if language_user == "russian":
        one_namber_translate= "Введите пожалуйста одно число"
        return one_namber_translate
    elif language_user == "english":
        one_namber_translate= "Please write one number"
        return one_namber_translate
    else:
        update.message.reply_text(
        reply_markup=language_keyboard()
        )

def integer_namber_translate_sentence(update):
    db_input(update.effective_user, update.message.chat.id)
    conn = sqlite3.connect('db/bot_database.db')
    cur = conn.cursor()
    people_id = update.effective_user.id
    language_people = cur.execute(f"SELECT language FROM bot_database WHERE user_id = {people_id}").fetchall()
    for row in language_people:
            language_user = row[0]
    if language_user == "russian":
        integer_namber_translate= "Введите целое число, пожалуйста"
        return integer_namber_translate
    elif language_user == "english":
        integer_namber_translate= "Write an integer number, please"
        return integer_namber_translate
    else:
        update.message.reply_text(
        reply_markup=language_keyboard()
        )

def crash_game_translate_sentence(update):
    db_input(update.effective_user, update.message.chat.id)
    conn = sqlite3.connect('db/bot_database.db')
    cur = conn.cursor()
    people_id = update.effective_user.id
    language_people = cur.execute(f"SELECT language FROM bot_database WHERE user_id = {people_id}").fetchall()
    for row in language_people:
            language_user = row[0]
    if language_user == "russian":
        crash_game_translate= "Вы сломали игру не делайте так больше пожалуйста"
        return crash_game_translate
    elif language_user == "english":
        crash_game_translate= "You broke the game please don't do this again"
        return crash_game_translate
    else:
        update.message.reply_text(
        reply_markup=language_keyboard()
        )

def your_namber_translate_sentence(update):
    db_input(update.effective_user, update.message.chat.id)
    conn = sqlite3.connect('db/bot_database.db')
    cur = conn.cursor()
    people_id = update.effective_user.id
    language_people = cur.execute(f"SELECT language FROM bot_database WHERE user_id = {people_id}").fetchall()
    for row in language_people:
            language_user = row[0]
    if language_user == "russian":
        your_namber_translate= "Ваше число"
        return your_namber_translate
    elif language_user == "english":
        your_namber_translate= "Your number"
        return your_namber_translate
    else:
        update.message.reply_text(
        reply_markup=language_keyboard()
        )

def mine_translate_word(update):
    db_input(update.effective_user, update.message.chat.id)
    conn = sqlite3.connect('db/bot_database.db')
    cur = conn.cursor()
    people_id = update.effective_user.id
    language_people = cur.execute(f"SELECT language FROM bot_database WHERE user_id = {people_id}").fetchall()
    for row in language_people:
            language_user = row[0]
    if language_user == "russian":
        mine_translate= "моё"
        return mine_translate
    elif language_user == "english":
        mine_translate= "mine"
        return mine_translate
    else:
        update.message.reply_text(
        reply_markup=language_keyboard()
        )

def win_translate_word(update):
    db_input(update.effective_user, update.message.chat.id)
    conn = sqlite3.connect('db/bot_database.db')
    cur = conn.cursor()
    people_id = update.effective_user.id
    language_people = cur.execute(f"SELECT language FROM bot_database WHERE user_id = {people_id}").fetchall()
    for row in language_people:
            language_user = row[0]
    if language_user == "russian":
        win_translate= "вы выиграли"
        return win_translate
    elif language_user == "english":
        win_translate= "you won"
        return win_translate
    else:
        update.message.reply_text(
        reply_markup=language_keyboard()
        )

def draw_translate_word(update):
    db_input(update.effective_user, update.message.chat.id)
    conn = sqlite3.connect('db/bot_database.db')
    cur = conn.cursor()
    people_id = update.effective_user.id
    language_people = cur.execute(f"SELECT language FROM bot_database WHERE user_id = {people_id}").fetchall()
    for row in language_people:
            language_user = row[0]
    if language_user == "russian":
        draw_translate= "ничья"
        return draw_translate
    elif language_user == "english":
        draw_translate= "draw"
        return draw_translate
    else:
        update.message.reply_text(
        reply_markup=language_keyboard()
        )

def lose_translate_word(update):
    db_input(update.effective_user, update.message.chat.id)
    conn = sqlite3.connect('db/bot_database.db')
    cur = conn.cursor()
    people_id = update.effective_user.id
    language_people = cur.execute(f"SELECT language FROM bot_database WHERE user_id = {people_id}").fetchall()
    for row in language_people:
            language_user = row[0]
    if language_user == "russian":
        lose_translate= "вы проиграли"
        return lose_translate
    elif language_user == "english":
        lose_translate= "you lose"
        return lose_translate
    else:
        update.message.reply_text(
        reply_markup=language_keyboard()
        )

def open_keyboard_translate_sentence(update):
    db_input(update.effective_user, update.message.chat.id)
    conn = sqlite3.connect('db/bot_database.db')
    cur = conn.cursor()
    people_id = update.effective_user.id
    language_people = cur.execute(f"SELECT language FROM bot_database WHERE user_id = {people_id}").fetchall()
    for row in language_people:
            language_user = row[0]
    if language_user == "russian":
        open_keyboard_translate= "Вы открыли клавиатуру"
        return open_keyboard_translate
    elif language_user == "english":
        open_keyboard_translate= "You opened the keyboard"
        return open_keyboard_translate
    else:
        update.message.reply_text(
        reply_markup=language_keyboard()
        )

def close_keyboard_translate_sentence(update):
    db_input(update.effective_user, update.message.chat.id)
    conn = sqlite3.connect('db/bot_database.db')
    cur = conn.cursor()
    people_id = update.effective_user.id
    language_people = cur.execute(f"SELECT language FROM bot_database WHERE user_id = {people_id}").fetchall()
    for row in language_people:
            language_user = row[0]
    if language_user == "russian":
        close_keyboard_translate= "Вы закрыли клавиатуру"
        return close_keyboard_translate
    elif language_user == "english":
        close_keyboard_translate= "You closed the keyboard"
        return close_keyboard_translate
    else:
        update.message.reply_text(
        reply_markup=language_keyboard()
        )

def your_new_emoji_translate_sentence(update):
    db_input(update.effective_user, update.message.chat.id)
    conn = sqlite3.connect('db/bot_database.db')
    cur = conn.cursor()
    people_id = update.effective_user.id
    language_people = cur.execute(f"SELECT language FROM bot_database WHERE user_id = {people_id}").fetchall()
    for row in language_people:
            language_user = row[0]
    if language_user == "russian":
        your_new_emoji_translate= "Теперь у вас такой самйлик"
        return your_new_emoji_translate
    elif language_user == "english":
        your_new_emoji_translate= "Now you have such an emoticon"
        return your_new_emoji_translate
    else:
        update.message.reply_text(
        reply_markup=language_keyboard()
        )

def language_keyboard():
    return ReplyKeyboardMarkup([["Перейти на Русский язык", "Switch to English"]], resize_keyboard= True)