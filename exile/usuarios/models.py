# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from cuser.fields import CurrentUserField
from subcripcion.models import Cuenta


class Usuario(User):
    cuenta = models.ForeignKey(Cuenta)
    identificacion = models.CharField(
        max_length=120, verbose_name="Identificación", unique=True)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento")
    direccion = models.CharField(max_length=120, verbose_name="Dirección")
    telefono = models.CharField(
        max_length=15, verbose_name="Teléfono", blank=True, null=True)
    fijo = models.CharField(
        max_length=15, verbose_name="Fijo", blank=True, null=True)
    imagen = models.ImageField(upload_to="avatar", null=True, blank=True)
    creator = CurrentUserField(add_only=True, related_name="created_user")
    last_editor = CurrentUserField(related_name="last_edited_user")
    eliminado = models.BooleanField(default=False)
    eliminado_por = models.ForeignKey(User, related_name="eliminado_por_usuario", blank=True, null=True)

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
    cuenta = models.ForeignKey(Cuenta)
    nombre = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now=True)
    creator = CurrentUserField(add_only=True, related_name="created_cargo")
    last_editor = CurrentUserField(related_name="last_edited_cargo")
    eliminado = models.BooleanField(default=False)
    eliminado_por = models.ForeignKey(User, related_name="eliminado_cargo", blank=True, null=True)

    def __unicode__(self):
        return u"%s" % (self.nombre)
    # end def
# end class


class Empleado(Usuario):
    cargo = models.ForeignKey(Cargo, blank=True, null=True)
    fecha_ingreso = models.DateField(verbose_name="Fecha de Ingreso", blank=True, null=True)
    fecha_retiro = models.DateField(verbose_name="Fecha de Retiro", blank=True, null=True)

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
    # end class

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleado"
# end class


class Grupo(models.Model):
    cuenta = models.ForeignKey(Cuenta)
    nombre = models.CharField(max_length=100)
    empleados = models.ManyToManyField(Empleado)
    creator = CurrentUserField(add_only=True, related_name="created_grupo")
    last_editor = CurrentUserField(related_name="last_edited_grupo")
    eliminado = models.BooleanField(default=False)
    eliminado_por = models.ForeignKey(User, related_name="eliminado_grupo", blank=True, null=True)

    def __unicode__(self):
        return u"%s" % (self.nombre)
    # end def
# end class


class Asistente(Usuario):

    class Meta:
        verbose_name = "Asistente"
        verbose_name_plural = "Asistentes"
    # end class
# end class
