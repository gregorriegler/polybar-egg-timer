Egg-Timer for the Polybar
=========================

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
> ./egg_timer.py -h                             
usage: egg_timer.py [-h] [-d DURATION] [-x SPEED] [-s SOUNDFILE] [-f FORMAT]

optional arguments:
  -h, --help            show this help message and exit
  -d DURATION, --duration DURATION
                        set the duration of the timer in seconds (int)
  -x SPEED, --speed SPEED
                        factor for the speed of the timer (int)
  -s SOUNDFILE, --soundfile SOUNDFILE
                        path to the file of the sound that plays when the timer finishes
  -f FORMAT, --format FORMAT
                        change the format of the timer. Default: {loop} {time} {play/pause}
```
