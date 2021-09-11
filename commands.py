import asyncio
import socket


async def commands(host, port):
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
            except Exception:
                await asyncio.sleep(.1)
                pass
