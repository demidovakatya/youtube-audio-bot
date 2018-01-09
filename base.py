import logging

from os import getenv
from telegram.ext import CommandHandler
from telegram.ext import Updater
from telegram.ext import MessageHandler


TOKEN = getenv("TELEGRAM_YOUTUBE_AUDIO_BOT_TOKEN")

logging.basicConfig(format='[ %(asctime) ] %(message)', level=logging.INFO)


# COMMAND HANDLERS
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


def main():
    updater = Updater(token=TOKEN)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()


if __name__ == '__main__':
    main()