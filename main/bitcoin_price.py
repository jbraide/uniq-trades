import requests
import time

TICKER_API_URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'


times = []
prices = []


def get_bitcoin_price():
        response = requests.get(TICKER_API_URL)
        response_json = response.json()
        date = response_json['time']['updated']
        currency = response_json['bpi']['USD']['code']
        rate = response_json['bpi']['USD']['rate']
        
        date = date.encode('utf-8')
        times.append(date)
        prices.append(rate)
        time.sleep(10)

for _ in range(2):
    get_bitcoin_price()

print(times)