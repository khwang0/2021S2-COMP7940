import telegram
from telegram.ext import Updater,CommandHandler,MessageHandler, Filters
import configparser
import logging
def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    #the logging helps you know when things do not work as expected
    updater = Updater(token=(config['TELEGRAM']['ACCESS_TOKEN']), use_context=True)
    dispatcher = updater.dispatcher
    updater.start_polling() # To start the bot, run:

    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)
    updater.idle()

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

if __name__ == '__main__':
    main()