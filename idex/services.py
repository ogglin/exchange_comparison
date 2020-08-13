import socket
import threading
import json
import time
from idex_module.client import Client

# import asyncio
# import pathlib
# import ssl
# import websockets
#
# # ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
# # localhost_pem = pathlib.Path(__file__).with_name("localhost.crl")
# # ssl_context.load_verify_locations(localhost_pem)
# context = ssl.SSLContext()
#
# async def hello():
#     # uri = "wss://datastream.idex.market"
#     uri = "wss://echo.websocket.org"
#     headers = ''
#     handshake = {
#         "request": "handshake",
#         "payload": "{\"version\": \"1.0.0\", \"key\": \"api:rbXUPt_TeOMzWRBpd8O_d\"}"
#     }
#     async with websockets.connect(
#             uri, ssl=context, extra_headers=headers
#     ) as websocket:
#
#         await websocket.send(str(handshake).encode("utf-8"))
#         print(f"{handshake}")
#
#         greeting = await websocket.recv()
#         print(f"{greeting}")
#         print(json.loads(greeting))
#
# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
# asyncio.get_event_loop().run_until_complete(hello())


def get_wss():
    api_key = 'api:rbXUPt_TeOMzWRBpd8O_d'
    address = 'wss://datastream.idex.market'
    private_key = '0xa76c9e24006f602065820fd16bfe3d0e4644aa385dec8a07b0c45f90d5d9e624'
    client = Client(api_key, address, private_key)

    # get currencies
    currencies = client.get_currencies()


    # # rT = threading.Thread(target=receving, args=("ResvThread", s))
    # host = socket.gethostbyname(socket.gethostname())
    # port = 0
    # # API_KEY = 'api:rbXUPt_TeOMzWRBpd8O_d'
    # rid = 'pair_request'
    # cid = ''
    # request = ''
    # status = ''
    # server = ('wss://datastream.idex.market', 443)
    # client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # client.bind((host, port))
    # client.setblocking(False)
    # # client.connect((host, port))
    # handshake = {
    #     "request": "handshake",
    #     "payload": "{\"version\": \"1.0.0\", \"key\": \"api:rbXUPt_TeOMzWRBpd8O_d\"}"
    # }
    # time.sleep(1)
    # client.sendto(str(handshake).encode("utf-8"), server)
    # reciv = client.recv(5242880)
    # print(json.loads(reciv))
    # while True:
    #     data = client.recv(5242880)
    #     return data
