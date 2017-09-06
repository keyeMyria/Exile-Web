from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
import datetime

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exile.settings')
app = Celery('exile')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

from celery.decorators import task
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from datetime import timedelta

@task(name="sum_two_numbers")
def add(x, y):
    return x + y
# end def

@task(name="periodic2")
def periodic2():
	file = open("./log.txt") 
	 
	file.write(str(datetime.date())) 
	 
	file.close()
# end def


@task(name="notification")
def notification():
	# make the notification here
	file = open("./notification.txt")  
	file.write(str(datetime.date())) 
	file.close()
# end def