#!/usr/bin/env python3

import argparse
import asyncio
import os
import sys
import time

from playsound import playsound
from plyer import notification

from commands import commands
from timer import Timer


class EggTimerApp:

    _quit = False
    _last_output = None

    def __init__(self, args):
        self._speed = args.speed
        self._sound_file = self._path_to_sound(args.soundfile)
        self._timer = Timer(args.duration, self.notify, args.format)
        self._host = args.host
        self._port = args.port

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
        async for command in commands(self._host, self._port):
            self.handle_command(command)
            if self._quit:
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
        if output != self._last_output:
            print(output, flush=True)
            self._last_output = output

    def notify(self):
        try:
            self._play_sound()
            notification.notify(title='Time over')
        except:
            print('There was a Problem notifying', sys.exc_info()[0], file=sys.stderr)

    def _play_sound(self):
        playsound(self._sound_file, False)

    def _path_to_sound(self, path):
        if path.startswith('/'):
            return path

        return os.path.dirname(os.path.realpath(__file__)) + '/' + path


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--duration", type=int, default=60, help="Set the duration of the timer in seconds (int). Default: 60")
    parser.add_argument("-x", "--speed", type=int, default=1, help="Factor for the speed of the timer (int). Default: 1")
    parser.add_argument("-s", "--soundfile", default="notification.wav", help="Path to the file of the sound that plays when the timer finishes. Default: 'notification.wav'")
    parser.add_argument("-f", "--format", default="{time} {loop}{play/pause}", help="Change the format of the timer. Default: '{time} {loop}{play/pause}'")
    parser.add_argument("-host", default='127.0.0.1', help="Host on which the egg-timer listens for commands. Default: '127.0.0.1'")
    parser.add_argument("-p", "--port", type=int, default=65441, help="Port on which the egg-timer listens for commands (int). Default: 65441")
    args = parser.parse_args()

    EggTimerApp(args).main()
