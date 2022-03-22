from celery import Celery
import time
from datetime import datetime

# config
broker = 'redis://192.168.1.42:6379'
backend = 'redis://0.0.0.0:6379/2'
app = Celery('tasks', broker=broker)

@app.task
def add(x, y):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("ready to execute {} at time {}".format("add()", str(current_time)))

    time.sleep(3)
    return x + y

if __name__ == '__main__':
    print("main lanuched")
    ans = add.delay(3,76)
    print("result is {}".format(ans))
    print("main end")
