from datetime import timedelta


class Timer:

    def __init__(self, value=60, notify=None):
        self._value = value
        self._current = value
        self._notify = notify
        self._running = False

    def start(self, timestamp):
        self._start = timestamp
        self._running = True

    def pause(self, timestamp):
        self._running = False
        self._current = self._seconds_left(timestamp)

    def time(self, timestamp):
        if(not self._running):
            return mmss(self._current)

        if(self._seconds_left(timestamp) == 0):
            self._reset()
            self._notify_over()

        return mmss(self._seconds_left(timestamp))

    def _seconds_left(self, timestamp):
        return max(self._current - (timestamp - self._start), 0)

    def _reset(self):
        self._running = False
        self._current = self._value

    def _notify_over(self):
        if(self._notify):
            self._notify()


def mmss(seconds):
    td = timedelta(seconds=seconds)
    return str(td)[2:7]
