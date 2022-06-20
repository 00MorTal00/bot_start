from telegram import ReplyKeyboardMarkup
from glob import glob
from telegram.ext import CommandHandler, MessageHandler, Filters, ConversationHandler
from random import randint, choice
from utils import play_random_number, main_keyboard

def start(update, context):
    print("Запущенна игра")
    update.message.reply_text(
        f"Введите целое число {context.user_data['emoji']}",
        reply_markup= ReplyKeyboardMarkup([["Я не хочу играть"]], resize_keyboard= True)
    )
    return "namber"


def game_body(update, context):
    user_namber = update.message.text
    if (user_namber == "Я не хочу играть"):
        update.message.reply_text(f"Хорошо {context.user_data['emoji']}", reply_markup=main_keyboard())
        print("Игра завершена")
        return ConversationHandler.END
    elif len(user_namber.split()) >= 2:
        update.message.reply_text(f"Введите пожалуйста одно число {context.user_data['emoji']}")
        return "namber"
    else:
        try:
            user_namber = int(user_namber)
            message = play_random_number(user_namber)
        except (TypeError, ValueError):
            update.message.reply_text(f"Введите целое число, пожалуйста {context.user_data['emoji']}")    
            return "namber"
    update.message.reply_text(message, reply_markup=main_keyboard())
    print("Игра завершена")
    return ConversationHandler.END

def crach_game(update, context):
    update.message.reply_text(f"Вы сломали игру не делайте так больше пожалуйста {context.user_data['emoji']}", reply_markup=main_keyboard())
    return ConversationHandler.END


game_namber = ConversationHandler(
        entry_points=[CommandHandler("guess", start), MessageHandler(Filters.regex("^(Игра у кого число больше)$"), start)],
        states={"namber": [MessageHandler(Filters.text, game_body)]},
        fallbacks=[MessageHandler(Filters.text, crach_game)]
    )        