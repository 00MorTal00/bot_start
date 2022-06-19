from email import message
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings
from handlers import greet_user, guess_number, send_cat_picture, talk_to_me

logging.basicConfig(filename="bot.log", level= logging.INFO)


def main():
    mybot = Updater(settings.APY_KEY, use_context=True)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("guess", guess_number))
    dp.add_handler(CommandHandler("cat", send_cat_picture))
    dp.add_handler(MessageHandler(Filters.regex("^(Прислать котика)$"), send_cat_picture))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()
