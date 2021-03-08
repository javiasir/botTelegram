from telegram.ext import Updater, CommandHandler
from auth import token

import logging

# Formato que tiene le mensaje
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger('SysBender')
# logger = logging.getLogger(__name__)

# Saludo del bot
def start(bot, update):
    logger.info('He recibido un comando start')
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Bot SysBender a su disposicion."
    )

if __name__ == '__main__':
    updater = Updater(token=token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()