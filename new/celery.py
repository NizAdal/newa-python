import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'new.settings')

app = Celery('new')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# Celery Beat Settings
app.conf.beat_schedule ={
    'send-mail-every-day-at-8': {
        'task': 'nizam.task.send_mail_func',
        # 'schedule': crontab(hour=10, minute=54),
        'schedule': crontab(hour=10, minute=54, day_of_month=19, month_of_year=6), # to perform the task only once 
        #'args':(2,)
    }
}