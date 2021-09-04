from datetime import timedelta


class Timer:

    def __init__(self, value=60, notify=None):
        self._value = value
        self._notify = notify
        self._stopped_at = value
        self._running = False

    def start(self, timestamp):
        self._start = timestamp
        self._running = True

    def pause(self, timestamp):
        self._stopped_at = self._seconds_left(timestamp)
        self._running = False

    def time(self, timestamp):
        if(not self._running):
            return mmss(self._stopped_at)

        seconds_left = self._seconds_left(timestamp)
        if(seconds_left == 0):
            self._reset()
            self._notify_over()

        return mmss(seconds_left)

    def _seconds_left(self, timestamp):
        return max(self._stopped_at - (timestamp - self._start), 0)

    def _reset(self):
        self._running = False
        self._stopped_at = self._value

    def _notify_over(self):
        if(self._notify):
            self._notify()


def mmss(seconds):
    td = timedelta(seconds=seconds)
    return str(td)[2:7]
