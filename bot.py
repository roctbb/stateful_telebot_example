import telebot
from infrastructure import *
from handlers import *
from helpers import *

@bot.message_handler(content_types=['text', 'sticker', 'video', 'photo', 'voice'])
def process_message(message):
    user = get_or_create_user(message.chat.id)
    state = user['state']

    if state in handlers:
        handlers[state](user, message)

bot.polling()
