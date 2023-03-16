
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from game_guess_namber import game_namber

import settings
from handlers import greet_user, send_cat_picture, send_users_picture, talk_to_me, check_user_photo
from utils import close_keyboard, open_keyboard, replacement_smile
from subscription import subscribe, unsubscribe
from jobs import send_to_subscribe
from language import ru_language, en_language

logging.basicConfig(filename="bot.log", level= logging.INFO)


def main():
    mybot = Updater(settings.APY_KEY, use_context=True)
    
    jb = mybot.job_queue

    jb.run_repeating(send_to_subscribe, interval=10, first=0)
    dp = mybot.dispatcher
    
    dp.add_handler(game_namber)
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("cat", send_cat_picture))
    dp.add_handler(CommandHandler("user_photo", send_users_picture))
    dp.add_handler(CommandHandler("open", open_keyboard))
    dp.add_handler(CommandHandler("close", close_keyboard))
    dp.add_handler(CommandHandler("change_smile", replacement_smile))
    dp.add_handler(CommandHandler("subscribe", subscribe))
    dp.add_handler(CommandHandler("unsubscribe", unsubscribe))
    dp.add_handler(CommandHandler("russian_language", ru_language))
    dp.add_handler(CommandHandler("english_language", en_language))
    dp.add_handler(MessageHandler(Filters.regex("^(Прислать котика)$"), send_cat_picture))
    dp.add_handler(MessageHandler(Filters.regex("^(Прислать картинку)$"), send_users_picture))
    dp.add_handler(MessageHandler(Filters.regex("^(Перейти на Русский язык)$"), ru_language))
    dp.add_handler(MessageHandler(Filters.regex("^(Switch to English)$"), en_language))
    dp.add_handler(MessageHandler(Filters.photo, check_user_photo))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()
