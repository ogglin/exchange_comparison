import json
import random
import time

import aiohttp
from aiohttp_socks import SocksConnector

from exchange_comparison.utils import _query
from exchange_pairs.utils import proxys

# 'cddba27a-916f-48e7-bad3-884c0869b627',
idex_apis = [
    'cddba27a-916f-48e7-bad3-884c0869b627',
    '5e7810c3-bcad-4467-8069-630e52752806',
    '6ae1849c-c8eb-46f8-a735-94b10ddcea2d',
    'faa69304-22a7-48fb-83fd-b5f5a372b758',
    '93872815-45fa-46a7-a1ed-b9d7f2200ec3',
    'd590c3cb-d35d-47dd-b38d-c0b91a124f11',
    '6a59e1d2-691f-4858-bb71-3c9a6297c82f',
    '14936906-d513-444c-8e06-10d53f5f3b3c',
    '5fb56407-582a-4132-9a92-a7e93684e81a',
    '6692e791-a7c6-45f3-9930-6a6c695a5689',
    '4f19b13d-aa3e-48c0-8cfc-9ad17ddc8266',
    '03b8d5fb-89a0-45a7-b615-6a2aa6f8570b',
    '28625e1b-eb3f-4780-97f7-6db1ca4047e6',
    '6bfd2f58-ece3-41fe-af8a-3209a4e6ae55',
    '08288b4c-5a79-47eb-bd23-a29034c80a06',
    '0ec315f5-3fd9-4c75-9b0a-3ae8af0adf9f',
    'cd8052e2-5286-48f8-a33e-873f475de0cd',
    '479e9cb9-d5c8-447f-ae6f-7b4cf38f47e0',
    'b2867fa3-f57a-4749-850a-a0db4217dcc1',
    'a094c2e0-e518-41cb-8992-e9ea225a5bda',
]

p_count = 0


async def get_idex_depth(symbol, cnt):
    global p_count
    proxy = proxys[cnt]
    print(proxy)
    if cnt > 39:
        cnt -= 20
    if cnt > 19:
        cnt -= 20
    header = {
        'IDEX-API-KEY': idex_apis[cnt],
    }
    url = f"https://api.idex.io/v1/orderbook?market={symbol}&level=2&limit=20"
    socks_url = 'socks5://' + proxy[2] + ':' + proxy[3] + '@' + proxy[0] + ':' + proxy[1]
    connector = SocksConnector.from_url(socks_url)
    # try:
    async with aiohttp.ClientSession(connector=connector, headers=header) as session:
        async with session.get(url) as response:
            html = await response.text()
            jhtml = json.loads(html)
            p_count += 1
            if 'sequence' in html:
                return jhtml
            elif 'code' in html:
                if jhtml['code'] != 'MARKET_NOT_FOUND':
                    print('IDEX', symbol, jhtml['code'])
                return None
    # except:
    #     pass


async def get_hitbtc_depth(symbol, proxy):
    print(proxy)
    url = f"https://api.hitbtc.com/api/2/public/orderbook/{symbol.replace('/', '')}"
    socks_url = 'socks5://' + proxy[2] + ':' + proxy[3] + '@' + proxy[0] + ':' + proxy[1]
    connector = SocksConnector.from_url(socks_url)
    # try:
    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get(url) as response:
            html = await response.text()
            jhtml = json.loads(html)
            if 'ask' in html:
                return jhtml
            elif 'error' in html:
                print('hitbtc', jhtml['error'])
                return None
            else:
                return None
    # except:
    #     pass


async def get_hotbit_depth(symbol, proxy):
    print(proxy)
    url = f"https://api.hotbit.io/api/v1/order.depth?interval=1e-8&&limit=20&market={symbol}"
    socks_url = 'socks5://' + proxy[2] + ':' + proxy[3] + '@' + proxy[0] + ':' + proxy[1]
    connector = SocksConnector.from_url(socks_url)
    # try:
    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get(url) as response:
            html = await response.text()
            jhtml = json.loads(html)
            if jhtml['error'] is None:
                return jhtml['result']
            elif jhtml['error']:
                print('hotbit', symbol, jhtml['error'])
                if 'market not exist' in html:
                    _query(f"""UPDATE hotbit_markets SET "is_active" = 'f' WHERE "market" LIKE '%{symbol}%'""")
                return None
            else:
                return None
    # except:
    #     pass


async def get_bilaxy_depth(symbol, proxy):
    print(proxy)
    url = f"https://newapi.bilaxy.com/v1/orderbook?pair={symbol}"
    socks_url = 'socks5://' + proxy[2] + ':' + proxy[3] + '@' + proxy[0] + ':' + proxy[1]
    connector = SocksConnector.from_url(socks_url)
    # try:
    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get(url) as response:
            html = await response.text()
            jhtml = json.loads(html)
            if 'timestamp' in html:
                return jhtml
            else:
                print('bilaxy', symbol, jhtml)
                if 'Not found pair' in html:
                    _query(f"""UPDATE bilaxy_markets SET "is_active" = 'f' WHERE "market" LIKE '%{symbol}%'""")
                return None
    # except:
    #     pass


def get_proxy():
    n = random.randint(0, 20)
    print(n)
    # proxy = proxys[n]
    # print(proxy)


if __name__ == "__main__":
    get_proxy()
