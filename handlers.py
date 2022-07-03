from glob import glob
from random import choice
from utils import smile_lite, main_keyboard
from bot_db import db_input

def greet_user(update, context):
    context.user_data['emoji'] = smile_lite(context.user_data)
    print('Вызван /start')
    db_input(update.effective_user, update.message.chat.id)
    update.message.reply_text(
        f"Здравстыуй пользователь {context.user_data['emoji']} !", reply_markup=main_keyboard())

def talk_to_me(update, context):
    text = update.message.text
    context.user_data['emoji'] = smile_lite(context.user_data)
    print(text)
    db_input(update.effective_user, update.message.chat.id)
    update.message.reply_text(
        f"{text} {context.user_data['emoji']}",
        reply_markup=main_keyboard()
        )


def send_cat_picture(update, context):
    print("Использована команда котик")
    db_input(update.effective_user, update.message.chat.id)
    cat_photos_list = glob("images/cat*.jp*g")
    cat_pic_filename = choice(cat_photos_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_pic_filename, "rb"), reply_markup=main_keyboard())
