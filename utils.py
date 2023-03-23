
from bot_db import emoji_of_the_user, update_emoji
from random import randint
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from translate import send_cat_translate_sentence, send_picture_translate_sentence, game_guess_namber_translate_sentence
from translate import your_namber_translate_sentence, mine_translate_word
from translate import win_translate_word, draw_translate_word, lose_translate_word
from translate import open_keyboard_translate_sentence, close_keyboard_translate_sentence, your_new_emoji_translate_sentence


def play_random_number(user_number, update):
    bot_number = randint(user_number - 20, user_number + 20)
    if user_number > bot_number:
        message = f"{your_namber_translate_sentence(update)} {user_number}, {mine_translate_word(update)} {bot_number}, {win_translate_word(update)} {emoji_of_the_user(update.effective_user)}"
    elif user_number == bot_number:
        message = f"{your_namber_translate_sentence(update)} {user_number}, {mine_translate_word(update)} {bot_number}, {draw_translate_word(update)} {emoji_of_the_user(update.effective_user)}"
    else:
        message = f"{your_namber_translate_sentence(update)} {user_number}, {mine_translate_word(update)} {bot_number}, {lose_translate_word(update)} {emoji_of_the_user(update.effective_user)}"
    return message



def main_keyboard(update, context):
    return ReplyKeyboardMarkup([[f"{send_cat_translate_sentence(update)}", 
                                 f"{send_picture_translate_sentence(update)}"],
                                [f"{game_guess_namber_translate_sentence(update)}"]], resize_keyboard= True)


def open_keyboard(update, context):
    update.message.reply_text(f"{open_keyboard_translate_sentence(update)} {emoji_of_the_user(update.effective_user)}", reply_markup=main_keyboard(update, context))
    

def close_keyboard(update, context):
    update.message.reply_text(f"{close_keyboard_translate_sentence(update)} {emoji_of_the_user(update.effective_user)}", reply_markup= ReplyKeyboardRemove())

def replacement_smile(update, context):
    people_id = update.effective_user.id
    update_emoji(people_id)
    update.message.reply_text(
        f"{your_new_emoji_translate_sentence(update)} {emoji_of_the_user(update.effective_user)}",
        reply_markup=main_keyboard(update, context)
        )