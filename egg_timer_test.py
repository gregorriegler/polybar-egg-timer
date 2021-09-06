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

    expected = '00:03 ⏸︎\n00:02\n00:01\n00:00\n00:03 ⏸︎\n'
    assert egg_timer_output.read() == expected


def test_app_just_quit():
    egg_timer_output = os.popen('./egg_timer.py 3 100')

    time.sleep(.1)
    os.system('./send_command.py quit')

    assert egg_timer_output.read() == '00:03 ⏸︎\n'


def test_app_pause():
    egg_timer_output = os.popen('./egg_timer.py 3 100')

    time.sleep(.1)
    os.system('./send_command.py toggle_play')
    time.sleep(.025)
    os.system('./send_command.py toggle_play')
    time.sleep(.1)
    os.system('./send_command.py quit')
    time.sleep(.1)

    output = egg_timer_output.read()
    assert output.count('⏸︎') >= 2


def test_loop():
    egg_timer_output = os.popen('./egg_timer.py 3 100')

    time.sleep(.1)
    os.system('./send_command.py toggle_loop')
    time.sleep(.1)
    os.system('./send_command.py quit')

    expected = '00:03 ⏸︎\n🔄 00:03 ⏸︎\n'
    assert egg_timer_output.read() == expected


def test_loop_and_play():
    egg_timer_output = os.popen('./egg_timer.py 3 100')

    time.sleep(.1)
    os.system('./send_command.py toggle_loop')
    time.sleep(.1)
    os.system('./send_command.py toggle_play')
    time.sleep(.1)
    os.system('./send_command.py quit')

    expected = '00:03 ⏸︎\n🔄 00:03 ⏸︎\n🔄 00:02\n🔄 00:01\n'
    assert expected in egg_timer_output.read()
