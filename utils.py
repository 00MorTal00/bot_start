import settings
from glob import glob
from emoji import emojize
from random import randint, choice
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove


def smile_lite(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    else:
        return user_data['emoji']

def play_random_number(user_number):
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        message = f"Ваше число {user_number}, мое {bot_number}, вы выиграли"
    elif user_number == bot_number:
        message = f"Ваше число {user_number}, мое {bot_number}, ничья"
    else:
        message = f"Ваше число {user_number}, мое {bot_number}, вы проиграли"
    return message




def main_keyboard():
    return ReplyKeyboardMarkup([["Прислать котика"], ["Игра у кого чило больше"]], resize_keyboard= True)

def open_keyboard(update, context):
    context.user_data['emoji'] = smile_lite(context.user_data)
    update.message.reply_text(f"Вы открыли клавиатуру {context.user_data['emoji']}", reply_markup=main_keyboard())
    

def close_keyboard(update, context):
    context.user_data['emoji'] = smile_lite(context.user_data)
    update.message.reply_text(f"Вы закрыли клавиатуру {context.user_data['emoji']}", reply_markup= ReplyKeyboardRemove())