from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from aux_functions.bot_functions import BotFunctions


class BotCommands:
    def __init__(self, bot_updater, bot_dispatcher):
        bot_functions = BotFunctions()

        start_handler = CommandHandler('start', bot_functions.start_response)
        bot_dispatcher.add_handler(start_handler)

        help_handler = CommandHandler('help', bot_functions.help_response)
        bot_dispatcher.add_handler(help_handler)

        all_commands_handler = MessageHandler(Filters.command, bot_functions.all_messages)
        bot_dispatcher.add_handler(all_commands_handler)

        all_messages_handler = MessageHandler(Filters.text, bot_functions.all_messages)
        bot_dispatcher.add_handler(all_messages_handler)