# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.db.models import Q
from usuarios import models as usuarios
from django.contrib.auth.forms import UserCreationForm
from exile.servicios import get_cuenta
from subcripcion.models import Cuenta
from cuser.middleware import CuserMiddleware


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))
# end class


class MasterU(UserCreationForm):

    def clean(self):
        if get_cuenta():
            return super(MasterU, self).clean()
        # end if
        raise forms.ValidationError(
            "Este usuario no esta asociado a una cuenta")
    # end def

    def save(self, commit=False):
        usuario = super(MasterU, self).save(commit)
        if get_cuenta():
            usuario.cuenta = get_cuenta()
            usuario.save()
        # end if
        return usuario
    # end def
# end class


class Master(forms.ModelForm):

    def clean(self):
        if get_cuenta():
            return super(Master, self).clean()
        # end if
        raise forms.ValidationError(
            "Este usuario no esta asociado a una cuenta")
    # end def

    def save(self, commit=False):
        master = super(Master, self).save(commit)
        if get_cuenta():
            master.cuenta = get_cuenta()
            master.save()
        # end if
        return master
    # end def
# end class


class MasterEdit(forms.ModelForm):

    def save(self, commit=False):
        master = super(MasterEdit, self).save(commit)
        if master.eliminado:
            user = CuserMiddleware.get_user()
            if user:
                master.eliminado_por = user
            # end if
        # end if
        master.save()
        return master
    # end def
# end class


class AsistenteForm(MasterU):

    def __init__(self, *args, **kwargs):
        super(AsistenteForm, self).__init__(*args, **kwargs)
        self.fields['fecha_nacimiento'].input_formats = (
            '%Y/%m/%d', '%d/%m/%Y', '%m/%d/%Y')
    # end def

    class Meta:
        model = usuarios.Asistente
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name',
                  'identificacion', 'fecha_nacimiento', 'direccion', 'telefono', 'fijo', 'imagen']

# end class


class AsistenteFormEdit(MasterEdit):

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


class CargoForm(Master):

    class Meta:
        model = usuarios.Cargo
        fields = ['nombre', ]
    # end class
# end class


class CargoFormEdit(MasterEdit):

    class Meta:
        model = usuarios.Cargo
        fields = ['nombre', 'eliminado']
    # end class
# end class


class EmpleadoForm(MasterU):

    def __init__(self, *args, **kwargs):
        super(EmpleadoForm, self).__init__(*args, **kwargs)
        self.fields['fecha_nacimiento'].input_formats = (
            '%Y/%m/%d', '%d/%m/%Y', '%m/%d/%Y')
    # end def

    class Meta:
        model = usuarios.Empleado
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name',
                  'identificacion', 'fecha_nacimiento', 'fecha_ingreso', 'fecha_retiro', 'cargo', 'direccion', 'telefono', 'fijo', 'imagen']

# end class


class EmpleadoFormEdit(MasterEdit):

    def __init__(self, *args, **kwargs):
        super(EmpleadoFormEdit, self).__init__(*args, **kwargs)
        self.fields['fecha_nacimiento'].input_formats = (
            '%Y/%m/%d', '%d/%m/%Y', '%m/%d/%Y')
        self.fields['fecha_nacimiento'].format = "m/d/y"
    # end def

    class Meta:
        model = usuarios.Empleado
        fields = ['username', 'email', 'first_name', 'last_name', 'identificacion',
                  'fecha_nacimiento', 'fecha_ingreso', 'fecha_retiro', 'cargo', 'direccion', 'telefono', 'fijo', 'imagen', 'eliminado']
    # end class
# end class


class GrupoForm(Master):

    class Meta:
        model = usuarios.Grupo
        fields = ['nombre', 'empleados']
    # end class
# end class


class GrupoFormEdit(MasterEdit):

    class Meta:
        model = usuarios.Grupo
        fields = ['nombre', 'empleados', 'eliminado']
    # end class
# end class
