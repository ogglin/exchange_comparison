import asyncio
import concurrent.futures
import datetime
import json
import time
import random
from random import randrange

import aiohttp
import requests
from aiohttp_socks import SocksConnector, SocksVer

from exchange_comparison.utils import _query
from exchange_pairs.models import Settings, ProfitExchanges, TrustedPairs
from .models import Hotbit

API_URL = 'https://api.hotbit.io/api/v1/allticker'

prices = []
PRODUCERS_COUNT = 20
idex_tiker_all = None
proxys = [
    ['193.111.152.28', '16881', 'user53105', '3x7cyr'],
    ['185.161.211.209', '16881', 'user53105', '3x7cyr'],
    ['193.111.155.237', '16881', 'user53105', '3x7cyr'],
    ['193.111.152.168', '16881', 'user53105', '3x7cyr'],
    ['185.20.187.218', '16881', 'user53105', '3x7cyr'],
    ['193.111.154.67', '16881', 'user53105', '3x7cyr'],
    ['185.161.209.185', '16881', 'user53105', '3x7cyr'],
    ['185.36.189.145', '16881', 'user53105', '3x7cyr'],
    ['185.36.190.130', '16881', 'user53105', '3x7cyr'],
    ['193.111.152.90', '16881', 'user53105', '3x7cyr'],
    ['213.32.84.200', '11565', 'user53105', '3x7cyr'],
    ['213.32.84.143', '11565', 'user53105', '3x7cyr'],
    ['79.137.15.162', '11565', 'user53105', '3x7cyr'],
    ['213.32.84.176', '11565', 'user53105', '3x7cyr'],
    ['147.135.175.235', '11565', 'user53105', '3x7cyr'],
    ['178.32.67.197', '11565', 'user53105', '3x7cyr'],
    ['178.32.67.151', '11565', 'user53105', '3x7cyr'],
    ['213.32.84.202', '11565', 'user53105', '3x7cyr'],
    ['147.135.206.67', '11565', 'user53105', '3x7cyr'],
    ['213.32.84.46', '11565', 'user53105', '3x7cyr'],
]


# Set Profits
async def get_idex_tiker_all():
    url = f'https://api.idex.io/v1/tickers'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            return json.loads(html)


async def get_idex_market(token):
    for tiker in idex_tiker_all:
        if tiker['market'].replace('-ETH', '') == token:
            return tiker
    return None


async def get_hotbit_depth(symbol, proxy):
    url = f"https://api.hotbit.io/api/v1/order.depth?interval=1e-8&&limit=20&market={symbol}"
    socks_url = 'socks5://' + proxy[2] + ':' + proxy[3] + '@' + proxy[0] + ':' + proxy[1]
    connector = SocksConnector.from_url(socks_url)
    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get(url) as response:
            html = await response.text()
            return json.loads(html)


async def compare(asks, bids, where, to, symbols, percent, currency, cnt):
    # print('---------/ ', cnt, currency, '/---------')
    # print(where, asks, to, bids, symbols, percent, currency)
    volume = 0
    ask_price = asks
    bid_price = bids
    full_price = 0
    full_volume = 0
    w_symbol = ''
    t_symbol = ''
    count = 0
    token_id = symbols[6]
    token_volume = symbols[7]

    if 'HOTBIT' not in where:
        w_symbol = symbols[0]
        t_symbol = symbols[1]
    if 'HOTBIT' in where:
        w_symbol = symbols[1]
        t_symbol = symbols[0]

    if type(asks) is float:
        for bid in bids:
            if float(bid[0]) / currency > (asks * percent / 100 + asks) and full_volume <= 1:
                count += 1
                # full_price += float(bid[0]) / currency
                full_volume += float(bid[1]) * float(bid[0]) / currency
                bid_price = float(bid[0]) / currency
        if count == 0:
            count = 1

    elif type(bids) is float:
        for ask in asks:
            if (float(ask[0]) / currency * percent / 100) + (float(ask[0]) / currency) < bids and full_volume <= 1:
                count += 1
                # full_price += float(ask[0]) / currency
                ask_price = float(ask[0]) / currency
                full_volume += float(ask[1]) * float(ask[0]) / currency
        if count == 0:
            count = 1

    if bid_price > 0 and ask_price > 0 and token_volume >= 0.1 and full_volume > 0.8:
        # print('/--------------------------')
        # print('token vol:', token_volume)
        # print('full vol:', full_volume)
        # print('vol:', volume)
        # print(where, asks, to, bids, symbols, percent, currency)
        # print('/ ' + w_symbol + ' from ' + where + ' to ' + t_symbol + ' ' + to + ' currency = ' + str(currency) + ' /')
        # print('/ buy ' + str(ask_price) + ' sell ' + str(bid_price) + ' volume ' + str(volume) + ' % ' + str(
        #     (bid_price - ask_price) / bid_price * 100) + ' /')
        # print('--------------------------/')
        return [w_symbol, where, ask_price, t_symbol, to, bid_price, volume, (bid_price - ask_price) / bid_price * 100,
                token_id]
    else:
        return None


async def compare_markets(symbol, percent, currency, proxy, cnt):
    compares = []
    isTD = True
    while isTD:
        try:
            hotbit_depth = await get_hotbit_depth(symbol[1], proxy)
            isTD = False
        except:
            time.sleep(1)
            isTD = True
    exchange_name = 'HOTBIT'
    if 'BTC' in symbol[1]:
        exchange_name = 'HOTBIT / BTC'
    else:
        currency = 1
    if 'error' in hotbit_depth:
        hotbit_asks = hotbit_depth['result']['asks']
        hotbit_bids = hotbit_depth['result']['bids']
        if 'idex' in symbol[3]:
            idex_ticker = await get_idex_market(symbol[0])
            # print(idex_ticker)
            if idex_ticker is not None and float(idex_ticker['quoteVolume']) > 1:
                if idex_ticker['ask'] is not None:
                    idex_ask = float(idex_ticker['ask'])
                    # print('ask', idex_ask)
                    a = await compare(asks=idex_ask, bids=hotbit_bids, where='IDEX', to=exchange_name, symbols=symbol,
                                      percent=percent, currency=currency, cnt=cnt)
                    if a is not None:
                        compares.append(a)
                if idex_ticker['bid'] is not None:
                    idex_bid = float(idex_ticker['bid'])
                    # print('bid', idex_bid)
                    b = await compare(asks=hotbit_asks, bids=idex_bid, where=exchange_name, to='IDEX', symbols=symbol,
                                      percent=percent, currency=currency, cnt=cnt)
                    if b is not None:
                        compares.append(b)
        else:
            if symbol[5] > 0:
                a = await compare(symbol[5], hotbit_bids, symbol[3].upper(), exchange_name, symbol, percent, currency,
                                  cnt)
                if a is not None:
                    compares.append(a)
            if symbol[4] > 0:
                b = await compare(hotbit_asks, symbol[4], exchange_name, symbol[3].upper(), symbol, percent, currency,
                                  cnt)
                if b is not None:
                    compares.append(b)
    else:
        print(hotbit_depth)
    return compares


async def init(symbols, percent, currency):
    global idex_tiker_all
    idex_tiker_all = await get_idex_tiker_all()
    async_tasks = []
    # print('start collect symbols ' + str(len(symbols)) + ' :' + str(datetime.datetime.now()))
    cnt = 0
    for symbol in symbols:
        async_tasks.append(compare_markets(symbol, percent, currency, proxys[cnt], cnt))
        cnt += 1
        if cnt >= len(proxys):
            cnt = 0
    # print('end  collect symbols: ' + str(len(async_tasks)) + str(datetime.datetime.now()))
    results = await asyncio.gather(*async_tasks)
    return results


def hotbit_profits():
    setting = Settings.objects.all()[0]
    percent = setting.market_percent / 100 * setting.market_koef
    ''', uniswap_one as (SELECT muo.exch_direction, mh.symbol, mh.decimals, "
                         f"'uniswap_one' as site, muo.highest_bid, muo.lowest_ask, lower(muo.tokenid) token_id, "
                         f"muo.volume FROM exchange_pairs LEFT JOIN module_hotbit mh ON mh.id = hotbit_id "
                         f"LEFT JOIN module_uniswap_one muo ON muo.id = exchange_pairs.uniswap_one_direction_id "
                         f"WHERE hotbit_id IS NOT NULL AND uniswap_one_direction_id IS NOT NULL  AND muo.volume >=1 "
                         f"ORDER BY hotbit_id) 
                         UNION ALL SELECT * FROM uniswap_one'''
    all_symbols = _query(f"WITH idex as (SELECT mi.exch_direction, mh.symbol, mh.decimals, 'idex' as site, "
                         f"mi.highest_bid, mi.lowest_ask, mi.token_id, mi.volume FROM exchange_pairs "
                         f"LEFT JOIN module_hotbit mh ON mh.id = hotbit_id "
                         f"LEFT JOIN module_idex mi ON mi.id = idex_direction_id "
                         f"WHERE hotbit_id is not null and idex_direction_id is not null and mi.volume >= 1 "
                         f"ORDER BY hotbit_id), kyber as (SELECT mk.exch_direction, mh.symbol, mh.decimals, "
                         f"'kyber' as site, mk.highest_bid, mk.lowest_ask, mk.token_id, mk.volume FROM exchange_pairs "
                         f"LEFT JOIN module_hotbit mh ON mh.id = hotbit_id "
                         f"LEFT JOIN module_kyber mk ON mk.id = kyber_direction_id "
                         f"WHERE hotbit_id is not null and kyber_direction_id is not null and mk.volume >= 1 "
                         f"ORDER BY hotbit_id), uniswap as (SELECT mu.exch_direction, mh.symbol, mh.decimals, "
                         f"'uniswap' as site, mu.highest_bid, mu.lowest_ask, lower(mu.tokenid) token_id, mu.volume "
                         f"FROM exchange_pairs LEFT JOIN module_hotbit mh ON mh.id = hotbit_id "
                         f"LEFT JOIN module_uniswap mu ON mu.id = uniswap_direction_id "
                         f"WHERE hotbit_id is not null and uniswap_direction_id is not null and mu.volume >= 1 "
                         f"ORDER BY hotbit_id) SELECT * FROM idex "
                         f"UNION ALL SELECT * FROM kyber "
                         f"UNION ALL SELECT * FROM uniswap;")
    get_eth_btc()
    currency = Settings.objects.all().values()[0]['currency']
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop = asyncio.get_event_loop()
    loop.set_default_executor(concurrent.futures.ThreadPoolExecutor(max_workers=20))
    init_result = loop.run_until_complete(init(all_symbols, percent, currency))
    compare_result = []
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
            if 'HOTBIT' in result[0][1]:
                buyurl = 'https://www.hotbit.io/exchange?symbol=' + result[0][0].replace('/', '_')
            if result[0][1] == 'IDEX':
                buyurl = 'https://exchange.idex.io/trading/' + result[0][0] + '-ETH'
            # if result[0][1] == 'BANKOR':
            #     buyurl = 'https://app.bancor.network/eth/swap?from=0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE&to=' + \
            #              result[0][8]
            if result[0][1] == 'KYBER':
                buyurl = 'https://kyberswap.com/swap/eth-' + result[0][0]
            if result[0][1] == 'UNISWAP':
                buyurl = 'https://app.uniswap.org/#/swap?outputCurrency=' + str(result[0][8])
            # if result[0][1] == 'UNISWAP_ONE':
            #     buyurl = 'https://app.uniswap.org/#/swap?outputCurrency=' + str(result[0][8]) + '&use=v1'

            if 'HOTBIT' in result[0][4]:
                sellurl = 'https://www.hotbit.io/exchange?symbol=' + result[0][3].replace('/', '_')
            if result[0][4] == 'IDEX':
                sellurl = 'https://exchange.idex.io/trading/' + result[0][3] + '-ETH'
            # if result[0][4] == 'BANKOR':
            #     sellurl = 'https://app.bancor.network/eth/swap?from=' + result[0][
            #         8] + '&to=0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE'
            if result[0][4] == 'KYBER':
                sellurl = 'https://kyberswap.com/swap/eth-' + result[0][3]
            if result[0][4] == 'UNISWAP':
                sellurl = 'https://app.uniswap.org/#/swap?outputCurrency=' + str(result[0][8])
            # if result[0][4] == 'UNISWAP_ONE':
            #     sellurl = 'https://app.uniswap.org/#/swap?outputCurrency=' + str(result[0][8]) + '&use=v1'
            compare_result.append({'pair': pair, 'buy_name': buy_name, 'buy': buy, 'sell_name': sell_name, 'sell': sell,
                                   'percent': percent, 'tokenid': tokenid, 'buyurl': buyurl, 'sellurl': sellurl})
    loop.close()
    return compare_result
    # except:
    #     print('False')
    #     return {'error': 'False'}


# Set Prices
def set_prices(token, symbol, buy, sell, volume):
    prices.append({token: [symbol, buy, sell, volume]})


def get_eth_btc():
    try:
        response = requests.get(f'https://api.hotbit.io/api/v1/market.status?market=ETH/BTC&period=10')
        Settings.objects.filter(id=1).update(currency=float(json.loads(response.content)['result']['last']))
    except:
        pass


def get_ticker():
    currency = get_eth_btc()
    ask_btc = currency
    bit_btc = currency
    token = ''
    resp_get = True
    while resp_get:
        try:
            response = requests.get(url=API_URL)
            resp_get = False
        except:
            resp_get = True
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



