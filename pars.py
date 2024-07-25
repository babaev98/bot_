from bs4 import BeautifulSoup
import requests

base = 'https://www.cbr.ru/currency_base/daily/'
html = requests.get(base).content
soup = BeautifulSoup(html, 'lxml')
div = soup.find('table', class_='data')
a = div.find_all('td')
currency_dictionary = {}

for i in range(0, len(a), 5):
    currency_dictionary[a[i].getText()] = tuple([a[i + x].getText() for x in range(1, 4)])


def values_():
    result = []
    for x in currency_dictionary:
        result.append(currency_dictionary[x][2])
    return result


print(values_())

