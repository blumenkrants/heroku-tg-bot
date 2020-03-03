import pytest
from diplom.bot_diplom import *

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters, \
     RegexHandler
from datetime import timedelta, datetime
from telegram.ext import messagequeue as mq


# Почитать рефакторинг
# PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
#          'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}
#
# mybot = Updater("728852231:AAEZLnITK0BYNpAfQ4DCIC8CjpyiYLYUpIo", request_kwargs=PROXY)
# dp = mybot.dispatcher
# mybot.bot._msg_queue = mq.MessageQueue()
# mybot.bot._is_messages_queued_default = True




@pytest.fixture(scope='class', autouse=True)
def suite_data():
    print("\n> Suite setup")
    yield
    print("> Suite teardown")
    
@pytest.fixture(scope='function')
def case_data():
    print("   > Case setup")
    yield lol
    print("\n   > Case teardown")

@pytest.fixture(scope='function')
def case_data_2():
    a = greet_user(bot,update,user_data)
    yield a
