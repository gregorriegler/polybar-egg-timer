import io
import threading
import time
from egg_timer import EggTimerApp

def test_app():
    output = io.StringIO()
    app = EggTimerApp(3, 50, output)
    app_thread = threading.Thread(target=app.main)
    app_thread.start()

    time.sleep(.1)
    app.start()
    time.sleep(.1)
    app.quit()

    exp = '00:03\n00:02\n00:01\n00:00\nok\n00:03\n'
    assert output.getvalue() == exp 

