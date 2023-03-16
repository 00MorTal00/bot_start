
from bot_db import emoji_of_the_user, update_emoji
from random import randint
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove



def play_random_number(user_number, update):
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        message = f"Ваше число {user_number}, мое {bot_number}, вы выиграли {emoji_of_the_user(update.effective_user)}"
    elif user_number == bot_number:
        message = f"Ваше число {user_number}, мое {bot_number}, ничья {emoji_of_the_user(update.effective_user)}"
    else:
        message = f"Ваше число {user_number}, мое {bot_number}, вы проиграли {emoji_of_the_user(update.effective_user)}"
    return message




def main_keyboard():
    return ReplyKeyboardMarkup([["Прислать котика", "Прислать картинку"], ["Игра у кого число больше"]], resize_keyboard= True)

def language_keyboard():
    return ReplyKeyboardMarkup([["Перейти на Русский язык", "Switch to English"]], resize_keyboard= True)

def open_keyboard(update, context):
    update.message.reply_text(f"Вы открыли клавиатуру {emoji_of_the_user(update.effective_user)}", reply_markup=main_keyboard())
    

def close_keyboard(update, context):
    update.message.reply_text(f"Вы закрыли клавиатуру {emoji_of_the_user(update.effective_user)}", reply_markup= ReplyKeyboardRemove())

def replacement_smile(update, context):
    people_id = update.effective_user.id
    update_emoji(people_id)
    update.message.reply_text(
        f"Теперь у вас такой самйлик {emoji_of_the_user(update.effective_user)}",
        reply_markup=main_keyboard()
        )