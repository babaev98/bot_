import requests
import json
base = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms=EUR&tsyms=RUB'
key_api = 'ef5ad86c74774af17854ec283d2cce531f5b0f3c3895c53354b74eb12f7292b7'

a = json.loads(requests.get(base).text)
print(type(a))