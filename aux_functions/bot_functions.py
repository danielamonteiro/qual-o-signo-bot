import logging
import telegram
from telegram.ext.dispatcher import run_async
import os

from aux_functions.check_date import CheckDate

class BotFunctions:

    @run_async
    def start_response(self, update, context):
        logging.info(f"ChatID [{update.effective_chat.id}] User Name: {update.effective_chat.first_name} {update.effective_chat.last_name}")
        logging.info(f"ChatID [{update.effective_chat.id}] User input: {update.message.text}")
        welcome_message = "🤖 Oi, tudo bem? Quer saber o signo de alguém? Só mandar aí a data no formato DD/MM 🤙"
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
        context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_message)
        logging.info(f"ChatID [{update.effective_chat.id}] BOT's response: {welcome_message}")
    
    @run_async
    def help_response(self, update, context):
        logging.info(f"ChatID [{update.effective_chat.id}] User Name: {update.effective_chat.first_name} {update.effective_chat.last_name}")
        logging.info(f"ChatID [{update.effective_chat.id}] User input: {update.message.text}")
        help_message = "É facinho usar, pô! Só mandar a data no formato DD/MM que eu te respondo com o signo! (mas manda só a data na mensagem, beleza? senão vai dar erro) 😁"
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
        context.bot.send_message(chat_id=update.effective_chat.id, text=help_message)
        logging.info(f"ChatID [{update.effective_chat.id}] BOT's response: {help_message}")
    
    @run_async
    def all_messages(self, update, context):
        logging.info(f"ChatID [{update.effective_chat.id}] User Name: {update.effective_chat.first_name} {update.effective_chat.last_name}")
        logging.info(f"ChatID [{update.effective_chat.id}] User input: {update.message['text']}")
        date = update.message["text"]
        date = CheckDate().check_valid_date(date)
        if not date:
            response_message = "A mensagem que você mandou não tem uma data válida. 😔"
        else:
            response_message = CheckDate().check_sign(date)
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
        context.bot.send_message(chat_id=update.effective_chat.id, text=response_message )
        logging.info(f"ChatID [{update.effective_chat.id}] BOT's response: {response_message }")