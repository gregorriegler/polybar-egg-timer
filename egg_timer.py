#!/usr/bin/env python3
import time
import asyncio
import sys
from timer import Timer
from commands import commands

# renames
# pause vs current in timer
# no more globals, all classes
# handle_commands misses one layer of abstraction (send command in)

class EggTimerApp:

    _quit = False
    _last_output = None

    def __init__(self, duration=60, speed=1, stdout=sys.stdout):
        self._speed = speed
        self._original_stdout = sys.stdout
        self._timer = Timer(duration, lambda: print("ok"))
        sys.stdout = stdout

    def main(self):
        asyncio.run(self.egg_timer())

    async def egg_timer(self):
        await asyncio.gather(self.run_timer(), self.handle_commands())

    async def run_timer(self):
        while not self._quit:
            output = self._timer.time(self._timestamp())
            self.print_once(output)
            await asyncio.sleep(1/(self._speed*2))

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
        self._timer.start(self._timestamp())

    def pause(self):
        self._timer.pause(self._timestamp())

    def quit(self):
        sys.stdout = self._original_stdout
        self._quit = True

    def _timestamp(self):
        return time.time() * self._speed

    def print_once(self, output):
        if(output != self._last_output):
            print(output)
            self._last_output = output


if __name__ == "__main__":
    EggTimerApp(60, 1).main()
