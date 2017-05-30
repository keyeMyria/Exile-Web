# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from operacion import models as operacion
import re
from django.core import validators
# Create your models here.


class Cliente(User):
    identificacion = models.CharField(max_length=100)
    direccion = models.CharField(
        "Dirección", max_length=200, blank=True, null=True)
    telfono = models.CharField(
        "Teléfono", max_length=15, blank=True, null=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
    # end class

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    # end def

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    # end def
# end class


class Modulo(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    descripcion = models.CharField(max_length=800, blank=True, null=True)
    estado = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end def

    def __str__(self):
        return u'%s' % (self.nombre)
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
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=800, null=True)
    modulo = models.ForeignKey(Modulo)
    funcionalidades = models.ManyToManyField(Funcionalidad)
    estado = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s --> %s' % (self.modulo.nombre, self.nombre)
    # end def

    def __str__(self):
        return u'%s --> %s' % (self.modulo.nombre, self.nombre)
    # end def

    class Meta:
        verbose_name = "Modulo plan"
        verbose_name_plural = "Modulos de planes"
    # end class
# end class


class Plan(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=800, null=True, blank=True)
    operadores = models.IntegerField(verbose_name='Número de operadores',default=0)
    asistentes = models.IntegerField(verbose_name='Número de asistentes',default=0)
    duracion = models.IntegerField(verbose_name='Dias de duración en meses',default=0)
    valor = models.FloatField(default=0)
    modulos = models.ManyToManyField(InstModulo)
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


class Suscripcion(models.Model):
    plan = models.ForeignKey(Plan)
    inscripcion = models.DateTimeField(auto_now_add=True, verbose_name='Inscripción',blank=True, null=True)
    inicio = models.DateTimeField(blank=True, null=True)
    fin = models.DateTimeField(blank=True, null=True)
    activa = models.BooleanField(default=False)
    estado = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s' % (self.plan.nombre)
    # end def

    def __str__(self):
        return u'%s' % (self.plan.nombre)
    # end def

    class Meta:
        verbose_name = "Suscripción"
        verbose_name_plural = "Subscripciones"
    # end class
#end class


class Factura(models.Model):
    suscripcion = models.ForeignKey(Suscripcion)
    realizacion = models.DateTimeField(auto_now_add=True)
    paga = models.BooleanField(default=False)
    estado = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s' % (self.plan.nombre)
    # end def

    def __str__(self):
        return u'%s' % (self.plan.nombre)
    # end def

    class Meta:
        verbose_name = "Suscripción"
        verbose_name_plural = "Subscripciones"
    # end class
#end class

class Cuenta(models.Model):
    cliente = models.ForeignKey(Cliente)
    suscripciones = models.ManyToManyField(Suscripcion)
    estado = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s' % (self.plan.nombre)
    # end def

    def __str__(self):
        return u'%s' % (self.plan.nombre)
    # end def

    class Meta:
        verbose_name = "Cuenta"
        verbose_name_plural = "Cuentas"
    # end class
#end class
