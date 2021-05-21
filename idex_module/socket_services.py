import asyncio
import json
import logging
import ssl
import time
from datetime import datetime
import requests

import websockets
from asgiref.sync import sync_to_async
from django.db.models import Q
from websockets import WebSocketClientProtocol
import psycopg2

from exchange_comparison.utils import _query
from exchange_pairs.models import WebsocketLog
import exchange_pairs.services as exps
from idex_module.models import IdexSocketLog

DATABASE_NAME = 'exchange_comparison'
DATABASE_USER = 'exchange_comparison'
DATABASE_PASSWORD = '0L7OBgdmXgvV28'
DATABASE_HOST = '95.183.12.206'
DATABASE_PORT = '5432'


logging.basicConfig(level=logging.INFO)

# ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
# localhost_pem = pathlib.Path(__file__).with_name("localhost.crl")
# ssl_context.load_verify_locations(localhost_pem)
context = ssl.SSLContext()
API_KEY = 'api:rbXUPt_TeOMzWRBpd8O_d'
WSS_URL = 'wss://websocket.idex.io/v1'
MarketURL = 'https://api.idex.io/v1/markets'


@sync_to_async
def log_message(message: str) -> None:
    logging.info(f"Message: {message}")


def get_tokens():
    response = requests.get(url=MarketURL)
    m_data = json.loads(response.content)
    tokens = []
    for data in m_data:
        tokens.append(data['market'])
    return tokens


def compare_price(data, compare, id):
    tm = datetime.fromtimestamp(data['t'] / 1000)
    token = data['m'].replace('-ETH', '')
    price = float(data['p'])
    if data['s'] == 'buy':
        stype = "buy"
        sprice = compare[4]
        buyurl = 'https://exchange.idex.io/trading/' + token + '-ETH'
        sellurl = 'https://app.uniswap.org/#/swap?outputCurrency=' + str(compare[1])
        percent = (sprice - price) / (price / 100)
        _query(f"""UPDATE websocket_log SET (datetime, buy_url, sell_url, percent, token, type, site, price,
                sprice) = ('{tm}', '{buyurl}', '{sellurl}', {percent}, '{token}',
                '{stype}', '{compare[0]}', {price}, {sprice}) WHERE id = {id};""")
    if data['s'] == 'sell':
        stype = "sell"
        sprice = compare[5]
        buyurl = 'https://app.uniswap.org/#/swap?outputCurrency=' + str(compare[1])
        sellurl = 'https://exchange.idex.io/trading/' + token + '-ETH'
        percent = (sprice - price) / (price / 100)
        _query(f"""UPDATE websocket_log SET (datetime, buy_url, sell_url, percent, token, type, site, price,
                        sprice) = ('{tm}', '{buyurl}', '{sellurl}', {percent}, '{token}',
                        '{stype}', '{compare[0]}', {price}, {sprice}) WHERE id = {id};""")


@sync_to_async
def save_log(message):
    slog = IdexSocketLog(log=str(message))
    slog.save()


async def check_connect(websocket):
    while True:
        print('try ping')
        pong_waiter = await websocket.ping()
        await pong_waiter
        if pong_waiter.result():
            print('Pong')
        time.sleep(3)


async def consumer_handler(websocket: WebSocketClientProtocol) -> None:
    print('Subscribed')
    # await check_connect(websocket)
    async for message in websocket:
        print(json.loads(message))
        data = json.loads(message)['data']
        log_message(data)
        try:
            await save_log(message)
        except:
            pass


async def subscribe(host, message) -> None:
    async with websockets.connect(host) as websocket:
        await websocket.send(message)
        subs = await websocket.recv()
        print('Subs: ', subs)
        await consumer_handler(websocket)


@sync_to_async
def get_wss():
    tokens = get_tokens()
    message = {
        'method': 'subscribe',
        'markets': tokens,
        'subscriptions': ['trades', ]
    }
    print(message)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(subscribe(WSS_URL, json.dumps(message)))
    loop.close()


@sync_to_async
def resave_wss():
    wT = True
    while wT:
        if len(exps.uniswap_prices_set) > 0:
            sLogs = WebsocketLog.objects.order_by('-id').filter(Q(token__isnull=True) & ~Q(log__icontains='error'))
            for sLog in sLogs:
                if 'trades' in sLog.log:
                    trade = json.loads(sLog.log)['data']
                else:
                    trade = json.loads(sLog.log)
                id = sLog.id
                for uni_p in exps.uniswap_prices_set:
                    if uni_p[0].lower() == trade['m'].replace('-ETH', '').lower():
                        compare_price(trade, uni_p, id)
            wT = False
        else:
            time.sleep(2)


async def init_resave():
    while True:
        await resave_wss()
        time.sleep(60)


if __name__ == '__main__':
    get_wss()
