import logging

from os import getenv
from telegram.ext import CommandHandler
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import MessageHandler, Filters
# from telegram.ext import InlineQueryHandler, InlineQueryResult


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


# def inline_processing(bot, update):
#     query = update.inline_query.query
#     if not query:
#         return
#     result = update.message.text # for now
#     bot.answer_inline_query(update.inline_query.id, result)


def unknown(bot, update):
    """If someone tries to send unknown commands to the bot, this MessageHandler
    with a command filter will reply to all commands that were
    not recognized by the previous handlers."""
    bot.send_message(chat_id=update.message.chat_id,
                     text="I have no idea what you are talking about.")



def main():
    updater = Updater(token=TG_TOKEN)

    dispatcher = updater.dispatcher

    # Initialize Command handlers
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))

    # Initialize Message handlers
    dispatcher.add_handler(MessageHandler(Filters.text, echo))
    dispatcher.add_handler(MessageHandler(Filters.commands, unknown))

    # # Initialize Inline handlers
    # dispatcher.add_handler(InlineQueryHandler(inline_processing))

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()