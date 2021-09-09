import os
import time


def test_app_run_through_timer():
    egg_timer_output = os.popen('./egg_timer.py -d 3 -x 100')

    time.sleep(.1)
    os.system('./egg_timer_control.py toggle_play')
    time.sleep(.8)
    os.system('./egg_timer_control.py quit')

    expected = '00:03 ⏸︎\n00:02 ▶️\n00:01 ▶️\n00:00 ▶️\n00:03 ⏸︎\n'
    assert egg_timer_output.read() == expected


def test_app_just_quit():
    egg_timer_output = os.popen('./egg_timer.py -d 3 -x 100')

    time.sleep(.1)
    os.system('./egg_timer_control.py quit')

    assert egg_timer_output.read() == '00:03 ⏸︎\n'


def test_change_time_longer():
    egg_timer_output = os.popen('./egg_timer.py -d 10 -x 100')

    time.sleep(.1)
    os.system('./egg_timer_control.py longer')
    time.sleep(.1)
    os.system('./egg_timer_control.py quit')

    assert egg_timer_output.read() == '00:10 ⏸︎\n00:20 ⏸︎\n'


def test_change_time_shorter():
    egg_timer_output = os.popen('./egg_timer.py -d 20 -x 100')

    time.sleep(.1)
    os.system('./egg_timer_control.py shorter')
    time.sleep(.1)
    os.system('./egg_timer_control.py quit')

    assert egg_timer_output.read() == '00:20 ⏸︎\n00:10 ⏸︎\n'


def test_app_pause():
    egg_timer_output = os.popen('./egg_timer.py -d 3 -x 100')

    time.sleep(.1)
    os.system('./egg_timer_control.py toggle_play')
    time.sleep(.025)
    os.system('./egg_timer_control.py toggle_play')
    time.sleep(.1)
    os.system('./egg_timer_control.py quit')
    time.sleep(.1)

    output = egg_timer_output.read()
    assert output.count('⏸︎') >= 2


def test_reset():
    egg_timer_output = os.popen('./egg_timer.py -d 600 -x 100')

    time.sleep(.1)
    os.system('./egg_timer_control.py toggle_play')
    time.sleep(.1)
    os.system('./egg_timer_control.py reset')
    time.sleep(.1)
    os.system('./egg_timer_control.py quit')

    assert egg_timer_output.read().endswith('10:00 ⏸︎\n')


def test_loop():
    egg_timer_output = os.popen('./egg_timer.py -d 3 -x 100')

    time.sleep(.1)
    os.system('./egg_timer_control.py toggle_loop')
    time.sleep(.1)
    os.system('./egg_timer_control.py quit')

    expected = '00:03 ⏸︎\n🔄 00:03 ⏸︎\n'
    assert egg_timer_output.read() == expected


def test_loop_and_play():
    egg_timer_output = os.popen('./egg_timer.py -d 3 -x 100')

    time.sleep(.1)
    os.system('./egg_timer_control.py toggle_loop')
    time.sleep(.1)
    os.system('./egg_timer_control.py toggle_play')
    time.sleep(.1)
    os.system('./egg_timer_control.py quit')

    expected = '00:03 ⏸︎\n🔄 00:03 ⏸︎\n🔄 00:02 ▶️\n🔄 00:01 ▶️\n'
    assert expected in egg_timer_output.read()


def test_different_format():
    egg_timer_output = os.popen('./egg_timer.py -d 3 -f "ok {time}"')
    time.sleep(.1)
    os.system('./egg_timer_control.py quit')

    expected = 'ok 00:03\n'
    assert expected in egg_timer_output.read()
