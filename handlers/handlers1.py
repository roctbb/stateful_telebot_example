from .decorator import *
from infrastructure import *

@state_handler('start')
def send_start_info(user, message):
    user['state'] = "register:awaiting_name"
    bot.send_message(message.chat.id, "Введи имя:")