# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.db.models import Q
from usuarios import models as usuarios
from django.contrib.auth.forms import UserCreationForm
from exile.servicios import get_cuenta
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
        if get_cuenta():
            return super(AsistenteForm, self).clean()
        # end if
        raise forms.ValidationError(
            "Este usuario no esta asociado a una cuenta")
    # end def

    def save(self, commit=False):
        usuario = super(AsistenteForm, self).save(commit)
        if get_cuenta():
            usuario.cuenta = get_cuenta()
            usuario.save()
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
                  'fecha_nacimiento', 'direccion', 'telefono', 'fijo', 'imagen', 'eliminado']
    # end class
# end class


class CargoForm(forms.ModelForm):

    class Meta:
        model = usuarios.Cargo
        fields = ['nombre', ]
    # end class

    def clean(self):
        if get_cuenta():
            return super(CargoForm, self).clean()
        # end if
        raise forms.ValidationError(
            "Este usuario no esta asociado a una cuenta")
    # end def

    def save(self, commit=False):
        cargo = super(CargoForm, self).save(commit)
        if get_cuenta():
            cargo.cuenta = get_cuenta()
            cargo.save()
        # end if
        return cargo
    # end def
# end class


class CargoFormEdit(forms.ModelForm):

    class Meta:
        model = usuarios.Cargo
        fields = ['nombre', 'eliminado']
    # end class
# end class
