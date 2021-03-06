from telegram.ext import Updater, CommandHandler, MessageHandler
from auth import token

import logging
import subprocess

# Formato que tiene le mensaje
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger('SysBender')
# logger = logging.getLogger(__name__)

# Saludo del bot
def start(update, context):
    logger.info('He recibido un comando start')
    update.message.reply_text('Bot SysBender a su disposicion')

def ping(update, context):
    logger.info('El usuario desea buscar un equipo')

    saltos = str(context.args[0])
    ip = str(context.args[1])

    ping = subprocess.run(['ping', '-c', saltos, ip])

    if ping.returncode == 0:
        update.message.reply_text('Esta encendido')
        print('Esta encendido')
    else:
        update.message.reply_text('Esta apagado o no responde')
        print('Esta apagado o no responde')

def scanRange(update, context):
    user_id = update.effective_user['id']
    logger.info('El usuario quiere escanear un rango')

    rango = context.args[0]

    moviles = range(1,3)

    redes = {
        'moviles': moviles
    }

    # print(redes[rango])

    for c in redes[rango]:
        ip = '192.168.1.'+str(c)
        ping = subprocess.run(['ping', '-c', '1', ip])

        if ping.returncode == 0:
            print(ip, 'Encendido')
            context.bot.sendMessage(
                chat_id= user_id,
                parse_mode="HTML",
                text=f"{ip}, <b>Encendido</b>")
        else:
            print(ip, 'Apagado')
            context.bot.sendMessage(
                chat_id= user_id,
                parse_mode="HTML",
                text=f"{ip}, <b>Apagado</b>") 


def help(update, context):
    logger.info('El usuario ha pedido ayuda')
    update.message.reply_text("""
    /ping arg1 arg2 - Hacer ping a una direccion IP, siendo el arg1 - nº de saltos y arg2 - Direccion IP (NO DOMINIOS)
    """)
    

def main():
    # updater = Updater("token", use_context=True)
    updater = Updater(token=token)
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('ping', ping))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CommandHandler('scanrange', scanRange))

    # Start the Bot to receive the messages
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()