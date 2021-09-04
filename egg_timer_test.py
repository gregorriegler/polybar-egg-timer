import io
import threading
import time
import os
from egg_timer import EggTimerApp

def test_app():
    output = io.StringIO()
    app = EggTimerApp(3, 50, output)
    app_thread = threading.Thread(target=app.main)
    app_thread.start()

    time.sleep(.1)
    os.system('./send_command.py')
    time.sleep(.3)
    os.system('./send_command.py quit')

    exp = '00:03\nstart\n00:02\n00:01\n00:00\nok\n00:03\nquit\n'
    assert output.getvalue() == exp 

