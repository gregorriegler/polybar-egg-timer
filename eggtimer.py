#!/usr/bin/env python3

from timer import Timer
import time
import socket
import asyncio

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432




async def main():
    await asyncio.gather(handle_commands(),run_timer())


async def handle_commands():
    async for command in receive_commands():
        print(command)


async def run_timer():
    timer = Timer(60, lambda st: print(st))
    timer.start(time.time())
    while True:
        print(timer.time(time.time()))
        await asyncio.sleep(1)


async def receive_commands():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST,PORT))
        server.listen()
        server.setblocking(False)
        while True:
            try:
                conn, addr = server.accept()
                with conn:
                    while True:
                        if not conn:
                            break
                        data = conn.recv(1024)
                        if not data:
                            break
                        command = data.decode('utf-8')
                        yield command
            except Exception as e:
                await asyncio.sleep(.1)
                pass


asyncio.run(main())
