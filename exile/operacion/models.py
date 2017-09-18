# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from usuarios import models as usuarios
from django.contrib.auth.models import User
from cuser.fields import CurrentUserField
from subcripcion.models import Cuenta
from djcelery.models import CrontabSchedule, IntervalSchedule, PeriodicTask

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
    direccion = models.TextField("Dirección", max_length=400, blank=True, null=True)
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
    fecha = models.DateTimeField(auto_now_add=True)
    cuenta = models.ForeignKey(Cuenta)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField("Descripción", max_length=400)
    #GPS
    latitud = models.CharField(max_length=100)
    longitud = models.CharField(max_length=100)

    lugar = models.ForeignKey(Lugar, blank=True, null=True)
    cliente = models.ForeignKey(Cliente, blank=True, null=True)
    empleados = models.ManyToManyField(usuarios.Empleado, blank=True)
    grupo = models.ForeignKey(usuarios.Grupo, blank=True, null=True)
    sub_complete = models.BooleanField()

    # Indica que esta tarea no se puede completar si sus subtareas no estan completadas

    fecha_ejecucion = models.DateTimeField()
    fecha_finalizacion = models.DateTimeField(null=True, blank=True)
    cron_ejecucion = models.OneToOneField(PeriodicTask, blank=True, null=True)
    
    crontab = models.OneToOneField(CrontabSchedule, blank=True, null=True)
    interval = models.OneToOneField(IntervalSchedule, blank=True, null=True)
    
    creator = CurrentUserField(add_only=True, related_name="created_tarea")
    fecha_edicion = models.DateTimeField(auto_now=True)
    last_editor = CurrentUserField(related_name="last_edited_tarea")
    eliminado = models.BooleanField(default=False)
    eliminado_por = models.ForeignKey(User, related_name="eliminado_por_tarea", blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end def
# end class

class Notificacion(models.Model):
    tarea = models.ForeignKey(Tarea)
    fecha = models.DateField(auto_now_add=True)

    #GPS
    latitud = models.CharField(max_length=100)
    longitud = models.CharField(max_length=100)

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField("Descripción", max_length=400)
# end class

class SubTarea(models.Model):
    tarea = models.ForeignKey(Tarea)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField("Descripción", max_length=400)

    #GPS
    latitud = models.CharField(max_length=100)
    longitud = models.CharField(max_length=100)

    creator = CurrentUserField(add_only=True, related_name="created_subtarea")
    last_editor = CurrentUserField(related_name="last_edited_subtarea")
    eliminado = models.BooleanField(default=False)
    eliminado_por = models.ForeignKey(User, related_name="eliminado_por_sub_tarea", blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end def
# end class

class SubNotificacion(models.Model):
    fecha = models.DateField(auto_now_add=True)
    notificacion = models.ForeignKey(Notificacion)
    subtarea = models.ForeignKey(SubTarea)

    #GPS
    latitud = models.CharField(max_length=100)
    longitud = models.CharField(max_length=100)

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField("Descripción", max_length=400)
# end class

class Completado(models.Model):
    notificacion = models.ForeignKey(Notificacion)    

    #GPS
    latitud = models.CharField(max_length=100)
    longitud = models.CharField(max_length=100)

    descompletado = models.BooleanField(default=False)
    descompletado_por = models.ForeignKey(User, related_name="descompletado_por_completado", blank=True, null=True)

    fecha = models.DateTimeField(auto_now_add=True)
    creator = CurrentUserField(add_only=True, related_name="created_completado")
    last_editor = CurrentUserField(related_name="last_edited_completado")

    def __unicode__(self):
        return u'Tarea %s completada' % (self.tarea.nombre, )
    # end def
# end class


class Multimedia(models.Model):
    FOTO = 1
    AUDIO = 2
    choices = (
        (FOTO, 'Foto'),
        (AUDIO, 'Audio')
    )
    fecha = models.DateTimeField(auto_now_add=True)
    notificacion = models.ForeignKey(Notificacion)
    tipo = models.IntegerField(choices=choices)
    archivo = models.FileField()
# end class

class CompletadoSub(models.Model):
    subnotificacion = models.ForeignKey(SubNotificacion)

    #GPS
    latitud = models.CharField(max_length=100)
    longitud = models.CharField(max_length=100)

    descompletado = models.BooleanField(default=False)
    descompletado_por = models.ForeignKey(User, related_name="descompletado_por_completado_sub", blank=True, null=True)

    creator = CurrentUserField(add_only=True, related_name="created_completadosub")
    last_editor = CurrentUserField(related_name="last_edited_completadosub")
    fecha = models.DateTimeField(auto_now_add=True)
# end class
