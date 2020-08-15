import requests
import json

koef = 0.99


def get_cur():
    proxies = {
        'http': '46.102.73.244:53281',
        'https': '199.91.203.210:3128'
    }
    url = 'https://api.bancor.network/0.1/currencies/tokens?limit=9999&skip=0&fromCurrencyCode=ETH&includeTotal=true&orderBy=code&sortOrder=asc&skip=0'
    response = requests.get(url=url, proxies=proxies)
    jData = json.loads(response.content)['data']['page']
    for data in jData:
        print(data['id'])
        print(data['code'])
        print(data['name'])
        print(1/data['price'])
        print('/********************/')


