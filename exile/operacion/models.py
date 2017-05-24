# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from usuarios import models as usuarios
from django.contrib.auth.models import User
# Create your models here.


class Tipo(models.Model):
    nombre = models.CharField(max_length=100)

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
    telfono = models.CharField(
        "Teléfono", max_length=15, blank=True, null=True)

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

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end class
# end class


class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField("Descripción", max_length=400)
    fecha_de_ejecucion = models.DateField()
    repetir_cada = models.TextField(default=0)
    empleados = models.ManyToManyField(usuarios.Empleado)
    grupos = models.ForeignKey(usuarios.Grupo, blank=True, null=True)
    sub_complete = models.BooleanField()  # Indica que esta tarea no se puede completar si sus subtareas no estan completadas
    unidad_de_repeticion = models.IntegerField(choices=(
        (3, "Mes(es)", ), (4, "Año(s)", ), ), null=True, blank=True, default=3)
    # Por cuando se repite

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end def
# end class


class SubTarea(models.Model):
    tarea = models.ForeignKey(Tarea)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField("Descripción", max_length=400)

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end def
# end class


class Completado(models.Model):
    tarea = models.ForeignKey(Tarea)
    usuario = models.ForeignKey(User)
    fecha = models.DateTimeField(auto_now_add=True)
    terminado = models.BooleanField(default=False)

    def __unicode__(self):
        return u'Tarea %s completada %s' % (self.tarea.nombre)
    # end def
# end class


class Multimedia(models.Model):
    completado = models.ForeignKey(Completado)
    archivo = models.FileField()
    audio = models.BooleanField()
    foto = models.BooleanField()
# end class


class CompletadoSub(models.Model):
    subtarea = models.ForeignKey(SubTarea)
    usuario = models.ForeignKey(User)
    fecha = models.DateTimeField(auto_now_add=True)
# end class
