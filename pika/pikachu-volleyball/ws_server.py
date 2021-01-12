

import asyncio
import websockets
import pickle
import json
import socket
import threading
from threading import Thread
import _thread

HOST = '192.168.50.168'  # The socket server's hostname or IP address
PORT = 54088        # The port used by the server
Gateway_IP = '192.168.43.176'  # for websocket server

data = ''
connect = 0

async def hello(websocket, path):
    
    '''print('echo')
    async for message in websocket:
        print(message,'received from client')
        greeting = f"Hello {message}!"
        await websocket.send(greeting)
        print(f"> {greeting}")
    '''
    while True:
        if connect != 0:
            data = conn.recv(44).decode('utf-8')
            #print('Received from socket server : ', data,"\n")
            #line = await websocket.recv()
            #print('gg')
            #print(data)
            #if line is None:
             #   return
            await websocket.send(data)
        else:
            print('disconnect')

def handle_client(conn, loop, number):
    with conn:
        print('sdsdsd')
        connect = conn
        web_port = 8866 + number
        start_server = websockets.serve(hello, "127.0.0.1", web_port, ping_interval=None)

        asyncio.set_event_loop(loop)
        loop.run_until_complete(start_server)
        loop.run_forever()
        #asyncio.get_event_loop().run_until_complete(start_server)
        #asyncio.get_event_loop().run_forever()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
client_num = 0
try:
    while True:
        conn, addr = s.accept()
        if(conn):
            loop = asyncio.new_event_loop()
            p = threading.Thread(target=handle_client, args=(conn, loop, client_num))
            p.start()
            #_thread.start_new_thread(handle_client,(conn,client_num,))
            
            client_num += 1
except KeyboardInterrupt:
    s.close()
"""
print (conn)
with conn:
    print('sdsdsd')
    connect = conn
    start_server = websockets.serve(hello, "127.0.0.1", 8866, ping_interval=None)
    
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
"""

            




            


