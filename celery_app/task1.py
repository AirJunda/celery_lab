
import time
from datetime import datetime
from celery_app import app

@app.task
def add(x, y):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("ready to execute {} at time {}".format("add()", str(current_time)))

    time.sleep(3)
    return x + y