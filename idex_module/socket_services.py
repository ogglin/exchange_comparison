import asyncio
import json
import logging
import ssl
import time

import websockets
from websockets import WebSocketClientProtocol

logging.basicConfig(level=logging.INFO)

# ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
# localhost_pem = pathlib.Path(__file__).with_name("localhost.crl")
# ssl_context.load_verify_locations(localhost_pem)
context = ssl.SSLContext()
API_KEY = 'api:rbXUPt_TeOMzWRBpd8O_d'
WSS_URL = "wss://datastream.idex.market"


def log_message(message: str) -> None:
    logging.info(f"Message: {message}")


async def consumer_handler(websocket: WebSocketClientProtocol) -> None:
    print('Subscribed')
    async for message in websocket:
        log_message(json.loads(message))


async def consume(host) -> None:
    async with websockets.connect(host) as websocket:
        await consumer_handler(websocket)


async def subscribe(host, handshake, req, payload) -> None:
    async with websockets.connect(host) as websocket:
        print(handshake)
        await websocket.send(handshake)
        greeting = await websocket.recv()
        print(greeting)
        sid = json.loads(greeting)['sid']
        req = {
            "sid": sid,
            "request": req,
            "payload": payload
        }
        reqs = json.dumps(req)
        print(reqs)
        time.sleep(1)
        await websocket.send(reqs)
        subs = await websocket.recv()
        print('Subs: ', subs)
        await consumer_handler(websocket)


async def produce(message: str, host: str) -> None:
    async with websockets.connect(host) as websocket:
        await websocket.send(message)
        await websocket.recv()


async def hello(api):
    token = 'ETH_QNT'
    headers = ''
    handshake = {
        "request": "handshake",
        "payload": "{\"version\": \"1.0.0\", \"key\": \"" + api + "\"}"
    }
    sHandshake = json.dumps(handshake)
    # handshake = '{"request": "handshake","payload": "{\\"version\\": \\"1.0.0\\", \\"key\\": \\"' + api + '\\"}" }'
    async with websockets.connect(
            WSS_URL, ssl=context, extra_headers=headers
    ) as websocket:
        await websocket.send(sHandshake)
        print(sHandshake)

        greeting = await websocket.recv()
        print(f"received: {greeting}")
        sid = json.loads(greeting)['sid']
        reqs = '{"sid": "' + sid + '","request": "subscribeToMarkets",' \
                                   '"payload": "{\\"topics\\": [\\"' + token + '\\", \"ETH_IDXM\"], ' \
                                   '\\"events\\": [\\"market_trades\\"] }"}'
        time.sleep(0.2)
        await websocket.send(reqs)
        print(reqs)
        # while True:
        #     return await websocket.recv()
        # print(f"received: {greeting}")


def get_wss():
    token = 'ETH_QNT'
    handshake = json.dumps({
        "request": "handshake",
        "payload": "{\"version\": \"1.0.0\", \"key\": \"" + API_KEY + "\"}"
    })
    req = "subscribeToMarkets"
    payload = '{\"topics\": [\"' + token + '\", \"ETH_IDXM\"], \"events\": [\"market_trades\"] }'
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(subscribe(WSS_URL, handshake, req, payload))

    # return data


# get_wss()


# def get_wss():
#     # rT = threading.Thread(target=receving, args=("ResvThread", s))
#     host = socket.gethostbyname(socket.gethostname())
#     port = 0
#     #
#     rid = 'pair_request'
#     cid = ''
#     request = ''
#     status = ''
#     server = ('wss://datastream.idex.market', 443)
#     client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     client.bind((host, port))
#     client.setblocking(False)
#     # client.connect((host, port))
#     handshake = {
#         "request": "handshake",
#         "payload": "{\"version\": \"1.0.0\", \"key\": \"api:rbXUPt_TeOMzWRBpd8O_d\"}"
#     }
#     time.sleep(1)
#     client.sendto(str(handshake).encode("utf-8"), server)
#     reciv = client.recv(5242880)
#     print(json.loads(reciv))
#     while True:
#         data = client.recv(5242880)
#         return data
