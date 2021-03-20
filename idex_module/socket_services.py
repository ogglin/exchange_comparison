import asyncio
import json
import logging
import ssl
from datetime import datetime
import requests

import websockets
from asgiref.sync import sync_to_async
from websockets import WebSocketClientProtocol
# from exchange_pairs.models import WebsocketLog
import psycopg2

from idex_module.models import IdexSocketLog

DATABASE_NAME = 'exchange_comparison'
DATABASE_USER = 'exchange_comparison'
DATABASE_PASSWORD = '0L7OBgdmXgvV28'
DATABASE_HOST = '95.183.12.206'
DATABASE_PORT = '5432'


def _query(q):
    con = psycopg2.connect(
        database=DATABASE_NAME,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD,
        host=DATABASE_HOST,
        port=DATABASE_PORT
    )
    cur = con.cursor()
    try:
        cur.execute(q)
        data = cur.fetchall()
    except psycopg2.DatabaseError as err:
        print("Error: ", err)
    else:
        return data
    finally:
        con.commit()


logging.basicConfig(level=logging.INFO)

# ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
# localhost_pem = pathlib.Path(__file__).with_name("localhost.crl")
# ssl_context.load_verify_locations(localhost_pem)
context = ssl.SSLContext()
API_KEY = 'api:rbXUPt_TeOMzWRBpd8O_d'
WSS_URL = 'wss://websocket.idex.io/v1'
MarketURL = 'https://api.idex.io/v1/markets'


def log_message(message: str) -> None:
    logging.info(f"Message: {message}")


def get_tokens():
    response = requests.get(url=MarketURL)
    m_data = json.loads(response.content)
    tokens = []
    for data in m_data:
        tokens.append(data['market'])
    return tokens


def save_log(data):
    if 'type' in data:
        data = data['data']
    token = _query(
        f"SELECT tsymbol FROM module_idex WHERE exch_direction = '{data['m'].replace('ETH', '').replace('-', '')}'")[0][
        0]
    contract = _query(f"SELECT contract FROM trusted_pairs WHERE tsymbol = '{token}';")[0][0]
    # compare_prices = _query(
    #     f"""with hotbit as (SELECT 'hotbit' as site, buy, sell FROM module_hotbit WHERE tsymbol = '{token}' and symbol not ilike '%BTC%'),
    #             hitbtc as (SELECT 'hitbtc' as site, buy, sell FROM module_hitbtc WHERE tsymbol = '{token}' and symbol not ilike '%BTC%'),
    #             kyber as (SELECT 'kyber' as site, lowest_ask buy, highest_bid sell FROM module_kyber WHERE tsymbol = '{token}'),
    #             bancor as (SELECT 'bancor' as site, lowest_ask buy, highest_bid sell FROM module_bancor WHERE tsymbol = '{token}'),
    #             uniswap as (SELECT 'uniswap' as site, lowest_ask buy, highest_bid sell FROM module_uniswap WHERE tsymbol = '{token}'),
    #             uniswap_one as (SELECT 'uniswap_one' as site, lowest_ask buy, highest_bid sell FROM module_uniswap_one WHERE tsymbol = '{token}')
    #             SELECT * FROM hotbit UNION ALL SELECT * FROM hitbtc UNION ALL SELECT * FROM kyber UNION ALL SELECT * FROM bancor UNION ALL SELECT * FROM uniswap UNION ALL SELECT * FROM uniswap_one;""")
    compare_prices = _query(
        f"SELECT 'uniswap' as site, lowest_ask buy, highest_bid sell FROM module_uniswap WHERE tsymbol = '{token}';")
    price = float(data['p'])
    for compare in compare_prices:
        if data['s'] == 'buy':
            stype = "buy"
            sprice = compare[2]
            buyurl = 'https://exchange.idex.io/trading/' + token + '-ETH'
            sellurl = ''
            if 'uniswap' in compare[0]:
                sellurl = 'https://app.uniswap.org/#/swap?outputCurrency=' + str(contract)
            return stype, price, sprice, (sprice - price) / (price / 100), token, buyurl, sellurl, compare[0]
        if data['s'] == 'sell':
            stype = "sell"
            sprice = compare[1]
            buyurl = ''
            sellurl = 'https://exchange.idex.io/trading/' + token + '-ETH'
            if 'uniswap' in compare[0]:
                buyurl = 'https://app.uniswap.org/#/swap?outputCurrency=' + str(contract)
            return stype, price, sprice, (sprice - price) / (price / 100), token, buyurl, sellurl, compare[0]


async def consumer_handler(websocket: WebSocketClientProtocol) -> None:
    print('Subscribed')
    async for message in websocket:
        slog = IdexSocketLog(log=str(message))
        slog.save()
        data = json.loads(message)['data']
        print(json.loads(message))
        log_message(data)
        log = json.dumps(data)
        stype, price, sprice, percent, token, buyurl, sellurl, site = save_log(data)
        try:
            log = f"INSERT INTO websocket_log (datetime, log, buy_url, sell_url, percent, token, type, site, price, sprice) " \
                  f"VALUES ('{datetime.utcnow()}', '{log}', '{buyurl}', '{sellurl}', {percent}, '{token}', '{stype}', '{site}', {price}, {sprice});"
            _query(log)
        except:
            pass


async def subscribe(host, message) -> None:
    async with websockets.connect(host) as websocket:
        await websocket.send(message)
        subs = await websocket.recv()
        print('Subs: ', subs)
        await consumer_handler(websocket)


async def produce(message: str, host: str) -> None:
    async with websockets.connect(host) as websocket:
        await websocket.send(message)
        await websocket.recv()


@sync_to_async
def get_wss():
    tokens = get_tokens()
    message = {
        'method': 'subscribe',
        'markets': tokens,
        'subscriptions': ['trades', ]
    }
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(subscribe(WSS_URL, json.dumps(message)))


if __name__ == '__main__':
    get_wss()
