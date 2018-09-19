# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.db.models import Q
from usuarios import models as usuarios
from django.contrib.auth.forms import UserCreationForm
from exile.servicios import get_cuenta
from subcripcion.models import Cuenta
from cuser.middleware import CuserMiddleware
from subcripcion.models import Cliente
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))
# end class

class PerfilForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class MasterU(forms.ModelForm):
    identificacion2 = forms.CharField(widget=forms.NumberInput() , label="Verificar número identificación")

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
            usuario.username = usuario.identificacion
            usuario.set_password(raw_password=usuario.identificacion)
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

    def clean(self):
        if get_cuenta():
            return super(MasterEdit, self).clean()
        # end if
        raise forms.ValidationError(
            "Este usuario no esta asociado a una cuenta")
    # end def

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

    def clean_identificacion(self):
        identificacion = self.cleaned_data['identificacion']
        if identificacion:
            user = User.objects.filter(username=identificacion).first()
            medico = usuarios.Asistente.objects.filter(identificacion=identificacion).first()
            if hasattr(self, 'instance') and self.instance.pk:
                if user.id != self.instance.id:
                    raise forms.ValidationError('Ya existe un usuario con este username')
                # end if
                if medico != self.instance:
                    raise forms.ValidationError('Ya existe un usuario con esta identificación')
                # end if
                return identificacion
            else:
                if user:
                    raise forms.ValidationError('Ya existe un usuario con este username')
                # end if
                if medico:
                    raise forms.ValidationError('Ya existe un usuario con esta identificación')
                # end if
                return identificacion
        # end if
        raise forms.ValidationError('Este campo es requerido')
    # end def

    def clean_identificacion2(self):
        identificacion = self.cleaned_data.get('identificacion', False)
        identificacion2 = self.cleaned_data.get('identificacion2', False)
        if identificacion2:
            if identificacion2 == identificacion:
                return identificacion
            else:
                raise forms.ValidationError("Los números de identificación no coinciden")
            # end if
        else:
            raise forms.ValidationError("Este campo es requerido")
        # end if
    # end def

    class Meta:
        model = usuarios.Asistente
        fields = ['email', 'first_name', 'last_name', 'identificacion', 'identificacion2',
                    'fecha_nacimiento', 'direccion', 'telefono', 'fijo', 'imagen']
        widgets = {
            'identificacion': forms.NumberInput(),
            'telefono': forms.NumberInput(),
            'fijo': forms.NumberInput()
        }
    # end class
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
        fields = ['email', 'first_name', 'last_name', 'identificacion',
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

    def clean_identificacion(self):
        identificacion = self.cleaned_data['identificacion']
        if identificacion:
            user = User.objects.filter(username=identificacion).first()
            medico = usuarios.Empleado.objects.filter(identificacion=identificacion).first()
            if hasattr(self, 'instance') and self.instance.pk:
                if user.id != self.instance.id:
                    raise forms.ValidationError('Ya existe un usuario con este username')
                # end if
                if medico != self.instance:
                    raise forms.ValidationError('Ya existe un usuario con esta identificación')
                # end if
                return identificacion
            else:
                if user:
                    raise forms.ValidationError('Ya existe un usuario con este username')
                # end if
                if medico:
                    raise forms.ValidationError('Ya existe un usuario con esta identificación')
                # end if
                return identificacion
        # end if
        raise forms.ValidationError('Este campo es requerido')
    # end def

    def clean_identificacion2(self):
        identificacion = self.cleaned_data.get('identificacion', False)
        identificacion2 = self.cleaned_data.get('identificacion2', False)
        if identificacion2:
            if identificacion2 == identificacion:
                return identificacion
            else:
                raise forms.ValidationError("Los números de identificación no coinciden")
            # end if
        else:
            raise forms.ValidationError("Este campo es requerido")
        # end if
    # end def

    class Meta:
        model = usuarios.Empleado
        fields = ['email', 'first_name', 'last_name', 'identificacion', 'fecha_nacimiento',
                    'fecha_ingreso', 'fecha_retiro', 'cargo', 'direccion', 'telefono', 'fijo', 'imagen']
        widgets = {
            'identificacion': forms.NumberInput(),
            'telefono': forms.NumberInput(),
            'fijo': forms.NumberInput()
        }
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
        fields = ['email', 'first_name', 'last_name', 'identificacion',
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


class ClienteAvatar(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['imagen', ]
    # end class
# end class


class AsistenteAvatar(forms.ModelForm):

    class Meta:
        model = usuarios.Asistente
        fields = ['imagen', ]
    # end class
# end class


class EmpleadoAvatar(forms.ModelForm):

    class Meta:
        model = usuarios.Empleado
        fields = ['imagen', ]
    # end class
# end class
