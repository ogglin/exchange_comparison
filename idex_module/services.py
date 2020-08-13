import socket
import threading
import json
import time
from idex.client import Client

import asyncio
import pathlib
import ssl
import websockets

# ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
# localhost_pem = pathlib.Path(__file__).with_name("localhost.crl")
# ssl_context.load_verify_locations(localhost_pem)
context = ssl.SSLContext()
API_KEY = 'api:rbXUPt_TeOMzWRBpd8O_d'


async def hello(api):
    uri = "wss://datastream.idex.market"
    headers = ''
    handshake = '{"request": "handshake","payload": "{\\"version\\": \\"1.0.0\\", \\"key\\": \\"' + api + '\\"}" }'
    async with websockets.connect(
            uri, ssl=context, extra_headers=headers
    ) as websocket:
        await websocket.send(handshake)
        print(handshake)

        greeting = await websocket.recv()
        print(f"received: {greeting}")
        sid = json.loads(greeting)['sid']
        reqs = '{"sid": "' + sid + '","request": "subscribeToMarkets",' \
                                   '"payload": "{\\"topics\\": [\\"ETH_AURA\\", \\"ETH_IDXM\\"], ' \
                                   '\\"events\\": [\\"market_orders\\", \\"market_cancels\\", \\"market_trades\\"] }"}'
        time.sleep(0.2)
        await websocket.send(reqs)
        print(reqs)
        while True:
            return await websocket.recv()
            # print(f"received: {greeting}")


def get_wss():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    data = asyncio.get_event_loop().run_until_complete(hello(API_KEY))
    print(data)
    return data

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
