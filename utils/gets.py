import json
import random
import time

import aiohttp
from aiohttp_socks import SocksConnector

from exchange_pairs.utils import proxys

idex_api = 'cddba27a-916f-48e7-bad3-884c0869b627'


async def get_idex_depth(symbol, proxy):
    n = random.randint(0, 20)
    proxy = proxys[n]
    headers = {
        'IDEX-API-KEY': idex_api,
    }
    url = f"https://api.idex.io/v1/orderbook?market={symbol}-ETH&level=2&limit=20"
    socks_url = 'socks5://' + proxy[2] + ':' + proxy[3] + '@' + proxy[0] + ':' + proxy[1]
    connector = SocksConnector.from_url(socks_url)
    isTD = True
    while isTD:
        try:
            async with aiohttp.ClientSession(connector=connector, headers=headers) as session:
                async with session.get(url) as response:
                    html = await response.text()
                    jhtml = json.loads(html)
                    if 'sequence' in html:
                        isTD = False
                        return jhtml
                    elif 'code' in html:
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
                    if jhtml['ask']:
                        isTD = False
                        return jhtml
                    elif jhtml['error']:
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
