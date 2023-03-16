import os
from glob import glob
from random import choice
from utils import main_keyboard, language_keyboard
from bot_db import db_input, emoji_of_the_user

def greet_user(update, context):
    print('Вызван /start')
    db_input(update.effective_user, update.message.chat.id)
    update.message.reply_text(
        f"Здравстыуй пользователь {emoji_of_the_user(update.effective_user)} !", 
        reply_markup=main_keyboard()
        )
    update.message.reply_text(
        f"Выберите язык / Choose language {emoji_of_the_user(update.effective_user)}", 
        reply_markup=language_keyboard()
        )

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    db_input(update.effective_user, update.message.chat.id)
    update.message.reply_text(
        f"{text} {emoji_of_the_user(update.effective_user)}",
        reply_markup=main_keyboard()
        )


def send_cat_picture(update, context):
    print("Использована команда котик")
    db_input(update.effective_user, update.message.chat.id)
    cat_photos_list = glob("images/cat*.jp*g")
    cat_pic_filename = choice(cat_photos_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_pic_filename, "rb"), reply_markup=main_keyboard())

def send_users_picture(update, context):
    print("Использована команда фото")
    db_input(update.effective_user, update.message.chat.id)
    user_photos_list = glob("user_photo/*.jp*g")
    user_pic_filename = choice(user_photos_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(user_pic_filename, "rb"), reply_markup=main_keyboard())

def check_user_photo(update, context):
    os.makedirs('user_photo', exist_ok=True)
    photo_file = context.bot.getFile(update.message.photo[-1].file_id)
    file_name = os.path.join('user_photo', f'{update.message.photo[-1].file_id}.jpg')
    photo_file.download(file_name)
    print('прислали фото')
    db_input(update.effective_user, update.message.chat.id)
    update.message.reply_text(
        f"Фото сохранено. {emoji_of_the_user(update.effective_user)} ", 
        reply_markup=main_keyboard()
        )