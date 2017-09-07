# -*- coding: utf-8 -*-
from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from celery.decorators import task
from celery import schedules
import datetime

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exile.settings')
app = Celery('exile')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@task(name="notification")
def notification(tarea):
    # make the notification here
    file = open("./notification.txt")  
    file.write(str(datetime.date())) 
    file.close()
# end def

class crontabdate(schedules.crontab):

    def __init__(self, *args, **kwargs):
        super(crontabdate, self).__init__(*args, **kwargs)
        print "start"
        self.start_date = kwargs.get('start_date', None)

    def is_due(self, last_run_at):
    	print "is_due"
        if self.start_date is not None and self.now() < self.start_date:
            return (False, 20)  # try again in 20 seconds
        return super(crontabdate, self).is_due(last_run_at)

    def __reduce__(self):
        return self.__class__, (self.run_every, self.relative, self.nowfun, self.start_date)