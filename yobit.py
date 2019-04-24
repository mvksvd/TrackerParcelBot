import requests

def get_btc():
    url = 'https://yobit.net/api/2/btc_usd/ticker'
    responce = requests.get(url).json()
    price = responce['ticker']['last']
    return str(price) + ' usd'


print(get_btc())