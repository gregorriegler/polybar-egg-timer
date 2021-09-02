#!/usr/bin/env python3
import time
import asyncio
from timer import Timer
from commands import commands


async def main():
    await asyncio.gather(run_timer(),handle_commands())


async def handle_commands():
    async for command in commands():
        print(command)
        mapping = {
            'start': start,
            'pause': pause
        }
        mapping.get(command)()


def start():
    global timer
    timer.start(time.time())

def pause():
    global timer
    timer.pause(time.time())

async def run_timer():
    global timer
    timer = Timer(60, lambda: print("ok"))
    while True:
        print(timer.time(time.time()))
        await asyncio.sleep(1)


asyncio.run(main())
