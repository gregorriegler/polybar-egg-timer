import pytest

from timer.timer import TimerStatus, format_time


@pytest.mark.parametrize(
    "playing, looping, format, expected",
    [
        (True, True, "", ""),
        (True, False, "random string", "random string"),
        (True, False, "{time}", "00:30"),
        (True, False, "random {time} string", "random 00:30 string"),
        (True, False, "{time} {play/pause}", "00:30 ▶"),
        (False, False, "{time} {play/pause}", "00:30 ⏸"),
        (True, True, "{loop} {time} {play/pause}", "🔄 00:30 ▶"),
        (True, False, "{loop} {time} {play/pause}", "00:30 ▶"),
    ]
)
def test_empty_format(playing, looping, format, expected):
    timer_status = TimerStatus(30, playing, looping)
    assert format_time(timer_status, format, {'play': '▶', 'pause': '⏸', 'loop': '🔄'}) == expected
