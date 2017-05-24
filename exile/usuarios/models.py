# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Usuario(User):
    identificacion = models.CharField(
        max_length=120, verbose_name="Identificación", unique=True)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento")
    direccion = models.CharField(max_length=120, verbose_name="Dirección")
    telefono = models.CharField(
        max_length=15, verbose_name="Teléfono", blank=True, null=True)
    fijo = models.CharField(
        max_length=15, verbose_name="Fijo", blank=True, null=True)
    imagen = models.ImageField(upload_to="avatar", null=True, blank=True)

    def avatar(self):
        if self.imagen:
            imagen = self.imagen
        else:
            imagen = 'account.svg'
        # end if
        return '<img class="image-cicle" src="/media/%s" />' % (imagen)
    # end def

    avatar.allow_tags = True

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    # end def
# end class


class Cargo(models.Model):
    nombre = models.CharField(max_length=100)
# end class


class Empleado(Usuario):
    cargo = models.ForeignKey(Cargo)
    fecha_ingreso = models.DateField(verbose_name="Fecha de Ingreso", blank=True, null=True)
    fecha_retiro = models.DateField(verbose_name="Fecha de Retiro", blank=True, null=True)
    # end class
# end class


class Grupo(models.Model):
    nombre = models.CharField(max_length=100)
    empleados = models.ManyToManyField(Empleado)
# end class


class Asistente(Usuario):

    class Meta:
        verbose_name = "Asistente"
        verbose_name_plural = "Asistentes"
    # end class
# end class
