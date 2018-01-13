import logging

from os import getenv
from telegram.ext import CommandHandler
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram import InlineQueryResult


TG_TOKEN = getenv("TELEGRAM_YOUTUBE_AUDIO_BOT_TOKEN")
YT_TOKEN = getenv("YOUTUBE_TELEGRAM_AUDIO_BOT_TOKEN")

logging.basicConfig(format='[ %(asctime)s ] %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# COMMAND HANDLERS
def start(bot, update):
    """Send a message when the command /start is issued."""
    bot.send_message(chat_id=update.message.chat_id,
                     text='Hi! Send a youtube link!')


def help(bot, update):
    """Send a message when the command /help is issued."""
    bot.send_message(chat_id=update.message.chat_id,
                     text='Send a youtube link!')


def echo(bot, update):
    """Echo the user message."""
    bot.send_message(chat_id=update.message.chat_id,
                     text=update.message.text)


def main():
    updater = Updater(token=TG_TOKEN)

    dispatcher = updater.dispatcher

    # Initialize Command handlers
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))

    # Initialize Message handlers
    dispatcher.add_handler(MessageHandler(Filters.text, echo))

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()