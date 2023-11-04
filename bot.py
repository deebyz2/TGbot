import telebot
import wikipedia
wikipedia.set_lang('ru')

import settings
bot = telebot.TeleBot(settings.API)

@bot.message_handler(content_types=['text'])
def talk(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'и тебе привет, пиши, что хочешь узнать')
    elif message.text == 'Хорошо':
        bot.send_message(message.chat.id, "Отлично")
    else:
        low_r = message.text
        low_r = low_r.replace(" ", "_")
        page = wikipedia.page(low_r)
        bot.send_message(message.chat.id, page.summary)

bot.polling(none_stop=True)