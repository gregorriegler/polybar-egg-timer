import io
import threading
import time
import os
from egg_timer import EggTimerApp

def test_app_run_through_timer():
    egg_timer_output = os.popen('./egg_timer.py 3 100')

    time.sleep(.1)
    os.system('./send_command.py')
    time.sleep(.3)
    os.system('./send_command.py quit')

    exp = '00:03\nstart\n00:02\n00:01\n00:00\nok\n00:03\nquit\n'
    assert egg_timer_output.read() == exp

def test_app_just_quit():
    egg_timer_output = os.popen('./egg_timer.py 3 100')

    time.sleep(.1)
    os.system('./send_command.py quit')

    exp = '00:03\nquit\n'
    assert egg_timer_output.read() == exp

def test_app_pause():
    egg_timer_output = os.popen('./egg_timer.py 3 100')

    time.sleep(.01)
    os.system('./send_command.py start')
    time.sleep(.01)
    os.system('./send_command.py pause')
    time.sleep(.01)
    os.system('./send_command.py quit')

    assert 'pause' in egg_timer_output.read()

