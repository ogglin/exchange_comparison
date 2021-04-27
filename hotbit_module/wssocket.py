import asyncio
import gzip
import json
import logging
import ssl
import time
import websockets
from asgiref.sync import sync_to_async

context = ssl.SSLContext()
logging.basicConfig(level=logging.INFO)

WSS_URL = 'wss://ws.hotbit.io'


@sync_to_async
def log_message(message: str) -> None:
    logging.info(f"Message: {message}")


async def check_connect(websocket):
    while True:
        print('try ping')
        pong_waiter = await websocket.ping()
        await pong_waiter
        if pong_waiter.result():
            print('Pong')
        time.sleep(3)


async def consumer_handler(websocket: websockets.WebSocketClientProtocol) -> None:
    print('Subscribed')
    # await check_connect(websocket)
    async for message in websocket:
        gzip_fd = gzip.GzipFile(fileobj=message)
        # destinations = pd.read_csv(gzip_fd)
        print(gzip_fd)
        # print(json.loads(message))
        data = json.loads(message)['data']
        log_message(data)


async def subscribe(host, message) -> None:
    async with websockets.connect(host) as websocket:
        await websocket.send(message)
        subs = await websocket.recv()
        print('Subs: ', subs)
        await consumer_handler(websocket)


@sync_to_async
def hotbit_wss():
    message = {
        'method': 'depths.subscribe',
        'params': [["ETCUSDT", 100, "0.00000001"], ["EOSUSDT", 100, "0.00000001"], ["BTCUSDT", 100, "0.00000001"], ],
        'id': 100
    }
    print(message)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(subscribe(WSS_URL, json.dumps(message)))
    loop.close()
