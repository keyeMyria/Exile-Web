# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from cuser.fields import CurrentUserField
from operacion import models as operacion
from django.contrib.auth.models import User
from subcripcion.models import Cuenta
# Create your models here.


class TipoReporte(models.Model):
    cuenta = models.ForeignKey(Cuenta)
    nombre = models.CharField(max_length=100)
    creator = CurrentUserField(add_only=True, related_name="created_tipo_re")
    last_editor = CurrentUserField(related_name="last_edited_tipo_re")
    eliminado = models.BooleanField(default=False)
    eliminado_por = models.ForeignKey(User, related_name="eliminado_por_tipo_re", blank=True, null=True)

    class Meta:
        verbose_name = "Tipo de reporte"
        verbose_name_plural = "Tipos de reportes"
    # end class

    def __unicode__(self):
        return u"%s" % (self.nombre)
    # end def
# end class


class Reporte(models.Model):
    cuenta = models.ForeignKey(Cuenta)
    cerrado = (
        (False, "Abierto"),
        (True, "Cerrado")
    )
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=400)
    tipo = models.ForeignKey(TipoReporte, blank=True, null=True)
    cliente = models.ForeignKey(operacion.Cliente, blank=True, null=True)
    lugar = models.ForeignKey(operacion.Lugar, blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    creator = CurrentUserField(add_only=True, related_name="created_reporte")
    last_editor = CurrentUserField(related_name="last_edited_reporte")
    estado = models.BooleanField(default=False, choices=cerrado)
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)
    eliminado = models.BooleanField(default=False)
    eliminado_por = models.ForeignKey(User, related_name="eliminado_por_reporte", blank=True, null=True)
    # resend = models.BooleanField(default=False, verbose_name="Re enviar al cliente")

    def __unicode__(self):
        return u'%s %s, creado por: %s' % (self.nombre, self.fecha.strftime('%Y-%m-%d %H:%M:%S'), self.creator.username)
    # end def
# end class


class FotoReporte(models.Model):
    foto = models.FileField(upload_to="fotos")
    reporte = models.ForeignKey(Reporte)

    class Meta:
        verbose_name = "Foto de reporte"
        verbose_name_plural = "Fotos de reportes"
    # end class

    def foto(self):
        if self.foto:
            url = self.foto
        else:
            url = 'no-imagen.svg'
        # end if
        return '<img src="/media/%s" width=50px heigth=50px/>' % (url)
    # end def

    foto.allow_tags = True

    def __unicode__(self):
        return u"%s" % (self.foto, )
    # end def
# end class
