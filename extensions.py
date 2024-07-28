import requests
import json
import pars


class APIException(Exception):
    pass


class TelegramUser:
    @staticmethod
    def get_price(quote, base, amount):
        TelegramUser.error_parameter(quote, base, amount)
        quote = pars.pars()[quote]
        base = pars.pars()[base]
        result = json.loads(requests.get(f'https://min-api.cryptocompare.com/data/'
                                         f'pricemulti?fsyms={quote}&tsyms={base}').text)[quote]
        result = float(result[base]) * float(amount)
        return result

    @staticmethod
    def error_parameter(quote, base, amount):

        if quote == base:
            raise APIException('Невозможно переводить одуну и ту же валюту')

        if not (quote in pars.name_currency()):
            raise APIException(f'Валюты ({quote}) нет в нашем списке. Пожалуйста в ведите валюту из списка '
                               f'предложеных в команде /values')

        if not (base in pars.name_currency()):
            raise APIException(f'Валюты ({base}) нет в нашем списке. Пожалуйста в ведите валюту из списка '
                               f'предложеных в команде /values')

        try:
            amount = float(amount)

            if amount <= 0:
                raise APIException(f'В качестве последнего агрумента следует укачать количество желаемой валюты{base}')

        except ValueError:
            raise APIException(f'В качестве последнего агрумента следует укачать количество желаемой валюты{base}')
