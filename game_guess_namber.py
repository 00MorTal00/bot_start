from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, Filters, ConversationHandler
from utils import play_random_number, main_keyboard
from bot_db import emoji_of_the_user
from translate import insert_namber_translate_sentence, dont_wanna_play_translate_sentence, ok_translate_word, one_namber_translate_sentence
from translate import integer_namber_translate_sentence, crash_game_translate_sentence

def start(update, context):
    print("Запущенна игра")
    update.message.reply_text(
        f"{insert_namber_translate_sentence(update)} {emoji_of_the_user(update.effective_user)}",
        reply_markup= ReplyKeyboardMarkup([[f"{dont_wanna_play_translate_sentence(update)}"]], 
                                          resize_keyboard= True)
    )
    return "namber"


def game_body(update, context):
    user_namber = update.message.text
    if (user_namber == "Я не хочу играть" or user_namber == "I don't want to play" ):
        update.message.reply_text(f"{ok_translate_word(update)} {emoji_of_the_user(update.effective_user)}", 
                                  reply_markup=main_keyboard(update, context))
        print("Игра завершена")
        return ConversationHandler.END
    elif len(user_namber.split()) >= 2:
        update.message.reply_text(f"{one_namber_translate_sentence(update)} {emoji_of_the_user(update.effective_user)}")
        return "namber"
    else:
        try:
            user_namber = int(user_namber)
            message = play_random_number(user_namber,update)
        except (TypeError, ValueError):
            update.message.reply_text(f"{integer_namber_translate_sentence(update)} {emoji_of_the_user(update.effective_user)}")    
            return "namber"
    update.message.reply_text(message, reply_markup=main_keyboard(update, context))
    print("Игра завершена")
    return ConversationHandler.END

def crach_game(update, context):
    update.message.reply_text(f"{crash_game_translate_sentence(update)} {emoji_of_the_user(update.effective_user)}", 
                              reply_markup=main_keyboard(update, context))
    return ConversationHandler.END


game_namber = ConversationHandler(
        entry_points=[CommandHandler("guess", start), 
                      MessageHandler(Filters.regex("^(Игра у кого число больше)$") | Filters.regex("^(Game guess whose number higher)$"), 
                                     start)],
        states={"namber": [MessageHandler(Filters.text, game_body)]},
        fallbacks=[MessageHandler(Filters.text, crach_game)]
    )        