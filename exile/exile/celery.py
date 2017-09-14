# -*- coding: utf-8 -*-
from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from celery.decorators import task
from celery import schedules
import datetime
import os

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exile.settings')
app = Celery('exile')

# Using a string here means the worker will not have to
# pickle the objects when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@task(name="notification")
def notification(tarea):
    from operacion.models import Tarea, Notificacion, SubTarea, SubNotificacion
    tarea = Tarea.objects.filter(pk=tarea).first()
    if tarea:
        notificacion = Notificacion.objects.create(
            tarea=tarea
        )
        subtareas = SubTarea.objects.filter(tarea=tarea)
        for subtarea in subtareas:
            SubNotificacion.objects.create(
                notificacion = notification,
                subtarea = subtarea,
                nombre = subtarea.nombre,
                descripcion = subtarea.descripcion
            )
        # end if
    # end if

    # make the notification here
    
    file = open(os.path.join(BASE_DIR, "notix.txt"), "w+") 
    file.write(str(datetime.datetime.now())) 
    file.close()
# end def

@task(name="ejecutar")
def ejecutar(tarea):
    from djcelery.models import PeriodicTask
    from operacion.models import Tarea
    tarea = Tarea.objects.filter(pk=tarea).first()
    if tarea:
        if tarea.interval or tarea.crontab:
            tsk, created = PeriodicTask.objects.get_or_create(
                interval = tarea.interval,
                crontab = tarea.crontab,
                name = 'Tarea #%d' % (tarea.pk, ),
                task = 'notification',
                args = [tarea.pk],
                expires = tarea.fecha_finalizacion or tarea.fecha_ejecucion
            )
        else:
            notification.dalay(tarea.pk)
        # end if
    # end if
# end def

