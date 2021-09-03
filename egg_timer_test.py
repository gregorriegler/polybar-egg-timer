import pytest
import io
import threading
import time
from eggtimer import EggTimerApp

def test_app():
    output = io.StringIO()
    app = EggTimerApp(1000, output)
    app_thread = threading.Thread(target=app.main)
    app_thread.start()

    time.sleep(.1)
    app.quit()
    assert output.getvalue().startswith('01:00\n')
