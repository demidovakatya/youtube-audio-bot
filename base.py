import logging

from os import getenv
from telegram.ext import CommandHandler
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import MessageHandler


TOKEN = getenv("TELEGRAM_YOUTUBE_AUDIO_BOT_TOKEN")

logging.basicConfig(format='[ %(asctime)s ] %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# COMMAND HANDLERS
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! Send a youtube link!')


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Send a youtube link.')


def echo(bot, update):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def main():
    updater = Updater(token=TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))

    dispatcher.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()