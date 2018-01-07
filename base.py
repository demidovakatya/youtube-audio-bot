from os import getenv
TOKEN = getenv("TELEGRAM_YOUTUBE_AUDIO_BOT_TOKEN")

from telegram.ext import Updater
updater = Updater(token=TOKEN)

dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='[ %(asctime) ] %(message)',
                    level=logging.INFO)


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text=update.message.text)

from telegram.ext import CommandHandler

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()