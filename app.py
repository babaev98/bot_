# telegram bot
from extensions import APIException, TelegramUser
import telebot
import pars
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help_(message: telebot.types.Message):
    bot.reply_to(message, f"Здравствуйте этот бот поможет вам узнать курс валют. Человек должен отправить"
                          f" сообщение боту в виде <имя валюты, цену которой он хочет узнать>, <имя валюты, в которой/"
                          f" надо узнать цену первой валюты>, <количество первой валюты>(через (,)\n"
                          f"При вводе команды /values выводится информация о всех доступных валютах")


@bot.message_handler(commands=['values'])
def values_(message: telebot.types.Message):
    pr = ''
    for _ in pars.name_currency():
        pr += '||' + _ + '||\n'
    bot.reply_to(message, f"{pr}")


@bot.message_handler(content_types=['text'])
def convert_(message: telebot.types.Message):
    values = message.text.split(', ')
    try:
        if len(values) != 3:
            raise APIException('Для вычесления требуется указать три аргумента. Введите команду /help или /start '
                               'для уточнения правил')
        quote, base, amount = values
        result = TelegramUser.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'{e}')
    except Exception as e:
        bot.reply_to(message, f'Возникла ошибка --{e}')
    else:
        bot.reply_to(message, f'Цена {amount} {quote} в {base} --> {round(result, 2)}')


bot.polling(non_stop=True)
