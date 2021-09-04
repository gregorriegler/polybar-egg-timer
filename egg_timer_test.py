import pytest
import io
import threading
import time
from eggtimer import EggTimerApp

def test_app():
    output = io.StringIO()
    app = EggTimerApp(3, 1000, output)
    app_thread = threading.Thread(target=app.main)
    app_thread.start()

    app.start()
    time.sleep(.1)
    app.quit()

    assert output.getvalue().startswith('00:03\n')
    assert '00:02\n00:01\n' in output.getvalue()
