from bs4 import BeautifulSoup
import requests
from config import BASE


def pars():
    html = requests.get(BASE).content
    soup = BeautifulSoup(html, 'lxml')
    div = soup.find('table', class_='data')
    a = div.find_all('td')
    currency_dictionary = {}

    for i in range(3, len(a), 5):
        currency_dictionary[a[i].getText()] = a[i-2].getText()
    currency_dictionary['Российский рубль'] = 'RUB'

    return currency_dictionary


def name_currency():
    currency_dictionary = pars()
    result = []

    for x in currency_dictionary:
        result.append(x)
    return result


if __name__ == "__main__":
    print(pars())
    print(name_currency())
