#!/usr/bin/env python3
import time
import asyncio
import sys
from timer import Timer
from commands import commands

# need main with asyncio.run ??
# do not repeat same time on stdout for better e2e tests
# renames
# pause vs current in timer
# no more globals, all classes
# handle_commands misses one layer of abstraction (send command in)

class EggTimerApp:

    _quit = False
    _last_output = None

    def __init__(self, duration=60, speed=1, stdout=sys.stdout):
        self._duration = duration
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
        timer = Timer(self._duration, lambda: print("ok"))
        while not self._quit:
            output = timer.time(self._timestamp())
            if(output != self._last_output):
                print(output)
                self._last_output = output

            await asyncio.sleep(1/self._speed)


if __name__ == "__main__":
    EggTimerApp(3, 1000).main()
