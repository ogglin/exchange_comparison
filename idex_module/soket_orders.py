import asyncio
import json
import logging
import ssl
import websockets
from websockets import WebSocketClientProtocol
from asgiref.sync import sync_to_async

from exchange_pairs.utils import GetTokens

logging.basicConfig(level=logging.INFO)

context = ssl.SSLContext()
API_KEY = 'api:rbXUPt_TeOMzWRBpd8O_d'
WSS_URL = 'wss://websocket.idex.io/v1'
idex_orderbooks = []


def orders_idex():
    global idex_orderbooks
    idex_tokens = GetTokens(module='idex', _all=False).tokens()
    markets = []
    for token in idex_tokens:
        idex_orderbooks.append(
            {'market': token[3] + '-ETH',
             'asks': [],
             'bids': []}
        )
        markets.append(token[3] + '-ETH')
    sub_message = {
        'method': 'subscribe',
        'markets': markets,
        'subscriptions': ['l2orderbook', ]
    }
    return sub_message


async def consumer_handler(websocket: WebSocketClientProtocol) -> None:
    print('Subscribed')
    async for message in websocket:
        print(json.loads(message))


async def subscribe(host, message) -> None:
    async with websockets.connect(host) as websocket:
        await websocket.send(message)
        subs = await websocket.recv()
        print('Subscribe to: ', subs)
        await consumer_handler(websocket)


@sync_to_async
def init_orderbook_idex_wss():
    message = orders_idex()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(subscribe(WSS_URL, json.dumps(message)))
    loop.close()
