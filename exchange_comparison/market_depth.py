import json
import random
import time

import aiohttp
from aiohttp_socks import SocksConnector
from asgiref.sync import async_to_sync, sync_to_async

from exchange_comparison.utils import _query
import exchange_comparison.global_vars as gv

p_count = 0
cnt = 0


async def get_bilaxy_depth(symbol, cnt):
    url = f"https://newapi.bilaxy.com/v1/orderbook?pair={symbol}"
    socks_url = 'socks5://' + gv.proxys1[cnt][2] + ':' + gv.proxys1[cnt][3] + '@' + gv.proxys1[cnt][0] + ':' + \
                gv.proxys1[cnt][1]
    connector = SocksConnector.from_url(socks_url)
    try:
        async with aiohttp.ClientSession(connector=connector) as session:
            async with session.get(url) as response:
                html = await response.text()
                jhtml = json.loads(html)
                if 'timestamp' in html:
                    return jhtml
                else:
                    # print('bilaxy', symbol, jhtml)
                    if 'Not found pair' in html:
                        _query(f"""UPDATE bilaxy_markets SET "is_active" = 'f' WHERE "market" LIKE '%{symbol}%';""")
                    return None
    except Exception as exc:
        print(exc, gv.proxys1[cnt])
        return None


async def get_idex_depth(symbol, cnt):
    global p_count
    if cnt > 39:
        cnt -= 20
    if cnt > 19:
        cnt -= 20
    header = {
        'IDEX-API-KEY': gv.idex_apis[cnt],
    }
    url = f"https://api.idex.io/v1/orderbook?market={symbol}&level=2&limit=20"
    socks_url = 'socks5://' + gv.proxys2[cnt][2] + ':' + gv.proxys2[cnt][3] + '@' + gv.proxys2[cnt][0] + ':' + \
                gv.proxys2[cnt][1]
    connector = SocksConnector.from_url(socks_url)
    try:
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
    except Exception as exc:
        print(exc, gv.proxys2[cnt])
        return None


async def get_hitbtc_depth(symbol, cnt):
    url = f"https://api.hitbtc.com/api/2/public/orderbook/{symbol.replace('/', '')}"
    socks_url = 'socks5://' + gv.proxys3[cnt][2] + ':' + gv.proxys3[cnt][3] + '@' + gv.proxys3[cnt][0] + ':' + \
                gv.proxys3[cnt][1]
    connector = SocksConnector.from_url(socks_url)
    try:
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
    except Exception as exc:
        print(exc, gv.proxys3[cnt])
        return None


async def get_hotbit_depth(symbol, cnt):
    url = f"https://api.hotbit.io/api/v1/order.depth?interval=1e-8&&limit=20&market={symbol}"
    socks_url = 'socks5://' + gv.proxys4[cnt][2] + ':' + gv.proxys4[cnt][3] + '@' + gv.proxys4[cnt][0] + ':' + \
                gv.proxys4[cnt][1]
    connector = SocksConnector.from_url(socks_url)
    try:
        async with aiohttp.ClientSession(connector=connector) as session:
            async with session.get(url) as response:
                html = await response.text()
                jhtml = json.loads(html)
                if jhtml['error'] is None:
                    return jhtml['result']
                elif jhtml['error']:
                    print('hotbit', symbol, jhtml['error'])
                    if 'market not exist' in html:
                        _query(f"""UPDATE hotbit_markets SET "is_active" = 'f' WHERE "market" LIKE '%{symbol}%';""")
                    return None
                else:
                    return None
    except Exception as exc:
        print(exc, gv.proxys4[cnt])
        return None


def get_proxy():
    global cnt
    cnt = cnt + 1
    socks_url = 'socks5://' + gv.proxys[cnt][2] + ':' + gv.proxys[cnt][3] + '@' + gv.proxys[cnt][0] + ':' + \
                gv.proxys[cnt][1]
    return socks_url
    # proxy = proxys[n]
    # print(proxy)
