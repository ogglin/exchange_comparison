import asyncio
import concurrent.futures
import aiohttp

import requests
import json
import datetime

from random import randrange
from rest_framework.response import Response
from rest_framework.views import APIView

from exchange_comparison.utils import _query
from exchange_pairs.models import Settings
from aiohttp_proxy import ProxyConnector, ProxyType, open_connection

PRODUCERS_COUNT = 20
# proxys = [
#     'http://fgks.org/proxy/',
#     'http://myproxysite.org',
#     'http://circuitec.com.br/errors.php',
#     'http://www.blackreaction.com/proxy',
#     'http://m.ultear.ru/',
#     'http://van-bracht.nl/glype13/',
#     'http://kv39.com/',
#     'http://pdiperjuangan-diy.org/wp-includes/error.php',
#     'http://ukah.perdomocore.com/blink182/',
#     'http://kv39.com/',
#     'http://hidebuzz.com/',
#     'http://irlandec.ru/index.php',
#     'http://www.meuproxy.ninja/',
#     'http://unblockedproxy.herokuapp.com/',
#     'http://fly.paidoohost.com/',
# ]


proxys = [
    ['185.36.189.232', '16714', 'user53105', '3x7cyr'],
    ['193.111.152.90', '16714', 'user53105', '3x7cyr'],
    ['193.111.154.94', '16714', 'user53105', '3x7cyr'],
    ['193.111.152.191', '16714', 'user53105', '3x7cyr'],
    ['185.161.211.192', '16714', 'user53105', '3x7cyr'],
    ['185.20.185.157', '16714', 'user53105', '3x7cyr'],
    ['185.161.210.27', '16714', 'user53105', '3x7cyr'],
    ['193.111.152.110', '16714', 'user53105', '3x7cyr'],
    ['193.111.152.131', '16714', 'user53105', '3x7cyr'],
    ['185.161.210.125', '16714', 'user53105', '3x7cyr']
]


idex_tiker_all = None


async def get_idex_tiker_all():
    url = f'https://api.idex.io/v1/tickers'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            return json.loads(html)


async def get_idex_market(token, proxy):
    for tiker in idex_tiker_all:
        if tiker['market'].replace('-ETH', '') == token:
            return tiker
    return None
    # url = f'https://api.idex.io/v1/tickers?market={token}-ETH'
    # print(url + str(datetime.datetime.now()), proxy)
    # socks_url = 'http://' + prx[2] + ':' + prx[3] + '@' + prx[1] + ':' + prx[0]
    # print(url + str(datetime.datetime.now()), socks_url)
    # reader, writer = await open_connection(
    #     # socks_url='http://user:password@127.0.0.1:1080',
    #     socks_url=socks_url,
    #     host=url,
    #     port=80
    # )
    # request = (b"GET /ip HTTP/1.1\r\n"
    #            b"Host: api.idex.io\r\n"
    #            b"Connection: close\r\n\r\n")
    #
    # writer.write(request)
    # print(reader.read(-1))
    # return await json.loads(reader.read(-1))
    # connector = ProxyConnector(
    #     proxy_type=ProxyType.SOCKS5,
    #     host=proxy[0],
    #     port=16714,
    #     username='user53105',
    #     password='3x7cyr',
    #     rdns=True
    # )
    #
    # async with aiohttp.ClientSession(connector=connector) as session:
    #     async with session.get(url) as response:
    #         html = await response.text()
    #         return json.loads(html)


async def get_hotbit_depth(symbol, proxy):
    url = f"https://api.hotbit.io/api/v1/order.depth?interval=1e-8&&limit=20&market={symbol}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            return json.loads(html)


async def compare(asks, bids, where, to, symbols, percent):
    volume = 0
    ask_price = 0
    bid_price = 0
    full_price = 0
    count = 1
    w_symbol = ''
    t_symbol = ''

    if where == 'idex':
        w_symbol = symbols[0]
        t_symbol = symbols[1]
    if where == 'hotbit':
        w_symbol = symbols[1]
        t_symbol = symbols[0]

    if type(asks) is float:
        for bid in bids:
            if float(bid[0]) > (asks * percent / 100 + asks):
                full_price += float(bid[0])
                volume += float(bid[1])
                ask_price = asks
        bid_price = full_price / count

    if type(bids) is float:
        for ask in asks:
            if (float(ask[0]) + float(ask[0]) * percent / 100) < bids:
                full_price += float(ask[0])
                volume += float(ask[1])
                bid_price = bids
        ask_price = full_price / count

    if bid_price > ask_price > 0 and volume > 0:
        # print('/--------------------------')
        # print('/ ' + w_symbol + ' from ' + where + ' to ' + t_symbol + ' ' + to + ' /')
        # print('/ ask ' + str(ask_price) + ' bid ' + str(bid_price) + ' volume ' + str(volume) + ' /')
        # print('--------------------------/')
        return [w_symbol, where, ask_price, t_symbol, to, bid_price, volume, (bid_price-ask_price)/bid_price*100]
    else:
        return None


async def compare_markets(symbol, percent, proxy):
    compares = []
    idex_ticker = await get_idex_market(symbol[0], proxy)
    hotbit_depth = await get_hotbit_depth(symbol[1], proxy)
    if hotbit_depth['error'] is None and idex_ticker is not None:
        if idex_ticker['ask']:
            idex_ask = float(idex_ticker['ask'])
        else:
            idex_ask = None
        if idex_ticker['bid']:
            idex_bid = float(idex_ticker['bid'])
        else:
            idex_bid = None
        hotbit_asks = hotbit_depth['result']['asks']
        hotbit_bids = hotbit_depth['result']['bids']
        a = await compare(idex_ask, hotbit_bids, 'idex', 'hotbit', symbol, percent)
        if a is not None:
            compares.append(a)
        b = await compare(hotbit_asks, idex_bid, 'hotbit', 'idex', symbol, percent)
        if b is not None:
            compares.append(b)
    return compares


async def init(symbols, percent):
    global idex_tiker_all
    idex_tiker_all = await get_idex_tiker_all()
    async_tasks = []
    # print('start collect symbols ' + str(len(symbols)) + ' :' + str(datetime.datetime.now()))
    for symbol in symbols:
        rn = randrange(len(proxys))
        async_tasks.append(compare_markets(symbol, percent, proxys[rn]))
    # print('end  collect symbols: ' + str(len(async_tasks)) + str(datetime.datetime.now()))
    results = await asyncio.gather(*async_tasks)
    return results


class hotbit(APIView):
    # token_exchange_set()

    def get(self, request):
        # print('start: ' + str(datetime.datetime.now()))
        if request.GET['symbol']:
            url = "https://api.hotbit.io/api/v1/order.depth?interval=1e-8&&limit=20&market=" + request.GET['symbol']
        else:
            url = "https://api.hotbit.io/api/v1/order.depth?interval=1e-8&&limit=20&market="
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        # print('end: ' + str(datetime.datetime.now()))
        return Response(json.loads(response.text))

    def post(self, request):
        # print('start: ' + str(datetime.datetime.now()))
        setting = Settings.objects.all()[0]
        percent = setting.market_percent / 100 * setting.market_koef
        symbols = _query(f'SELECT mi.exch_direction, mh.symbol, mh.decimals FROM exchange_pairs '
                         f'LEFT JOIN module_hotbit mh ON mh.id = hotbit_id '
                         f'LEFT JOIN module_idex mi ON mi.id = idex_direction_id '
                         f'WHERE hotbit_id is not null and idex_direction_id is not null ORDER BY hotbit_id LIMIT 40;')
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop = asyncio.get_event_loop()
        loop.set_default_executor(concurrent.futures.ThreadPoolExecutor(max_workers=20))
        init_result = loop.run_until_complete(init(symbols, percent))
        compare_result = []
        for result in init_result:
            if len(result) > 0:
                compare_result.append(result[0])
        # print(json.dumps(compare_result))
        loop.close()
        # print('end: ' + str(datetime.datetime.now()))
        return Response(compare_result)
