from datetime import timedelta


class Timer:

    def __init__(self, value=60, notify=None):
        self._value = value
        self._notify = notify
        self._stopped_at = value
        self._running = False
        self._loop = False

    def toggle_play(self, timestamp):
        if(self._running):
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
        if(new_value > 1 and new_stopped_at > 1):
            self._value = new_value
            self._stopped_at = new_stopped_at

    def time(self, timestamp):
        if(not self._running):
            return self._loop_symbol() + mmss(self._stopped_at) + ' ⏸︎'

        seconds_left = self._seconds_left(timestamp)
        if(seconds_left == 0):
            self._reset(timestamp)
            self._notify_over()

        return self._loop_symbol() + mmss(seconds_left)

    def _seconds_left(self, timestamp):
        return max(self._stopped_at - (timestamp - self._start), 0)

    def _reset(self, timestamp):
        if(self._loop):
            self._start = timestamp
            self._running = True
        else:
            self._running = False
        self._stopped_at = self._value

    def _notify_over(self):
        if(self._notify):
            self._notify()

    def _loop_symbol(self):
        if(self._loop):
            return '🔄 '
        else:
            return ''


def mmss(seconds):
    td = timedelta(seconds=seconds)
    return str(td)[2:7]
