# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from usuarios import models as usuarios
from django.contrib.auth.models import User
from cuser.fields import CurrentUserField
from subcripcion.models import Cuenta
from djcelery.models import CrontabSchedule, IntervalSchedule
from exile.celery import crontabdate
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class CrontabDateSchedule(CrontabSchedule):
    start_date = models.DateTimeField()
    def __init__(self, *args, **kwargs):
        super(CrontabDateSchedule, self).__init__(*args, **kwargs)
        print "CrontabDateSchedule"
        file = open(os.path.join(BASE_DIR, "text.txt"), "w+")  
        file.write("CrontabDateSchedule" + str(datetime.now())) 
        file.close()
    #end def

    @property
    def schedule(self):
        print "schedule"
        file = open(os.path.join(BASE_DIR, "text.txt"), "w+")  
        file.write("schedule" + str(datetime.now())) 
        file.close()
        return None
        return schedules.crontabdate(minute=self.minute,
                                 hour=self.hour,
                                 day_of_week=self.day_of_week,
                                 day_of_month=self.day_of_month,
                                 month_of_year=self.month_of_year, start_date=self.start_date)
# end def

class Tipo(models.Model):
    nombre = models.CharField(max_length=100)
    creator = CurrentUserField(add_only=True, related_name="created_tipo")
    last_editor = CurrentUserField(related_name="last_edited_tipo")
    cuenta = models.ForeignKey(Cuenta)
    eliminado = models.BooleanField(default=False)
    eliminado_por = models.ForeignKey(User, related_name="eliminado_por_tipo", blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end def
# end def


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.ForeignKey(Tipo, verbose_name="Tipo de identifiación")
    identificacion = models.CharField(max_length=100)
    direccion = models.CharField(
        "Dirección", max_length=200, blank=True, null=True)
    telefono = models.CharField(
        "Teléfono", max_length=15, blank=True, null=True)
    creator = CurrentUserField(add_only=True, related_name="created_cliente")
    last_editor = CurrentUserField(related_name="last_edited_cliente")
    cuenta = models.ForeignKey(Cuenta, related_name="mi_cliente")
    eliminado = models.BooleanField(default=False)
    eliminado_por = models.ForeignKey(User, related_name="eliminado_por_cliente", blank=True, null=True)

    class Meta:
        verbose_name = "Mi cliente"
        verbose_name_plural = "Mis clientes"
    # end class

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end def
# end class


class Lugar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField(
        "Dirección", max_length=400, blank=True, null=True)
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)
    creator = CurrentUserField(add_only=True, related_name="created_lugar")
    last_editor = CurrentUserField(related_name="last_edited_lugar")
    cuenta = models.ForeignKey(Cuenta)
    eliminado = models.BooleanField(default=False)
    eliminado_por = models.ForeignKey(User, related_name="eliminado_por_lugar", blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end class
# end class


class Tarea(models.Model):
    cuenta = models.ForeignKey(Cuenta)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField("Descripción", max_length=400)
    #fecha_ejecucion = models.DateTimeField()
    lugar = models.ForeignKey(Lugar, blank=True, null=True)
    cliente = models.ForeignKey(Cliente, blank=True, null=True)
    empleados = models.ManyToManyField(usuarios.Empleado, blank=True)
    creator = CurrentUserField(add_only=True, related_name="created_tarea")
    last_editor = CurrentUserField(related_name="last_edited_tarea")
    grupo = models.ForeignKey(usuarios.Grupo, blank=True, null=True)
    sub_complete = models.BooleanField()  # Indica que esta tarea no se puede completar si sus subtareas no estan completadas
    crontab = models.OneToOneField(CrontabDateSchedule, blank=True, null=True)
    interval = models.OneToOneField(IntervalSchedule, blank=True, null=True)
    eliminado = models.BooleanField(default=False)
    eliminado_por = models.ForeignKey(User, related_name="eliminado_por_tarea", blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end def
# end class

class SubTarea(models.Model):
    tarea = models.ForeignKey(Tarea)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField("Descripción", max_length=400)
    creator = CurrentUserField(add_only=True, related_name="created_subtarea")
    last_editor = CurrentUserField(related_name="last_edited_subtarea")
    eliminado = models.BooleanField(default=False)
    eliminado_por = models.ForeignKey(User, related_name="eliminado_por_sub_tarea", blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end def
# end class


class Completado(models.Model):
    tarea = models.OneToOneField(Tarea)
    fecha = models.DateTimeField(auto_now_add=True)
    terminado = models.BooleanField(default=True)
    creator = CurrentUserField(add_only=True, related_name="created_completado")
    last_editor = CurrentUserField(related_name="last_edited_completado")

    def __unicode__(self):
        return u'Tarea %s completada' % (self.tarea.nombre, )
    # end def
# end class


class Multimedia(models.Model):
    FOTO = 1
    MULTIMEDIA = 2
    choices = (
        (FOTO, 'Foto'),
        (MULTIMEDIA, 'Multimedia')
    )
    fecha = models.DateTimeField(auto_now_add=True)
    tarea = models.ForeignKey(Tarea)
    archivo = models.FileField()
    tipo = models.IntegerField(choices=choices)
# end class

class CompletadoSub(models.Model):
    subtarea = models.OneToOneField(SubTarea)
    creator = CurrentUserField(add_only=True, related_name="created_completadosub")
    last_editor = CurrentUserField(related_name="last_edited_completadosub")
    fecha = models.DateTimeField(auto_now_add=True)
# end class
