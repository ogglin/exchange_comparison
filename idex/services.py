import socket
import threading
import json


def get_wss():
    # rT = threading.Thread(target=receving, args=("ResvThread", s))
    host = socket.gethostbyname(socket.gethostname())
    port = 0
    # API_KEY = 'api:rbXUPt_TeOMzWRBpd8O_d'
    rid = 'pair_request'
    cid = ''
    request = ''
    status = ''
    server = ('wss://datastream.idex.market', 443)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client.bind((host, port))
    # client.setblocking(False)
    client.connect(('wss://datastream.idex.market', 443))
    handshake = {
        "request": "handshake",
        "payload": "{\"version\": \"1.0.0\", \"key\": \"api:rbXUPt_TeOMzWRBpd8O_d\"}"
    }
    # client.sendto(str(handshake).encode("utf-8"), server)
    client.send(str(handshake).encode("utf-8"))
    reciv = client.recv(5242880)
    print(json.loads(reciv))
    while True:
        data = client.recv(5242880)
        return data
