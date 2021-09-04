import pytest
from timer import Timer


notified = ''


def notify():
    global notified
    notified += 'notified'


@pytest.fixture(autouse=True)
def run_around_tests():
    global notified
    notified = ''
    yield


def test_starts_paused():
    timer = Timer(60)
    assert timer.time(0) == '01:00⏸︎'
    assert timer.time(1) == '01:00⏸︎'


def test_starts_counting_down():
    timer = Timer(60)
    timer.start(0)
    assert timer.time(1) == '00:59'
    assert timer.time(2) == '00:58'
    assert timer.time(2.2) == '00:57'
    assert timer.time(60) == '00:00'


def test_starts_at_non_zero():
    timer = Timer(60)
    timer.start(100)
    assert timer.time(101) == '00:59'
    assert timer.time(102) == '00:58'
    assert timer.time(160) == '00:00'


def test_notifies_once_when_over():
    timer = Timer(60, notify)
    timer.start(0)
    assert timer.time(60) == '00:00'
    assert notified == 'notified'


def test_resets_when_over():
    timer = Timer(60)
    timer.start(0)
    assert timer.time(60) == '00:00'
    assert timer.time(61) == '01:00⏸︎'
    assert timer.time(62) == '01:00⏸︎' # stopped


def test_notifies_after_reset():
    timer = Timer(60, notify)
    timer.start(0)
    timer.time(60) == '00:00'
    timer.start(100)
    assert timer.time(160) == '00:00'
    assert notified == 'notifiednotified'


def test_pauses():
    timer = Timer(60)
    timer.start(0)
    timer.pause(30)
    assert timer.time(60) == '00:30⏸︎'


def test_resumes_after_pause():
    timer = Timer(60)
    timer.start(0)
    timer.pause(30)
    timer.start(50)
    assert timer.time(60) == '00:20'
    assert timer.time(70) == '00:10'
    assert timer.time(80) == '00:00'
