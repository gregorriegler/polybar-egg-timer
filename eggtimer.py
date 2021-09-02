#!/usr/bin/env python3

from timer import Timer
import time
import socket
import asyncio

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432




async def main():
    await asyncio.gather(run_timer(),handle_commands())


async def handle_commands():
    async for command in CommandStream().commands():
        print(command)


async def run_timer():
    timer = Timer(60, lambda st: print(st))
    timer.start(time.time())
    while True:
        print(timer.time(time.time()))
        await asyncio.sleep(1)

class CommandStream:

    def __init__(self, host='127.0.0.1', port=65441):
        self._host = host
        self._port = port

    async def commands(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind((self._host, self._port))
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


asyncio.run(main())
