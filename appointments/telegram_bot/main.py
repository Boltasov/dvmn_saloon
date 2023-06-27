from environs import Env

from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler, ConversationHandler
from telegram.ext import MessageHandler, Filters

from appointments.telegram_bot.handlers import start, keyboard_menu_handler, keyboard_service_handler, \
    keyboard_master_handler, keyboard_date_handler, message_date_handler, keyboard_time_handler, message_time_handler, \
    phone_handler, cancel_handler
from appointments.telegram_bot.handlers import MENU, ASK_SERVICE, ASK_DATE, ASK_TIME, ASK_MASTER, ASK_PHONE

env = Env()
env.read_env()
API_TOKEN = env('TG_KEY')


def start_bot():
    updater = Updater(token=API_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler('start', start)
        ],
        states={
            MENU: [
                CallbackQueryHandler(callback=keyboard_menu_handler, pass_chat_data=True)
            ],
            ASK_SERVICE: [
                CallbackQueryHandler(callback=keyboard_service_handler, pass_chat_data=True)
            ],
            ASK_DATE: [
                CallbackQueryHandler(callback=keyboard_date_handler, pass_chat_data=True),
                MessageHandler(Filters.all, callback=message_date_handler, pass_chat_data=True)
            ],
            ASK_TIME: [
                CallbackQueryHandler(callback=keyboard_time_handler, pass_chat_data=True),
                MessageHandler(Filters.all, callback=message_time_handler, pass_chat_data=True)
            ],
            ASK_MASTER: [
                CallbackQueryHandler(callback=keyboard_master_handler, pass_chat_data=True)
            ],
            ASK_PHONE: [
                MessageHandler(Filters.all, callback=phone_handler, pass_chat_data=True)
            ]
        },
        fallbacks=[
            CommandHandler('cancel', cancel_handler)
        ]
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()
