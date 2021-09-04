#!/usr/bin/env python3
import time
import asyncio
import sys
from timer import Timer
from commands import commands

# dont print commands
# notification sound
# loop feature

class EggTimerApp:

    _quit = False
    _last_output = None

    def __init__(self, duration, speed):
        self._speed = speed
        self._timer = Timer(duration, lambda: print("ok"))

    def main(self):
        asyncio.run(self.egg_timer())

    async def egg_timer(self):
        await asyncio.gather(self.run_timer(), self.receive_commands())

    async def run_timer(self):
        while not self._quit:
            output = self._timer.time(self._timestamp())
            self.print_once(output)
            await asyncio.sleep(1/(self._speed*2))

    async def receive_commands(self):
        async for command in commands():
            self.handle_command(command)
            if(self._quit):
                break

    def handle_command(self, command):
        mapping = {
            'start': self.start,
            'pause': self.pause,
            'quit': self.quit
        }
        mapping.get(command)()

    def start(self):
        self._timer.start(self._timestamp())

    def pause(self):
        self._timer.pause(self._timestamp())

    def quit(self):
        self._quit = True

    def _timestamp(self):
        return time.time() * self._speed

    def print_once(self, output):
        if(output != self._last_output):
            print(output)
            self._last_output = output


if __name__ == "__main__":
    duration = 60
    if(len(sys.argv) > 1):
        duration = int(sys.argv[1])

    speed = 1
    if(len(sys.argv) > 2):
        speed = int(sys.argv[2])

    EggTimerApp(duration, speed).main()
