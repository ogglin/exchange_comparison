import json

import requests
import asyncio
import concurrent.futures
from random import randrange

import aiohttp
from rest_framework.response import Response
from rest_framework.views import APIView

from exchange_comparison.utils import _query
from exchange_pairs.models import Settings, ProfitExchanges, TrustedPairs
from .models import Hotbit

API_URL = 'https://api.hotbit.io/api/v1/allticker'

prices = []
PRODUCERS_COUNT = 20
idex_tiker_all = None
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


# Set Profits
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


async def compare(asks, bids, where, to, symbols, percent, currency):
    volume = 0
    ask_price = asks
    bid_price = bids
    full_price = 0
    w_symbol = ''
    t_symbol = ''
    count = 0

    if where != 'HOTBIT':
        w_symbol = symbols[0]
        t_symbol = symbols[1]
    if where == 'HOTBIT':
        w_symbol = symbols[1]
        t_symbol = symbols[0]

    if type(asks) is float:
        for bid in bids:
            if float(bid[0]) / currency > (asks * percent / 100 + asks):
                # print('bids', bid, float(bid[0]) / currency, '>', asks * percent / 100 + asks)
                count += 1
                full_price += float(bid[0]) / currency
                volume += float(bid[1]) / currency
        if count == 0:
            count = 1
        bid_price = full_price / count

    elif type(bids) is float:
        for ask in asks:
            if (float(ask[0]) / currency * percent / 100) + (float(ask[0]) / currency) < bids:
                # print('asks', ask, float(ask[0]) / currency, '<', bids * percent / 100 + bids)
                count += 1
                full_price += float(ask[0]) / currency
                volume += float(ask[1]) / currency
        if count == 0:
            count = 1
        ask_price = full_price / count

    if bid_price > ask_price > 0 and volume > 0:
        # print('/--------------------------')
        # print('ask type', type(asks))
        # print('bid type', type(bids))
        # print(where, asks, to, bids, symbols, percent, currency)
        # print('/ ' + w_symbol + ' from ' + where + ' to ' + t_symbol + ' ' + to + ' currency = ' + str(currency) + ' /')
        # print('/ buy ' + str(ask_price) + ' sell ' + str(bid_price) + ' volume ' + str(volume) + ' % ' + str(
        #     (bid_price - ask_price) / bid_price * 100) + ' /')
        # print('--------------------------/')
        return [w_symbol, where, ask_price, t_symbol, to, bid_price, volume, (bid_price - ask_price) / bid_price * 100]
    else:
        return None


async def compare_markets(symbol, percent, currency, proxy):
    compares = []
    hotbit_depth = await get_hotbit_depth(symbol[1], proxy)
    if 'BTC' in symbol[1]:
        pass
    else:
        currency = 1
    try:
        if hotbit_depth['error'] is None:
            hotbit_asks = hotbit_depth['result']['asks']
            hotbit_bids = hotbit_depth['result']['bids']
            if 'idex' in symbol[3]:
                idex_ticker = await get_idex_market(symbol[0], proxy)
                # print(idex_ticker)
                if idex_ticker is not None:
                    if idex_ticker['ask'] is not None:
                        idex_ask = float(idex_ticker['ask'])
                        # print('ask', idex_ask)
                        a = await compare(asks=idex_ask, bids=hotbit_bids, where='IDEX', to='HOTBIT', symbols=symbol,
                                          percent=percent, currency=currency)
                        if a is not None:
                            compares.append(a)
                    if idex_ticker['bid'] is not None:
                        idex_bid = float(idex_ticker['bid'])
                        # print('bid', idex_bid)
                        b = await compare(asks=hotbit_asks, bids=idex_bid, where='HOTBIT', to='IDEX', symbols=symbol,
                                          percent=percent, currency=currency)
                        if b is not None:
                            compares.append(b)
            if symbol[4] > 0:
                a = await compare(symbol[4], hotbit_bids, symbol[3].upper(), 'HOTBIT', symbol, percent, currency)
                if a is not None:
                    compares.append(a)
            if symbol[5] > 0:
                b = await compare(hotbit_asks, symbol[5], 'HOTBIT', symbol[3].upper(), symbol, percent, currency)
                if b is not None:
                    compares.append(b)
    except:
        pass
    return compares


async def init(symbols, percent, currency):
    global idex_tiker_all
    idex_tiker_all = await get_idex_tiker_all()
    async_tasks = []
    # print('start collect symbols ' + str(len(symbols)) + ' :' + str(datetime.datetime.now()))
    for symbol in symbols:
        rn = randrange(len(proxys))
        async_tasks.append(compare_markets(symbol, percent, currency, proxys[rn]))
    # print('end  collect symbols: ' + str(len(async_tasks)) + str(datetime.datetime.now()))
    results = await asyncio.gather(*async_tasks)
    return results


def save_profits():
    # print('start: ' + str(datetime.datetime.now()))
    setting = Settings.objects.all()[0]
    percent = setting.market_percent / 100 * setting.market_koef
    all_symbols = []
    symbols_idex = _query(f"SELECT mi.exch_direction, mh.symbol, mh.decimals,'idex', mi.highest_bid, mi.lowest_ask "
                          f"FROM exchange_pairs "
                          f"LEFT JOIN module_hotbit mh ON mh.id = hotbit_id "
                          f"LEFT JOIN module_idex mi ON mi.id = idex_direction_id "
                          f"WHERE hotbit_id is not null and idex_direction_id is not null ORDER BY hotbit_id;")
    all_symbols.extend(symbols_idex)
    symbols_bankor = _query(f"SELECT mb.exch_direction, mh.symbol, mh.decimals,'bankor', mb.highest_bid, mb.lowest_ask "
                            f"FROM exchange_pairs "
                            f"LEFT JOIN module_hotbit mh ON mh.id = hotbit_id "
                            f"LEFT JOIN module_bancor mb ON mb.id = bancor_direction_id "
                            f"WHERE hotbit_id is not null and bancor_direction_id is not null ORDER BY hotbit_id;")
    all_symbols.extend(symbols_bankor)
    symbols_kyber = _query(f"SELECT mk.exch_direction, mh.symbol, mh.decimals,'kyber', mk.highest_bid, mk.lowest_ask "
                           f"FROM exchange_pairs "
                           f"LEFT JOIN module_hotbit mh ON mh.id = hotbit_id "
                           f"LEFT JOIN module_kyber mk ON mk.id = kyber_direction_id "
                           f"WHERE hotbit_id is not null and kyber_direction_id is not null ORDER BY hotbit_id;")
    all_symbols.extend(symbols_kyber)
    symbols_uniswap = _query(
        f"SELECT mu.exch_direction, mh.symbol, mh.decimals, 'uniswap', mu.highest_bid, mu.lowest_ask, mu.tokenid "
        f"FROM exchange_pairs "
        f"LEFT JOIN module_hotbit mh ON mh.id = hotbit_id "
        f"LEFT JOIN module_uniswap mu ON mu.id = uniswap_direction_id "
        f"WHERE hotbit_id is not null and uniswap_direction_id is not null ORDER BY hotbit_id;")
    all_symbols.extend(symbols_uniswap)
    symbols_uniswap_one = _query(
        f"SELECT muo.exch_direction, mh.symbol, mh.decimals, 'uniswap_one', muo.highest_bid, muo.lowest_ask, muo.tokenid "
        f"FROM exchange_pairs LEFT JOIN module_hotbit mh ON mh.id = hotbit_id "
        f"LEFT JOIN module_uniswap_one muo ON muo.id = uniswap_one_direction_id "
        f"WHERE hotbit_id is not null and uniswap_one_direction_id is not null ORDER BY hotbit_id;")
    all_symbols.extend(symbols_uniswap_one)
    # try:
    currency = get_eth_btc()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop = asyncio.get_event_loop()
    loop.set_default_executor(concurrent.futures.ThreadPoolExecutor(max_workers=20))
    init_result = loop.run_until_complete(init(all_symbols, percent, currency))
    compare_result = []
    ProfitExchanges.objects.all().delete()
    buyurl = ''
    sellurl = ''
    for result in init_result:
        if len(result) > 0:
            pair = result[0][0]
            buy_name = result[0][1]
            buy = result[0][2]
            sell_name = result[0][4]
            sell = result[0][5]
            percent = result[0][7]
            tokenid = '0x0000000000000000000000000000000000000000000000000000000000000000'
            if result[0][1] == 'HOTBIT':
                buyurl = 'https://www.hotbit.io/exchange?symbol=' + result[0][0].replace('/', '_')
            if result[0][1] == 'IDEX':
                buyurl = 'https://exchange.idex.io/trading/' + result[0][0] + '-ETH'
            if result[0][1] == 'BANKOR':
                buyurl = 'https://www.bancor.network/?q=' + result[0][0]
            if result[0][1] == 'KYBER':
                buyurl = 'https://kyberswap.com/swap/ent-' + result[0][0]
            if result[0][1] == 'UNISWAP':
                buyurl = 'https://app.uniswap.org/#/swap?outputCurrency=' + str(result[0][6])
            if result[0][1] == 'UNISWAP_ONE':
                buyurl = 'https://exchange.idex.io/trading/' + str(result[0][6]) + '&use=v1'

            if result[0][4] == 'HOTBIT':
                sellurl = 'https://www.hotbit.io/exchange?symbol=' + result[0][3].replace('/', '_')
            if result[0][4] == 'IDEX':
                sellurl = 'https://exchange.idex.io/trading/' + result[0][3] + '-ETH'
            if result[0][4] == 'BANKOR':
                sellurl = 'https://www.bancor.network/?q=' + result[0][3]
            if result[0][4] == 'KYBER':
                sellurl = 'https://kyberswap.com/swap/ent-' + result[0][3]
            if result[0][4] == 'UNISWAP':
                sellurl = 'https://app.uniswap.org/#/swap?outputCurrency=' + str(result[0][6])
            if result[0][4] == 'UNISWAP_ONE':
                sellurl = 'https://exchange.idex.io/trading/' + str(result[0][6]) + '&use=v1'

            compare_result.append({'pair': pair, 'buy_name': buy_name, 'buy': buy, 'sell_name': sell_name, 'sell': sell,
                                   'percent': percent, 'tokenid': tokenid, 'buyurl': buyurl, 'sellurl': sellurl})
            pair = ProfitExchanges(pair=pair, buy_name=buy_name, buy=buy, sell_name=sell_name, sell=sell,
                                   percent=percent, tokenid=tokenid, buyurl=buyurl, sellurl=sellurl)

            pair.save()
    loop.close()
    return compare_result
    # print('end: ' + str(datetime.datetime.now()))
    # except:
    #     print('False')
    #     return {'error': 'False'}


# Set Prices
def set_prices(token, symbol, buy, sell, volume):
    prices.append({token: [symbol, buy, sell, volume]})


def get_eth_btc():
    # response = requests.get(f'https://api.hotbit.io/api/v1/market.status?market=ETH/BTC&period=10')
    # currency = float(json.loads(response.content)['result']['last'])
    currency = Settings.objects.all().values()[0]
    return currency['currency']
    # bids = json.loads(response.content)['result']['bids']
    # all_ask = 0
    # for ask in asks:
    #     # print(ask[0], ask[1])
    #     all_ask += float(ask[0])
    #
    # all_bid = 0
    # for bid in bids:
    #     # print(bid[0], bid[1])
    #     all_bid += float(bid[0])
    # return 1 / (all_ask / len(asks)), 1 / (all_bid / len(bids))


def get_ticker():
    currency = get_eth_btc()
    ask_btc = currency
    bit_btc = currency
    token = ''
    response = requests.get(url=API_URL)
    jData = sorted(json.loads(response.content)['ticker'], key=lambda x: x['symbol'], reverse=False)
    for data in jData:
        if 'USDT' not in data['symbol']:
            buy = float(data['buy'])
            sell = float(data['sell'])
            volume = float(data['vol'])
            token = data['symbol'].replace('_ETH', '').replace('_BTC', '')
            if (buy > 0 or sell > 0) and volume > 0:
                if 'ETH_BTC' in data['symbol']:
                    set_prices('BTC', 'ETH/BTC', 1 / buy, 1 / sell, volume)
                elif 'BTC' in data['symbol'] and 'ETH' not in data['symbol']:
                    buy = buy * ask_btc
                    sell = sell * ask_btc
                    set_prices(token, data['symbol'].replace('_BTC', '') + '/BTC', buy, sell, volume)
                else:
                    set_prices(token, data['symbol'].replace('_ETH', '') + '/ETH', buy, sell, volume)


def currencies_update(token, symbol, buy, sell, volume, contract, decimals):
    pair_id = Hotbit.objects.filter(symbol=symbol).values('id')
    if len(pair_id) > 0:
        Hotbit.objects.filter(id=pair_id[0]['id']).update(exch_direction=token, symbol=symbol, buy=buy, sell=sell,
                                                          volume=volume, contract=contract, decimals=decimals)
    else:
        pair = Hotbit(exch_direction=token, symbol=symbol, buy=buy, sell=sell, volume=volume, is_active=True,
                      contract=contract, decimals=decimals)
        pair.save()


def set_currencies():
    get_ticker()
    trusted_pair = list(TrustedPairs.objects.all().values_list())
    contract = None
    decimals = None
    for price in prices:
        token = list(price.keys())[0]
        p = list(list(price.values()))[0]
        for pair in trusted_pair:
            if token == pair[1]:
                contract = pair[2]
                decimals = pair[3]
        currencies_update(token, p[0], p[1], p[2], p[3], contract, decimals)
        contract = None
        decimals = None

# set_currencies()
