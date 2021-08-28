class Timer:
    value = 60            
    notify = None

    def __init__(self, notify=None):
        self.notify = notify


    def start(self, when):
        value = when
        pass

    def left(self, when):    
        result = self.value - when
        if(result <= 0):
            notify()
        return result

# Code

def test_starts_at_60_by_default():
    timer = Timer()
    assert timer.left(0) == 60

def test_counts_down():
    timer = Timer()
    timer.start(0)
    assert timer.left(1) == 59
    assert timer.left(2) == 58

notified = ''
def notify():
    global notified
    notified = 'notified'

def test_notifies_when_over():
    timer = Timer(notify)
    timer.start(0)
    assert timer.left(60) == 0
    assert notified == 'notified'

