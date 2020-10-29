import asyncio
import json
import logging
import ssl
import time
import requests

import websockets
from websockets import WebSocketClientProtocol
from exchange_pairs.models import WebsocketLog

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
        log_message(json.loads(message))
        try:
            log = WebsocketLog(datetime=time.ctime(), log=json.loads(message))
            log.save()
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

# get_wss()
