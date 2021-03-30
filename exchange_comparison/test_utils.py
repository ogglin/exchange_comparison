import json

import requests
from asgiref.sync import sync_to_async

from exchange_pairs.models import TrustedPairs


def get_symbols():
    url = ('https://api.hitbtc.com/api/2/public/symbol')
    symbols = json.loads(requests.get(url=url).text)
    tsymbols = TrustedPairs.objects.all()
    print(len(symbols))
    for symbol in symbols:
        token = symbol['baseCurrency']
        try:
            tsymbol = tsymbols.get(tsymbol=token)
            print(tsymbol)
        except:
            print('new', token)
            pair = TrustedPairs(token=token, is_active=False, tsymbol=token, contract=None)
            pair.save()
    #     # if 'USDT' in symbol['']
    #     print(symbol)


@sync_to_async
def test_start():
    get_symbols()

