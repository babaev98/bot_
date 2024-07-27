from bs4 import BeautifulSoup
import requests

base = 'https://www.cbr.ru/currency_base/daily/'
html = requests.get(base).content
soup = BeautifulSoup(html, 'lxml')
div = soup.find('table', class_='data')
a = div.find_all('td')


def pars():
    currency_dictionary = {}
    for i in range(1, len(a), 5):
        currency_dictionary[a[i].getText()] = a[i+2].getText()
        currency_dictionary['RUB'] = 'Российский рубль'
    return currency_dictionary


def name_currency():
    currency_dictionary = pars()
    result = []
    for x in currency_dictionary:
        result.append(currency_dictionary[x])
    return result


if __name__ == "__main__":
    print(pars())
    print(name_currency())
