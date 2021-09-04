import io
import threading
import time
import os
from egg_timer import EggTimerApp

def test_app():
    stream = os.popen('./egg_timer.py 3 100')

    time.sleep(.1)
    os.system('./send_command.py')
    time.sleep(.3)
    os.system('./send_command.py quit')

    new_output = stream.read()
    exp = '00:03\nstart\n00:02\n00:01\n00:00\nok\n00:03\nquit\n'
    assert new_output == exp

