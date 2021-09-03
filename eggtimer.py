#!/usr/bin/env python3
import time
import asyncio
from timer import Timer
from commands import commands

# top level class
# seconds multiplier but nonbreaking
# stdout redirect
# e2e test
# need main with asyncio.run ??
# renames
# pause vs current in timer
# no more globals, all classes

class EggTimerApp:

    def __init__(self, speed=1):
        self._speed = speed

    def main(self):
        asyncio.run(self.egg_timer())

    async def egg_timer(self):
        await asyncio.gather(self.run_timer(), self.handle_commands())

    async def handle_commands(self):
        async for command in commands():
            print(command)
            mapping = {
                'start': self.start,
                'pause': self.pause
            }
            mapping.get(command)()

    def start(self):
        global timer
        timer.start(self._timestamp())

    def pause(self):
        global timer
        timer.pause(self._timestamp())

    def _timestamp(self):
        return time.time() * self._speed

    async def run_timer(self):
        global timer
        timer = Timer(60, lambda: print("ok"))
        while True:
            print(timer.time(self._timestamp()))
            await asyncio.sleep(1/self._speed)


if __name__ == "__main__":
    EggTimerApp(1000).main()
