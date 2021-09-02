#!/usr/bin/env python3
from timer import Timer
from commands import commands
import time
import asyncio


async def main():
    await asyncio.gather(run_timer(),handle_commands())


async def handle_commands():
    async for command in commands():
        print(command)


async def run_timer():
    timer = Timer(60, lambda st: print(st))
    timer.start(time.time())
    while True:
        print(timer.time(time.time()))
        await asyncio.sleep(1)


asyncio.run(main())
