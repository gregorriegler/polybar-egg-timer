Egg-Timer for the Polybar
=========================
[![build](https://github.com/gregorriegler/polybar-egg-timer/actions/workflows/python-app.yml/badge.svg)](https://github.com/gregorriegler/polybar-egg-timer/actions/workflows/python-app.yml)

## Features

![Egg Timer In Action](egg-timer.png)
- Sound Notification
- On-Screen Display Notification
- Pause and Resume
- Loop
- Change Time
- Reset

## Install

### Prerequisites
- Python 3
- `pip install playsound` for sound notification
- `pip install plyer` for textual notification

### Clone/Download this Repo
```
cd ~/.config/polybar/scripts
git clone https://github.com/gregorriegler/polybar-egg-timer
```

### Example Configuration
```
[module/egg-timer]
type = custom/script

exec = /path-to-egg-timer/egg_timer.py
tail = true

format = <label>
label = %output%

click-left = /path-to-egg-timer/egg_timer_control.py toggle_play
click-right = /path-to-egg-timer/egg_timer_control.py toggle_loop
click-middle = /path-to-egg-timer/egg_timer_control.py reset
scroll-up = /path-to-egg-timer/egg_timer_control.py longer
scroll-down = /path-to-egg-timer/egg_timer_control.py shorter
```

## What you should know
The Egg-Timer is built of two scripts.

- `egg_timer.py`, which runs the timer and is displayed in your bar. it listens for commands on a socket.
- `egg_timer_control.py`, which you can use to send commands to the timer.

## egg_timer.py

### Arguments
```
> ./egg_timer.py -h                             
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
### Example
Initialize with 5 minutes, and play a custom sound on finish:
```
> ./egg_timer.py -d 300 -s /path/to/your/sound.wav
```

## egg_timer_control.py 

### Arguments
```
> ./egg_timer_control.py -h    
usage: egg_timer_control.py [-h] [-host HOST] [-p PORT]
                            {toggle_play,reset,toggle_loop,longer,shorter,quit}

positional arguments:
  {toggle_play,reset,toggle_loop,longer,shorter,quit}

optional arguments:
  -h, --help            show this help message and exit
  -host HOST            Host where the control sends commands to. Default: '127.0.0.1'
  -p PORT, --port PORT  Port on which the control sends commands (int). Default: 65441
```
### Example
Start the timer:
```
> ./egg_timer_control.py toggle_play
```

## Troubleshooting
### Polybar shows this warning in the log file: 
```
warn: Dropping unmatched character ︎ (U+fe0e) in '10:00 ⏸︎'
```
This is not related to the Egg-Timer but Polybar itself. It has to do with ['variation selectors'](https://en.wikipedia.org/wiki/Variation_Selectors_(Unicode_block)).
As long as the Egg-Timer displays correctly in your bar, it's not a big deal. 
See this Polybar [GitHub issue](https://github.com/polybar/polybar/issues/2186) for more Information.

