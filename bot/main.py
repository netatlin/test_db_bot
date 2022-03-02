import telebot
from telebot import types
import random
import logging
from json_formatter import JSONFormatter
from config import TOKEN
from sqlalchemy.orm import Session
from models import UserMessages
from config import conn

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
loggingStreamHandler = logging.StreamHandler()
loggingStreamHandler.setFormatter(JSONFormatter())
logger.addHandler(loggingStreamHandler)
logger.info({"message": 'Bot is starting'})

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    """Логика при запуске бота"""
    bot.send_message(message.chat.id, 'Привет', parse_mode="HTML")


@bot.message_handler()
def my_orders_message(message):
    """Логика при отправке сообщения в бота"""

    session = Session(conn, future=True)
    with session:
        message_to_add = UserMessages(user_id=message.chat.id, body=message.text)
        session.add(message_to_add)
        session.commit()
        bot.send_message(message.chat.id, 'Записал', reply_to_message_id=message.id)


bot.polling(none_stop=True)