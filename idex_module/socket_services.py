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

DATABASE_NAME = 'exchange_comparison'
DATABASE_USER = 'exchange_comparison'
DATABASE_PASSWORD = '0L7OBgdmXgvV28'
DATABASE_HOST = '95.183.12.206'
DATABASE_PORT = '5432'


def _query(q):
    print(q)
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


async def consumer_handler(websocket: WebSocketClientProtocol) -> None:
    print('Subscribed')
    async for message in websocket:
        data = json.loads(message)['data']
        print(json.loads(message))
        log_message(data)
        try:
            log = f"INSERT INTO websocket_log (datetime, log) VALUES ('{datetime.utcnow()}', '{json.dumps(data)}');"
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
