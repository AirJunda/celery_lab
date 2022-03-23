#import djcelery

#djcelery.setup_loader()

from datetime import timedelta
from celery.schedules import crontab

BROKER_URL = 'redis://192.168.1.42:6379'
CELERY_RESULT_BACKEND = 'redis://192.168.1.42:6379/2'

CELERY_TIMEZONE = 'Asia/Shanghai'



CELERY_IMPORTS = (
    'course.tasks',
)

BROKER_BACKEND = 'redis'

CELERY_QUEUES = {
    'work_queue': {
        'exchange': 'work_queue',
        'exchange_type': 'direct',
        'binding_key': 'work_queue'
    },
    'beat_tasks': {
        'exchange': 'beat_tasks',
        'exchange_type': 'direct',
        'binding_key': 'beat_tasks'
    }
}

CELERY_DEFAULT_QUEUE = 'work_queue'

# prevent dead lock
CELERYD_FORCE_EXECV = True
# worker conucrent num
CELERYD_CONCURRENCY  = 4
# allow re try
CELERY_ACKS_LATE = True
# prevent memory leak, each worker can execute at most 100 jobs
CELERYD_MAX_TASKS_PER_CHILD = 100
# time out limit for each task
CELERY_TASK_TIME_LIMIT = 12 * 30




CELERYBEAT_SCHEDULE = {
    'task1': {
        'task': 'course.tasks.dj_cron_task',
        'schedule': timedelta(seconds=10),
        'options':{
            'queue': 'beat_tasks'
        }
    },
}


