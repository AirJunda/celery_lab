from datetime import timedelta
from celery.schedules import crontab


BROKER_URL = 'redis://192.168.1.42:6379'
CELERY_RESULT_BACKEND = 'redis://192.168.1.42:6379/2'

CELERY_TIMEZONE = 'Asia/Shanghai'

CELERY_IMPORTS = (
    'celery_app.task1',
    'celery_app.task2',
)

CELERYBEAT_SCHEDULE = {
    'task1': {
        'task': 'celery_app.task1.add',
        'schedule': timedelta(seconds=10),
        'args': (2,8)
    },
}
