from confi import TOKEN
from telegram.ext import Updater, MessageHandler, Dispatcher, CommandHandler
import botcons

def main():
    updater = Updater(TOKEN, use_context=True) 
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", botcons.start))
    dispatcher.add_handler(CommandHandler("allstars", botcons.stars))
    dispatcher.add_handler(CommandHandler("boyero", botcons.boyero))
    dispatcher.add_handler(CommandHandler("casiopea", botcons.casiopea))
    dispatcher.add_handler(CommandHandler("cazo", botcons.cazo))
    dispatcher.add_handler(CommandHandler("cygnet", botcons.cygnet))
    dispatcher.add_handler(CommandHandler("geminis", botcons.geminis))
    dispatcher.add_handler(CommandHandler("hydra", botcons.hydra))
    dispatcher.add_handler(CommandHandler("osamayor", botcons.osamayor))
    dispatcher.add_handler(CommandHandler("osamenor", botcons.osamenor))
    dispatcher.add_handler(CommandHandler("allcons", botcons.allcons))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
