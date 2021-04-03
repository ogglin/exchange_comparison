import json

import requests
from asgiref.sync import sync_to_async

from exchange_pairs.models import TrustedPairs
from hitbtc_module.models import Hitbtc
from hotbit_module.models import Hotbit


def get_symbols():
    url = ('https://api.hitbtc.com/api/2/public/symbol')
    symbols = json.loads(requests.get(url=url).text)
    hsymbols = Hitbtc.objects.all()
    print(len(symbols))
    for symbol in symbols:
        token = symbol['baseCurrency']

        try:
            hsymbol = hsymbols.get(symbol=symbol['id'])
            if hsymbol.tsymbol is None:
                hsymbol.tsymbol = token
                hsymbol.save()
            print(hsymbol)
        except:
            print('new', token)
            pair = Hitbtc(symbol=symbol['id'], is_active=False, tsymbol=token, exch_direction=token)
            pair.save()
    #     # if 'USDT' in symbol['']
    #     print(symbol)


def get_symbols_hotbit():
    url = ('https://api.hotbit.io/api/v1/market.list')
    symbols = json.loads(requests.get(url=url).text)['result']
    hsymbols = Hotbit.objects.all()
    print(len(symbols))
    for symbol in symbols:
        token = symbol['stock']

        try:
            hsymbol = hsymbols.get(symbol=symbol['name'])
            if hsymbol.tsymbol is None:
                hsymbol.tsymbol = token
                hsymbol.save()
            print(symbol['name'])
        except:
            print('new', symbol['name'])
            pair = Hotbit(symbol=symbol['name'], is_active=False, tsymbol=token, exch_direction=token)
            pair.save()
    #     # if 'USDT' in symbol['']
    #     print(symbol)


@sync_to_async
def test_start():
    get_symbols_hotbit()
