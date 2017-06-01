# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.db.models import Q
from usuarios import models as usuarios
from django.contrib.auth.forms import UserCreationForm
from cuser.middleware import CuserMiddleware
from subcripcion.models import Cuenta


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))
# end class


class AsistenteForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(AsistenteForm, self).__init__(*args, **kwargs)
        self.fields['fecha_nacimiento'].input_formats = (
            '%Y/%m/%d', '%d/%m/%Y', '%m/%d/%Y')
    # end def

    class Meta:
        model = usuarios.Asistente
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name',
                  'identificacion', 'fecha_nacimiento', 'direccion', 'telefono', 'fijo', 'imagen']

    def clean(self):
        user = CuserMiddleware.get_user()
        cuenta = Cuenta.objects.filter(
            Q(cliente=user.pk) | Q(usuario=user.pk)).first()
        if cuenta:
            return super(AsistenteForm, self).clean()
        # end if
        raise forms.ValidationError(
            "Este usuario no esta asociado a una cuenta")
    # end def

    def save(self, commit=False):
        usuario = super(AsistenteForm, self).save(commit)
        user = CuserMiddleware.get_user()
        if user:
            cuenta = Cuenta.objects.filter(
                Q(cliente=user.pk) | Q(usuario=user.pk)).first()
            if cuenta:
                usuario.cuenta = cuenta
                usuario.save()
            # end if
        # end if
        return usuario
    # end def
# end class


class AsistenteFormEdit(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AsistenteFormEdit, self).__init__(*args, **kwargs)
        self.fields['fecha_nacimiento'].input_formats = (
            '%Y/%m/%d', '%d/%m/%Y', '%m/%d/%Y')
        self.fields['fecha_nacimiento'].format = "m/d/y"
    # end def

    class Meta:
        model = usuarios.Asistente
        fields = ['username', 'email', 'first_name', 'last_name', 'identificacion',
                  'fecha_nacimiento', 'direccion', 'telefono', 'fijo', 'imagen']
    # end class
# end class
