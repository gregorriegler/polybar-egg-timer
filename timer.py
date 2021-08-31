from datetime import timedelta


class Timer:

    def __init__(self, value=60, notify=None):
        self._value = value
        self._notify = notify
        self._running = False

    def start(self, timestamp):
        self._start = timestamp
        self._running = True

    def pause(self, timestamp):
        self._running = False
        self._value = self._seconds_left(timestamp)

    def time(self, timestamp):
        if(not self._running):
            return mmss(self._value)

        if(self._seconds_left(timestamp) == 0):
            self._notify_once()

        return mmss(self._seconds_left(timestamp))

    def _notify_once(self):
        if(self._notify):
            self._notify()
            self._notify = None

    def _seconds_left(self, timestamp):
        return max(self._value - (timestamp - self._start), 0)


def mmss(seconds):
    td = timedelta(seconds=seconds)
    return str(td)[2:7]
