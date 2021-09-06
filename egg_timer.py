#!/usr/bin/env python3

import time
import asyncio
import sys
import os
from playsound import playsound
from timer import Timer
from commands import commands

# sound not playing fully
# actual notification
# mouse wheel changes time
# sound configurable
# warn: Dropping unmatched character ︎ (U+fe0e) in '01:00⏸︎' ??
# better ideas for when address already in use? how to test and run at the same time

# [module/egg-timer]
# type = custom/script

# exec = /home/gregor/IdeaProjects/eggtimer-python/egg_timer.py
# tail = true

# format = <label>
# label = %output%

# click-left = /home/gregor/IdeaProjects/eggtimer-python/send_command.py

class EggTimerApp:

    _quit = False
    _last_output = None

    def __init__(self, duration, speed):
        self._speed = speed
        self._timer = Timer(duration, self.play_sound)

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
            'toggle_play': self.toggle_play,
            'toggle_loop': self.toggle_loop,
            'quit': self.quit
        }
        mapping.get(command)()

    def toggle_play(self):
        self._timer.toggle_play(self._timestamp())

    def toggle_loop(self):
        self._timer.toggle_loop()

    def quit(self):
        self._quit = True

    def _timestamp(self):
        return time.time() * self._speed

    def print_once(self, output):
        if(output != self._last_output):
            print(output, flush=True)
            self._last_output = output

    def play_sound(self):
        dir = os.path.dirname(os.path.realpath(__file__))
        playsound(dir + '/notification.wav', False)


if __name__ == "__main__":
    duration = 60
    if(len(sys.argv) > 1):
        duration = int(sys.argv[1])

    speed = 1
    if(len(sys.argv) > 2):
        speed = int(sys.argv[2])

    EggTimerApp(duration, speed).main()
