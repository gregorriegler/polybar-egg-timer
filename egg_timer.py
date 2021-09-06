#!/usr/bin/env python3

import time
import asyncio
import sys
import os
from playsound import playsound
from plyer import notification
from timer import Timer
from commands import commands

# when counting down show play button
# doc requirements: pip install playsound and plyer
# customizable format
# sound not playing fully
# sound configurable
# warn: Dropping unmatched character ︎ (U+fe0e) in '01:00⏸︎' ??
# better ideas for when address already in use? port as argv

# [module/egg-timer]
# type = custom/script

# exec = eggtimer-python/egg_timer.py
# tail = true

# format = <label>
# label = %output%

# click-left = eggtimer-python/send_command.py
# click-right = eggtimer-python/send_command.py toggle_loop
# scroll-up = eggtimer-python/send_command.py longer
# scroll-down = eggtimer-python/send_command.py shorter

class EggTimerApp:

    _quit = False
    _last_output = None

    def __init__(self, duration, speed):
        self._speed = speed
        self._timer = Timer(duration, self.notify)

    def main(self):
        asyncio.run(self.egg_timer())

    async def egg_timer(self):
        await asyncio.gather(self.run_timer(), self.receive_commands())

    async def run_timer(self):
        while not self._quit:
            output = self._timer.time(self._timestamp())
            self.print_once(output)
            await asyncio.sleep(1/(self._speed*10))

    async def receive_commands(self):
        async for command in commands():
            self.handle_command(command)
            if(self._quit):
                break

    def handle_command(self, command):
        mapping = {
            'toggle_play': self.toggle_play,
            'toggle_loop': self.toggle_loop,
            'longer': self.longer,
            'shorter': self.shorter,
            'quit': self.quit
        }
        mapping.get(command)()

    def toggle_play(self):
        self._timer.toggle_play(self._timestamp())

    def toggle_loop(self):
        self._timer.toggle_loop()

    def longer(self):
        self._timer.longer()

    def shorter(self):
        self._timer.shorter()

    def quit(self):
        self._quit = True

    def _timestamp(self):
        return time.time() * self._speed

    def print_once(self, output):
        if(output != self._last_output):
            print(output, flush=True)
            self._last_output = output

    def notify(self):
        self._play_sound()
        notification.notify(title='Time over')

    def _play_sound(self):
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
