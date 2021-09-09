from datetime import timedelta


class Timer:

    def __init__(self, value=60, notify=None, format="{loop} {time} {play/pause}"):
        self._value = value
        self._notify = notify
        self._format = format
        self._stopped_at = value
        self._start = None
        self._running = False
        self._loop = False

    def toggle_play(self, timestamp):
        if self._running:
            self._stopped_at = self._seconds_left(timestamp)
            self._running = False
        else:
            self._start = timestamp
            self._running = True

    def reset(self):
        self._running = False
        self._stopped_at = self._value

    def toggle_loop(self):
        self._loop = not self._loop

    def longer(self):
        self.change_time(10)

    def shorter(self):
        self.change_time(-10)

    def change_time(self, amount):
        new_value = self._value + amount
        new_stopped_at = self._stopped_at + amount
        if new_value > 1 and new_stopped_at > 1:
            self._value = new_value
            self._stopped_at = new_stopped_at

    def time(self, timestamp):
        return format_time(self._timer_status(timestamp), self._format)

    def _timer_status(self, timestamp):
        if not self._running:
            return TimerStatus(self._stopped_at, False, self._loop)
        seconds_left = self._seconds_left(timestamp)
        if seconds_left == 0:
            self._reset(timestamp)
            self._notify_over()

        return TimerStatus(seconds_left, True, self._loop)

    def _seconds_left(self, timestamp):
        return max(self._stopped_at - (timestamp - self._start), 0)

    def _reset(self, timestamp):
        if self._loop:
            self._start = timestamp
            self._running = True
        else:
            self._running = False
        self._stopped_at = self._value

    def _notify_over(self):
        if self._notify:
            self._notify()


def mmss(seconds):
    td = timedelta(seconds=seconds)
    return str(td)[2:7]


class TimerStatus:

    def __init__(self, seconds_left, playing, looping):
        self.seconds_left = seconds_left
        self.playing = playing
        self.looping = looping


def format_time(timer_status, format="{loop} {time} {play/pause}"):
    return format\
        .replace("{loop}", "🔄" if timer_status.looping else "")\
        .replace("{time}", _mmss(timer_status.seconds_left))\
        .replace("{play/pause}", "▶️" if timer_status.playing else "⏸︎")\
        .strip()


def _mmss(seconds):
    td = timedelta(seconds=seconds)
    return str(td)[2:7]
