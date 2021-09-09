#!/usr/bin/env python3

import time
import asyncio
import sys
import os
import argparse
from playsound import playsound
from plyer import notification
from timer import Timer
from commands import commands

# all tests test ui
# use a string assertion lib
# customizable format
# sound not playing fully
# warn: Dropping unmatched character ︎ (U+fe0e) in '01:00⏸︎' ??
# better ideas for when address already in use? port as argv
# doc requirements: pip install playsound and plyer

# [module/egg-timer]
# type = custom/script

# exec = eggtimer-python/egg_timer.py
# tail = true

# format = <label>
# label = %output%

# click-left = eggtimer-python/send_command.py
# click-right = eggtimer-python/send_command.py toggle_loop
# click-middle = eggtimer-python/send_command.py reset
# scroll-up = eggtimer-python/send_command.py longer
# scroll-down = eggtimer-python/send_command.py shorter

class EggTimerApp:

    _quit = False
    _last_output = None

    def __init__(self, args):
        self._speed = args.speed
        self._soundfile = self._path_to_sound(args.soundfile)
        self._timer = Timer(args.duration, self.notify, args.format)

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
        {
            'toggle_play': self.toggle_play,
            'reset': self.reset,
            'toggle_loop': self.toggle_loop,
            'longer': self.longer,
            'shorter': self.shorter,
            'quit': self.quit
        }.get(command)()

    def toggle_play(self):
        self._timer.toggle_play(self._timestamp())

    def reset(self):
        self._timer.reset()

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
        playsound(self._soundfile, False)

    def _path_to_sound(self, path):
        if(path.startswith('/')):
            return path

        dir = os.path.dirname(os.path.realpath(__file__))
        return dir + '/' + path


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--duration", type=int, default=60, help="set the duration of the timer in seconds (int)")
    parser.add_argument("-x", "--speed", type=int, default=1, help="factor for the speed of the timer (int)")
    parser.add_argument("-s", "--soundfile", default="notification.wav", help="path to the file of the sound that plays when the timer finishes")
    parser.add_argument("-f", "--format", default="{loop} {time} {play/pause}", help="change the format of the timer. Default: {loop} {time} {play/pause}")
    args = parser.parse_args()

    EggTimerApp(args).main()
