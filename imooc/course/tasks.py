from celery import Task
import time
from datetime import datetime
from course import app

@app.task
def djtask():
    # this works
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("ready to execute {} at time {}".format("django task()", str(current_time)))

    time.sleep(3)
    endtime = now.strftime("%H:%M:%S")
    return "task done at:" + str(endtime)

@app.task
def dj_cron_task():
    # this works
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("ready to execute {} at time {}".format("django cron task()", str(current_time)))


    endtime = now.strftime("%H:%M:%S")
    return "cron task end time is: " + str(endtime)


class CourseTask(Task):
    name = 'course-task'
    # mooc课用这种继承改写run的方法去demo,我本地试验失败。提示‘Received unregistered task of type 'course-task’

    def run(self, *args, **kwargs):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("ready to execute {} at time {}".format("add()", str(current_time)))

        time.sleep(3)
        endtime = now.strftime("%H:%M:%S")
        return "task done at:" + str(endtime )


