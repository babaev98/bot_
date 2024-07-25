# telegram bot

import telebot as tl
import pars

TOKEN = '7257276665:AAFMuQrB4QVz9oEHMVNS40N1ss76Nq0iFVc'

bot = tl.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def handle_docs_hello(message):
    bot.reply_to(message, f"Здравствуйте этот бот поможет вам узнать курс валют. Человек должен отправить"
                          f" сообщение боту в виде <имя валюты, цену которой он хочет узнать> <имя валюты, в которой/"
                          f" надо узнать цену первой валюты> <количество первой валюты>\n"
                          f"При вводе команды /values выводится информация о всех доступных валютах")


@bot.message_handler(commands=['values'])
def handle_docs_hello(message):
    pr = '||'
    for _ in pars.values_():
        pr += _ + '|| '
    bot.reply_to(message, f"{pr}")


bot.polling(non_stop=True)
