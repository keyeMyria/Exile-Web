# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Cliente(User):
    identificacion = models.CharField(max_length=25, unique=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    # end def

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    # end def

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
    # end class
# end class


class Modulo(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    descripcion = models.CharField(max_length=800, blank=True, null=True)
    estado = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    # end def

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    # end def

    class Meta:
        verbose_name = "Modulo"
        verbose_name_plural = "Modulos"
    # end class
# end class


class Funcionalidad(models.Model):
    modulo = models.ForeignKey(Modulo)
    nombre = models.CharField(max_length=30, unique=True)
    url = models.URLField(max_length=300, blank=True, null=True)
    descripcion = models.CharField(max_length=800, blank=True, null=True)
    estado = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s --> %s' % (self.modulo.nombre, self.nombre)
    # end def

    def __str__(self):
        return u'%s --> %s' % (self.modulo.nombre, self.nombre)
    # end def

    class Meta:
        verbose_name = "Funcionalidad"
        verbose_name_plural = "Funcionalidades"
    # end class
# end class


class InstModulo(models.Model):
    modulo = models.ForeignKey(Modulo)
    funcionalidades = models.ManyToManyField(Funcionalidad)
    estado = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s' % (self.modulo.nombre)
    # end def

    def __str__(self):
        return u'%s' % (self.modulo.nombre)
    # end def

    class Meta:
        verbose_name = "Funcionalidad plan"
        verbose_name_plural = "Funcionalidades planes"
    # end class
# end class


class Plan(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=800)
    modulos = models.ManyToManyField(InstModulo)

    def __unicode__(self):
        return u'%s' % (self.modulo.nombre)
    # end def

    def __str__(self):
        return u'%s' % (self.modulo.nombre)
    # end def

    class Meta:
        verbose_name = "Funcionalidad plan"
        verbose_name_plural = "Funcionalidades planes"
    # end class
# end class
