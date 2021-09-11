Egg-Timer for the Polybar
=========================
[![example workflow](https://github.com/gregorriegler/polybar-egg-timer/actions/workflows/python-app.yml/badge.svg)](https://github.com/gregorriegler/polybar-egg-timer/actions/workflows/python-app.yml)

## Example Configuration
```
[module/egg-timer]
type = custom/script

exec = /path-to-eggtimer/egg_timer.py
tail = true

format = <label>
label = %output%

click-left = /path-to-eggtimer/egg_timer_control.py toggle_play
click-right = /path-to-eggtimer/egg_timer_control.py toggle_loop
click-middle = /path-to-eggtimer/egg_timer_control.py reset
scroll-up = /path-to-eggtimer/egg_timer_control.py longer
scroll-down = /path-to-eggtimer/egg_timer_control.py shorter
```

## egg_timer.py Arguments
```
$ ./egg_timer.py -h                             
usage: egg_timer.py [-h] [-d DURATION] [-x SPEED] [-s SOUNDFILE] [-f FORMAT] [-host HOST] [-p PORT]

optional arguments:
  -h, --help            show this help message and exit
  -d DURATION, --duration DURATION
                        Set the duration of the timer in seconds (int). Default: 60
  -x SPEED, --speed SPEED
                        Factor for the speed of the timer (int). Default: 1
  -s SOUNDFILE, --soundfile SOUNDFILE
                        Path to the file of the sound that plays when the timer finishes. Default:
                        'notification.wav'
  -f FORMAT, --format FORMAT
                        Change the format of the timer. Default: '{loop} {time} {play/pause}'
  -host HOST            Host on which the egg-timer listens for commands. Default: '127.0.0.1'
  -p PORT, --port PORT  Port on which the egg-timer listens for commands (int). Default: 65441
```

## egg_timer_control.py Arguments
```
$ ./egg_timer_control.py -h    
usage: egg_timer_control.py [-h] [-host HOST] [-p PORT]
                            {toggle_play,reset,toggle_loop,longer,shorter,quit}

positional arguments:
  {toggle_play,reset,toggle_loop,longer,shorter,quit}

optional arguments:
  -h, --help            show this help message and exit
  -host HOST            Host where the control sends commands to. Default: '127.0.0.1'
  -p PORT, --port PORT  Port on which the control sends commands (int). Default: 65441
```
