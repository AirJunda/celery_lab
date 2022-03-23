from celery import Celery

app = Celery('django-demo')
app.config_from_object('course.celeryconfig')