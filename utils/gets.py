import json
import random
import time

import aiohttp
from aiohttp_socks import SocksConnector

from exchange_pairs.utils import proxys

# 'cddba27a-916f-48e7-bad3-884c0869b627',
idex_apis = [
    'af40529c-b446-4a96-8254-c4775a49c547',
    '7bc4c104-96d0-49e1-a5a8-8ccde84b00e5',
    'c4639122-b828-421a-af39-c6b2a4979fc3',
    '80851287-ce30-4703-8f87-17bce116d7a6',
    '84d02a17-eeba-47b3-905b-6862b56c293c',
    '07efd3e1-b67d-43b1-a8f4-69bd96f159e7',
    '7c8ee5c1-21a4-4fba-98ae-27448d76458d'
]

p_count = 0


async def get_idex_depth(symbol, proxy):
    global p_count
    n = random.randint(0, 6)
    # proxy = proxys[n]
    header = {
        # 'IDEX-API-KEY': idex_apis[n],
    }
    url = f"https://api.idex.io/v1/orderbook?market={symbol}-ETH&level=2&limit=20"
    socks_url = 'socks5://' + proxy[2] + ':' + proxy[3] + '@' + proxy[0] + ':' + proxy[1]
    connector = SocksConnector.from_url(socks_url)
    isTD = True
    while isTD:
        try:
            async with aiohttp.ClientSession(connector=connector, headers=header) as session:
                async with session.get(url) as response:
                    html = await response.text()
                    jhtml = json.loads(html)
                    p_count += 1
                    if 'sequence' in html:
                        isTD = False
                        print(p_count, symbol, proxy)
                        print(jhtml)
                        return jhtml
                    elif 'code' in html:
                        print(p_count, symbol, proxy)
                        print(jhtml['code'])
                        isTD = False
                        return None
        except:
            time.sleep(2)


async def get_hotbit_depth(symbol, proxy):
    url = f"https://api.hotbit.io/api/v1/order.depth?interval=1e-8&&limit=20&market={symbol}"
    socks_url = 'socks5://' + proxy[2] + ':' + proxy[3] + '@' + proxy[0] + ':' + proxy[1]
    connector = SocksConnector.from_url(socks_url)
    isTD = True
    while isTD:
        try:
            async with aiohttp.ClientSession(connector=connector) as session:
                async with session.get(url) as response:
                    html = await response.text()
                    jhtml = json.loads(html)
                    if jhtml['error'] is None:
                        isTD = False
                        return jhtml['result']
                    elif jhtml['error']:
                        isTD = False
                        print(jhtml['error'])
                        return None
                    else:
                        isTD = True
        except:
            time.sleep(1)


async def get_hitbtc_depth(symbol, proxy):
    url = f"https://api.hitbtc.com/api/2/public/orderbook/{symbol.replace('/', '')}"
    socks_url = 'socks5://' + proxy[2] + ':' + proxy[3] + '@' + proxy[0] + ':' + proxy[1]
    connector = SocksConnector.from_url(socks_url)
    isTD = True
    while isTD:
        try:
            async with aiohttp.ClientSession(connector=connector) as session:
                async with session.get(url) as response:
                    html = await response.text()
                    jhtml = json.loads(html)
                    if 'ask' in html:
                        isTD = False
                        return jhtml
                    elif 'error' in html:
                        isTD = False
                        print(jhtml['error'])
                        return None
                    else:
                        isTD = True
        except:
            time.sleep(1)


def get_proxy():
    n = random.randint(0, 20)
    print(n)
    # proxy = proxys[n]
    # print(proxy)


if __name__ == "__main__":
    get_proxy()
