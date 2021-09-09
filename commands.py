import socket
import asyncio

HOST = '127.0.0.1'
PORT = 65441


async def commands(host=HOST, port=PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((host, port))
        server.listen()
        server.setblocking(False)
        while True:
            try:
                connection, _ = server.accept()
                with connection:
                    while True:
                        if not connection:
                            break
                        data = connection.recv(1024)
                        if not data:
                            break
                        command = data.decode('utf-8')
                        yield command
            except Exception as e:
                await asyncio.sleep(.1)
                pass
