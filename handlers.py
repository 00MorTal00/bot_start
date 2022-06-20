from glob import glob
from random import choice
from utils import smile_lite, main_keyboard

def greet_user(update, context):
    context.user_data["emoji"] = smile_lite(context.user_data)
    print('Вызван /start')
    update.message.reply_text(
        f'Здравстыуй пользователь {context.user_data["emoji"]} !', reply_markup=main_keyboard())

def talk_to_me(update, context):
    text = update.message.text
    context.user_data["emoji"] = smile_lite(context.user_data)
    print(text)
    update.message.reply_text(
        f'{text} {context.user_data["emoji"]}',
        reply_markup=main_keyboard()
        )


def send_cat_picture(update, context):
    print("Использована команда котик")
    cat_photos_list = glob("images/cat*.jp*g")
    cat_pic_filename = choice(cat_photos_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_pic_filename, "rb"), reply_markup=main_keyboard())
