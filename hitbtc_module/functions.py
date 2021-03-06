import asyncio
import concurrent.futures
import datetime
import json
import time

import aiohttp
import requests
from aiohttp_socks import SocksConnector
from asgiref.sync import sync_to_async

from exchange_pairs.models import Settings
import exchange_pairs.services as ex_serv
from exchange_pairs.utils import CompareToken as ct, GetTokens as gt
from hitbtc_module.models import Hitbtc
from hotbit_module.functions import proxys

hitbtc_tikers_set = []


@sync_to_async
def currencies_update():
    # print('start idex currency update: ' + str(datetime.datetime.now()))
    update_list = []
    objs = Hitbtc.objects.all().order_by('id')
    if len(objs) > 0:
        for data in hitbtc_tikers_set:
            try:
                obj = objs.get(exch_direction=data['token'])
                obj.lowest_ask = data['ask']
                obj.highest_bid = data['bid']
                obj.volume = data['volume']
                update_list.append(obj)
            except:
                pair = Hitbtc(exch_direction=data['token'], buy=data['ask'], sell=data['bid'], is_active=True,
                              volume=data['volume'], symbol=data['symbol'])
                pair.save()
    else:
        for data in hitbtc_tikers_set:
            pair = Hitbtc(exch_direction=data['token'], buy=data['ask'], sell=data['bid'], is_active=True,
                          volume=data['volume'], symbol=data['symbol'])
            pair.save()
    Hitbtc.objects.bulk_update(update_list, ['buy', 'sell', 'volume'])
    # print('end idex currency update: ' + str(datetime.datetime.now()))


async def get_tiker():
    global hitbtc_tikers_set
    url = 'https://api.hitbtc.com/api/2/public/ticker'
    statuscode = 0
    while statuscode != 200:
        response = 0
        try:
            response = requests.get(url=url)
            hitbtc_tikers_set = []
        except (
                requests.ConnectionError,
                requests.exceptions.ReadTimeout,
                requests.exceptions.Timeout,
                requests.exceptions.ConnectTimeout,
        ) as e:
            time.sleep(1)
            statuscode = 0
            print(e)
        if response:
            statuscode = response.status_code
    jData = json.loads(response.content)
    for jd in jData:
        if 'ETH' in jd['symbol'] or 'BTC' in jd['symbol']:
            exch_direction = jd['symbol'].replace('ETH', '').replace('BTC', '')
            buy = jd['ask']
            sell = jd['bid']
            symbol = jd['symbol']
            volume = jd['volume']
            hitbtc_tikers_set.append(
                {'token': exch_direction, 'ask': buy, 'bid': sell, 'volume': volume, 'symbol': symbol})
    await currencies_update()
    print('tiker update', datetime.datetime.now())


async def hitbtc_tiker_init():
    while True:
        await get_tiker()


async def get_hitbtc_depth(symbol, proxy):
    url = f"https://api.hitbtc.com/api/2/public/orderbook/{symbol}"
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


async def compare_markets(token, percent, currency, proxy, exch):
    # tsymbol, contract, site, token, sell, buy, volume
    hitbtc_deth = await get_hitbtc_depth(token[3], proxy)
    asks = []
    bids = []
    if hitbtc_deth:
        if 'ask' in exch:
            for ask in hitbtc_deth['ask']:
                asks.append([ask['price'], ask['size']])
            return ct(buy_from='hitbtc', buy_symbol=token[2], buy_prices=asks, buy_volume=0, sell_to=token[2],
                      sell_prices=token[4],
                      sell_volume=1, sell_symbol=token[0],
                      contract=token[1], profit_percent=percent, currency=currency).compare()
        else:
            for ask in hitbtc_deth['bid']:
                bids.append([ask['price'], ask['size']])
            return ct(buy_from='hitbtc', buy_symbol=token[2], buy_prices=token[4], buy_volume=0, sell_to=token[2],
                      sell_prices=bids,
                      sell_volume=1, sell_symbol=token[0],
                      contract=token[1], profit_percent=percent, currency=currency).compare()


async def init_compare(hitbtc_tokens, all_tokens, percent, currency):
    async_tasks = []
    # print('start collect symbols ' + str(len(symbols)) + ' :' + str(datetime.datetime.now()))
    cnt = 0
    for htoken in hitbtc_tokens:
        for token in all_tokens:
            if htoken[0] == token[0]:
                async_tasks.append(compare_markets(token, percent, currency, proxys[cnt], 'ask'))
                async_tasks.append(compare_markets(token, percent, currency, proxys[cnt], 'bid'))
                cnt += 1
                if cnt >= len(proxys):
                    cnt = 0
    # print('end  collect symbols: ' + str(len(async_tasks)) + str(datetime.datetime.now()))
    results = await asyncio.gather(*async_tasks)
    return results


# @sync_to_async
def hitbtc_profits():
    # global all_compared_tokens
    print('hitbtc_profits start', datetime.datetime.now())
    setting = Settings.objects.all()[0]
    percent = setting.market_percent / 100 * setting.market_koef
    # tsymbol, contract, site, token, sell, buy, volume
    isTD = True
    hitbtc_tokens = []
    all_tokens = []
    while isTD:
        if len(ex_serv.all_compared_tokens) > 0:
            for token in ex_serv.all_compared_tokens:
                if 'hitbtc' in token[2]:
                    hitbtc_tokens.append(token)
                else:
                    all_tokens.append(token)
            isTD = False
        else:
            isTD = True
            time.sleep(1)
            print('wait for tokens')
    currency = Settings.objects.all().values()[0]['currency']
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop = asyncio.get_event_loop()
    loop.set_default_executor(concurrent.futures.ThreadPoolExecutor(max_workers=20))
    init_result = loop.run_until_complete(init_compare(hitbtc_tokens, all_tokens, percent, currency))
    print('hitbtc_profits end', datetime.datetime.now())
    compare_result = []
    for result in init_result:
        if result:
            '''
            'buy_from',
            'buy_symbol':,
            'buy_price': ,
            'buy_volume':,
            'buy_ask':,
            'sell_to':,
            'sell_symbol':,
            'sell_price':,
            'sell_volume':,
            'sell_bid':,
            'percent':,
            'contract':,
            '''

            buy_name = result['buy_from']
            pair = result['buy_symbol'].replace('ETH', '').replace('BTC', '')
            buy = result['buy_price']
            buy_ask = result['buy_ask']
            sell_name = result['sell_to']
            sell_symbol = result['sell_symbol']
            sell = result['sell_price']
            sell_bid = result['sell_bid']
            percent = result['percent']
            contract = result['contract']
            tokenid = '0x0000000000000000000000000000000000000000000000000000000000000000'
            if 'hitbtc' in buy_name:
                if 'ETH' in result['buy_symbol']:
                    buyurl = 'https://hitbtc.com/' + pair + '-to-eth'
                if 'BTC' in result['buy_symbol']:
                    buyurl = 'https://hitbtc.com/' + pair + '-to-btc'
            if 'hotbit' in buy_name:
                buyurl = 'https://www.hotbit.io/exchange?symbol=' + sell_symbol.replace('/', '_')
            if buy_name == 'idex':
                buyurl = 'https://exchange.idex.io/trading/' + pair + '-ETH'
            # if result[0][1] == 'BANKOR':
            #     buyurl = 'https://app.bancor.network/eth/swap?from=0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE&to=' + \
            #              result[0][8]
            if buy_name == 'kyber':
                buyurl = 'https://kyberswap.com/swap/eth-' + pair
            if buy_name == 'uniswap':
                buyurl = 'https://app.uniswap.org/#/swap?outputCurrency=' + str(contract)
            # if result[0][1] == 'UNISWAP_ONE':
            #     buyurl = 'https://app.uniswap.org/#/swap?outputCurrency=' + str(result[0][8]) + '&use=v1'

            if 'hitbtc' in sell_name:
                if 'ETH' in result['buy_symbol']:
                    sellurl = 'https://hitbtc.com/' + pair + '-to-eth'
                if 'BTC' in result['buy_symbol']:
                    sellurl = 'https://hitbtc.com/' + pair + '-to-btc'
            if 'hotbit' in sell_name:
                sellurl = 'https://www.hotbit.io/exchange?symbol=' + sell_symbol.replace('/', '_')
            if sell_name == 'idex':
                sellurl = 'https://exchange.idex.io/trading/' + pair + '-ETH'
            # if result[0][4] == 'BANKOR':
            #     sellurl = 'https://app.bancor.network/eth/swap?from=' + result[0][
            #         8] + '&to=0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE'
            if sell_name == 'kyber':
                sellurl = 'https://kyberswap.com/swap/eth-' + pair
            if sell_name == 'uniswap':
                sellurl = 'https://app.uniswap.org/#/swap?outputCurrency=' + str(contract)
            # if result[0][4] == 'UNISWAP_ONE':
            #     sellurl = 'https://app.uniswap.org/#/swap?outputCurrency=' + str(result[0][8]) + '&use=v1'
            compare_result.append(
                {'pair': result['buy_symbol'], 'buy_name': buy_name, 'buy': buy, 'buy_ask': buy_ask,
                 'sell_name': sell_name, 'sell': sell, 'sell_bid': sell_bid,
                 'percent': percent, 'tokenid': tokenid, 'buyurl': buyurl, 'sellurl': sellurl})
    loop.close()
    return compare_result

# async def hitbtc_profits_init():
#     while True:
#         await hitbtc_profits()
#
#
# if __name__ == '__main__':
#     hitbtc_profits()
