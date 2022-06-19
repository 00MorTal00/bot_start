from glob import glob
from random import randint, choice
from utils import smile_lite, play_random_number, main_keyboard

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

def guess_number(update, context):
    print(context.args)
    if context.args:
        try:
            user_namber = int(context.args[0])
            message = play_random_number(user_namber)
        except (TypeError, ValueError):
            message = "Введите целое число"
    else:
        message = "Введите число"
    update.message.reply_text(message, reply_markup=main_keyboard())

def send_cat_picture(update, context):
    print("Использована команда котик")
    cat_photos_list = glob("images/cat*.jp*g")
    cat_pic_filename = choice(cat_photos_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_pic_filename, "rb"), reply_markup=main_keyboard())
