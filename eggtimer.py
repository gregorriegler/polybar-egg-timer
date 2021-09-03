#!/usr/bin/env python3
import time
import asyncio
from timer import Timer
from commands import commands

# top level class
# seconds multiplier but nonbreaking
# stdout redirect
# e2e test
# renames
# pause vs current in timer
# no more globals, all classes

async def egg_timer():
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


def main():
    asyncio.run(egg_timer())


if __name__ == "__main__":
    main()
