
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
        self.value = max(self.value - when, 0)

    def left(self, when):
        if(not self.running):
            return self.value

        result = max(self.value - when, 0)
        if(result == 0):
            notify()

        return result


# Tests


def test_starts_paused():
    timer = Timer(60)
    assert timer.left(0) == 60
    assert timer.left(1) == 60


def test_starts_counting_down():
    timer = Timer(60)
    timer.start(0)
    assert timer.left(1) == 59
    assert timer.left(2) == 58
    assert timer.left(60) == 0
    assert timer.left(61) == 0  # does not overcount


def test_notifies_when_over():
    timer = Timer(60, notify)
    timer.start(0)
    assert timer.left(60) == 0
    assert notified == 'notified'


def test_pauses():
    timer = Timer(60)
    timer.start(0)
    timer.left(30)
    timer.pause(30)

    assert timer.left(60) == 30


notified = ''


def notify():
    global notified
    notified = 'notified'
