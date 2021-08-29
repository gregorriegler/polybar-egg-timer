from datetime import timedelta


class Timer:

    def __init__(self, value=60, notify=None):
        self.value = value
        self.notify = notify
        self.running = False

    def start(self, when):
        self.start = when
        self.running = True
        pass

    def pause(self, when):
        self.running = False
        self.value = self.__left(when)

    def left(self, when):
        if(not self.running):
            return self.__pretty(self.value)

        result = self.__left(when)
        if(result == 0):
            notify()

        return self.__pretty(result)

    def __left(self, when):
        return max(self.value - when, 0)

    def __pretty(self, seconds):
        td = timedelta(seconds=seconds)
        return str(td)[2:]


# Tests


def test_starts_paused():
    timer = Timer(60)
    assert timer.left(0) == '01:00'
    assert timer.left(1) == '01:00'


def test_starts_counting_down():
    timer = Timer(60)
    timer.start(0)
    assert timer.left(1) == '00:59'
    assert timer.left(2) == '00:58'
    assert timer.left(60) == '00:00'
    assert timer.left(61) == '00:00'  # does not overcount


def test_notifies_when_over():
    timer = Timer(60, notify)
    timer.start(0)
    assert timer.left(60) == '00:00'
    assert notified == 'notified'


def test_pauses():
    timer = Timer(60)
    timer.start(0)
    timer.pause(30)
    assert timer.left(60) == '00:30'


notified = ''


def notify():
    global notified
    notified = 'notified'
