#!/usr/bin/env python3
import time
import asyncio
import sys
from timer import Timer
from commands import commands

# need main with asyncio.run ??
# renames
# pause vs current in timer
# no more globals, all classes
# handle_commands misses one layer of abstraction (send command in)

class EggTimerApp:

    _quit = False

    def __init__(self, speed=1, stdout=sys.stdout):
        self._speed = speed
        self._original_stdout = sys.stdout
        sys.stdout = stdout

    def main(self):
        asyncio.run(self.egg_timer())

    def quit(self):
        sys.stdout = self._original_stdout
        self._quit = True

    async def egg_timer(self):
        await asyncio.gather(self.run_timer(), self.handle_commands())

    async def handle_commands(self):
        mapping = {
            'start': self.start,
            'pause': self.pause,
            'quit': self.quit
        }
        async for command in commands():
            print(command)
            mapping.get(command)()
            if(self._quit):
                break

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
        while not self._quit:
            print(timer.time(self._timestamp()))
            await asyncio.sleep(1/self._speed)


if __name__ == "__main__":
    EggTimerApp(1000).main()
