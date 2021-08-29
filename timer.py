from datetime import timedelta


class Timer:

    def __init__(self, value=60, notify=None):
        self._value = value
        self._notify = notify
        self._running = False

    def start(self, when):
        self._start = when
        self._running = True

    def pause(self, when):
        self._running = False
        self._value = self._seconds_left(when)

    def time(self, when):
        if(not self._running):
            return mmss(self._value)

        result = self._seconds_left(when)
        if(result == 0 and self._notify):
            self._notify()

        return mmss(result)

    def _seconds_left(self, when):
        return max(self._value - (when - self._start), 0)


def mmss(seconds):
    td = timedelta(seconds=seconds)
    return str(td)[2:]
