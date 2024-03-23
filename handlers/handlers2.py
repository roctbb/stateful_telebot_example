from .decorator import *
from infrastructure import *

@state_handler('register:awaiting_name')
def send_start_info(user, message):
    if message.text:
        user['state'] = "register:awaiting_age"
        user['name'] = message.text
        bot.send_message(message.chat.id, "Введи введи возраст:")
    else:
        bot.send_message(message.chat.id, "Введи имя:")
