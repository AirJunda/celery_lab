import time
from datetime import datetime
from celery_app import app

@app.task
def multiply(x, y):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("ready to execute {} at time {}".format("multiply()", str(current_time)))

    time.sleep(5)
    return x * y