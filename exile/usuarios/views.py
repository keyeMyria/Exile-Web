# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from supra import views as supra
from django.contrib.auth import login, logout, authenticate
from django.utils.decorators import method_decorator
from exile.decorator import check_login, get_cuenta
from django.http import HttpResponse
from django.db.models import Q
from cuser.middleware import CuserMiddleware
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from subcripcion.models import Cliente
from subcripcion import decorators as asp_subcrip
from exile.settings import ORIGIN
import forms
import models
import json as simplejson

# Create your views here.
supra.SupraConf.ACCECC_CONTROL["allow"] = True
supra.SupraConf.ACCECC_CONTROL["origin"] = ORIGIN
supra.SupraConf.ACCECC_CONTROL["credentials"] = "true"
supra.SupraConf.ACCECC_CONTROL["headers"] = "origin, content-type, accept"
supra.SupraConf.ACCECC_CONTROL["methods"] = "POST, GET, PUT, DELETE, OPTIONS"
supra.SupraConf.body = True
supra.SupraListView.date_format = '%m/%d/%Y'


class UserDetail(supra.SupraDetailView):
    model = User
    list_display  = ['id', 'first_name', 'last_name', 'email', 'username', 'avatar']

    def avatar(self, obj, row):
        cliente = Cliente.objects.filter(id=obj["id"]).first()
        if cliente:
            return "/media/%s" % (cliente.imagen)
        # end if
        asistente = models.Asistente.objects.filter(id=obj["id"]).first()
        if asistente:
            return "/media/%s" % (asistente.imagen)
        # end if
        empleado = models.Empleado.objects.filter(id=obj["id"]).first()
        if empleado:
            return "/media/%s" % (empleado.imagen)
        # end if
        return None
    # end def
# end class

class LoginU(supra.SupraSession):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        a = super(LoginU, self).dispatch(request, *args, **kwargs)
        return a
    # end def
# end class


class LoginE(supra.SupraSession):
    model = models.Empleado

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        a = super(LoginE, self).dispatch(request, *args, **kwargs)
        return a
    # end def
# end class


@supra.access_control
def logoutUser(request):
    logout(request)
    return HttpResponse(status=200)
# end def

@supra.access_control
@get_cuenta
def islogin(cuenta, request):
    if request.user.is_authenticated():
        if cuenta:
            if cuenta.cliente.id == request.user.pk:
                if cuenta.cliente.imagen:
                    avatar = "/media/%s" % (cuenta.cliente.imagen)
                else:
                    avatar = None

                url = "/usuarios/avatar/cliente/%d/" % (cuenta.cliente.id)
                data = {"url_avatar": url, "session": request.session.session_key, "username": request.user.username, "first_name": request.user.first_name, "last_name": request.user.last_name, "email": request.user.email, "cuenta": cuenta.id, "avatar": avatar,  "ws": "noti/%d/" % (cuenta.id), "cargo": "Administrador"}
                return HttpResponse(simplejson.dumps(data), 200)

            else:
                asistente = models.Asistente.objects.filter(id=request.user.id).first()
                if asistente:
                    if asistente.imagen:
                        avatar = "/media/%s" % (asistente.imagen)
                    else:
                        avatar = None

                    url = "/usuarios/avatar/asistente/%d/" % (asistente.id)
                    data = {"url_avatar": url, "session": request.session.session_key, "username": request.user.username, "first_name": request.user.first_name, "last_name": request.user.last_name, "email": request.user.email, "cuenta": cuenta.id, "avatar": avatar,  "ws": "noti/%d/" % (cuenta.id), "cargo": "Asistente"}
                    return HttpResponse(simplejson.dumps(data), 200)

                empleado = models.Empleado.objects.filter(id=request.user.id).first()
                if empleado:
                    if empleado.imagen:
                        avatar = "/media/%s" % (empleado.imagen)
                    else:
                        avatar = None

                    if empleado.cargo:
                        cargo = empleado.cargo.nombre
                    else:
                        cargo = None

                    url = "/usuarios/avatar/empleado/%d/" % (empleado.id)
                    data = {"url_avatar": url, "session": request.session.session_key, "username": request.user.username, "first_name": request.user.first_name, "last_name": request.user.last_name, "email": request.user.email, "cuenta": cuenta.id, "avatar": avatar,  "ws": "noti/%d/" % (cuenta.id), "cargo": cargo}
                    return HttpResponse(simplejson.dumps(data), 200)
        # end if
        return HttpResponse(simplejson.dumps({"session": request.session.session_key, "username": request.user.username, "first_name": request.user.first_name, "last_name": request.user.last_name}), 200)
    # end if
    return HttpResponse([], 400)
# end if



class MasterList(supra.SupraListView):
    search_key = 'q'
    list_filter = ["id"]

    @method_decorator(check_login)
    def dispatch(self, request, *args, **kwargs):
        return super(MasterList, self).dispatch(request, *args, **kwargs)
    # end def

    @method_decorator(get_cuenta)
    def get_queryset(self, cuenta):
        queryset = super(MasterList, self).get_queryset()
        if self.request.GET.get('length', False):
            self.paginate_by = self.request.GET.get('length', False)
        # end if
        propiedad = self.request.GET.get('sort_property', False)
        orden = self.request.GET.get('sort_direction', False)
        eliminado = self.request.GET.get('eliminado', False)
        if eliminado == '1':
            if cuenta:
                queryset = queryset.filter(cuenta=cuenta.id, eliminado=True)
        else:
            if cuenta:
                queryset = queryset.filter(cuenta=cuenta.id, eliminado=False)
        # end if
        if propiedad and orden:
            if orden == "asc":
                queryset = queryset.order_by(propiedad)
            elif orden == "desc":
                propiedad = "-" + propiedad
                queryset = queryset.order_by(propiedad)
        # end if
        return queryset
    # end def
# end class


"""
    Servicios de Asistente
"""


class AsistenteSupraForm(supra.SupraFormView):
    model = models.Asistente
    form_class = forms.AsistenteForm
    response_json = False

    # @method_decorator([check_login,asp_subcrip.user_plan_asistente,asp_subcrip.user_plan_validar])
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(AsistenteSupraForm, self).dispatch(request, *args, **kwargs)
    # end def

    def get_form_class(self):
        if 'pk' in self.http_kwargs:
            self.form_class = forms.AsistenteFormEdit
        # end if
        return self.form_class
    # end class
# end class


class AsistenteSupraFormDelete(supra.SupraDeleteView):
    model = models.Asistente

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(AsistenteSupraFormDelete, self).dispatch(request, *args, **kwargs)
    # end def

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.eliminado = True
        user = CuserMiddleware.get_user()
        self.object.eliminado_por = user
        self.object.save()
        return HttpResponse(status=200)
    # end def
# end class


class AsistenteList(MasterList):
    model = models.Asistente
    list_display = ['first_name', 'last_name', 'username', 'identificacion', 'fecha_nacimiento', 'email', 'direccion',
                    'telefono', 'fijo', 'creator', 'last_editor', 'imagen', 'id', 'cuenta']
    search_fields = ['first_name', 'last_name',
                     'identificacion', 'email', 'username']
    paginate_by = 10


    def avatar(self, obj, now):
        if obj.imagen:
            return "/media/%s" % (obj.imagen)
        # end if
        return None
    # end def
# end class


"""
    Servicios de Cargo
"""


class CargoSupraForm(supra.SupraFormView):
    model = models.Cargo
    form_class = forms.CargoForm
    response_json = False

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(CargoSupraForm, self).dispatch(request, *args, **kwargs)
    # end def

    def get_form_class(self):
        if 'pk' in self.http_kwargs:
            self.form_class = forms.CargoFormEdit
        # end if
        return self.form_class
    # end class
# end class


class CargoDeleteSupra(supra.SupraDeleteView):
    model = models.Cargo

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(CargoDeleteSupra, self).dispatch(request, *args, **kwargs)
    # end def

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.eliminado = True
        user = CuserMiddleware.get_user()
        self.object.eliminado_por = user
        self.object.save()
        return HttpResponse(status=200)
    # end def
# end class


class CargoList(MasterList):
    model = models.Cargo
    list_display = ['nombre', 'fecha', 'id']
    search_fields = ['nombre', ]
    paginate_by = 10
# end class


"""
    Servicios de empleado
"""


class EmpleadoSupraForm(supra.SupraFormView):
    model = models.Empleado
    form_class = forms.EmpleadoForm
    response_json = False

    # @method_decorator([check_login,asp_subcrip.user_plan_asistente,asp_subcrip.user_plan_validar])
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(EmpleadoSupraForm, self).dispatch(request, *args, **kwargs)
    # end def

    def get_form_class(self):
        if 'pk' in self.http_kwargs:
            self.form_class = forms.EmpleadoFormEdit
        # end if
        return self.form_class
    # end class
# end class


class EmpleadoSupraFormDelete(supra.SupraDeleteView):
    model = models.Empleado

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(EmpleadoSupraFormDelete, self).dispatch(request, *args, **kwargs)
    # end def

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.eliminado = True
        user = CuserMiddleware.get_user()
        self.object.eliminado_por = user
        self.object.save()
        return HttpResponse(status=200)
    # end def
# end class


class StackEmpleadoList(supra.SupraListView):
    model = models.Empleado
    list_display = ['first_name', 'last_name', 'username', 'identificacion', 'fecha_nacimiento', 'email', 'direccion',
                    'telefono', 'fijo', 'creator', 'last_editor', 'fecha_ingreso', 'fecha_retiro', 'cargo', 'cargo__nombre',
                    'imagen', 'id', 'cuenta']
    list_filter = ['pk', 'grupo']
# end class

class EmpleadoList(MasterList):
    model = models.Empleado
    list_display = ['first_name', 'last_name', 'username', 'identificacion', 'fecha_nacimiento', 'email', 'direccion',
                    'telefono', 'fijo', 'creator', 'last_editor', 'fecha_ingreso', 'fecha_retiro', 'cargo', 'cargo__nombre',
                    'imagen', 'id', 'cuenta']
    search_fields = ['first_name', 'last_name',
                     'identificacion', 'email', 'username']
    list_filter = ['pk', 'grupo', 'tarea']
    paginate_by = 10
# end class


"""
    Servicios grupo
"""


class GrupoSupraForm(supra.SupraFormView):
    model = models.Grupo
    form_class = forms.GrupoForm
    response_json = False

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(GrupoSupraForm, self).dispatch(request, *args, **kwargs)
    # end def

    def get_form_class(self):
        if 'pk' in self.http_kwargs:
            self.form_class = forms.GrupoFormEdit
        # end if
        return self.form_class
    # end class
# end class


class GrupoSupraFormDelete(supra.SupraDeleteView):
    model = models.Grupo

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(GrupoSupraFormDelete, self).dispatch(request, *args, **kwargs)
    # end def

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.eliminado = True
        user = CuserMiddleware.get_user()
        self.object.eliminado_por = user
        self.object.save()
        return HttpResponse(status=200)
    # end def
# end class


class GrupoList(MasterList):
    model = models.Grupo
    list_display = ['nombre', 'empleados', 'id']
    search_fields = ['nombre', ]
    paginate_by = 10

    def empleados(self, obj, row):
        lista = []
        if obj:
            empleados = models.Empleado.objects.filter(grupo=obj.pk).values('id')
            for e in empleados:
                lista.append(e['id'])
            # end class
            return lista
        return lista
    # end def
# end class

@csrf_exempt
@check_login
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return HttpResponse(status=200)

        errors = form.errors.items()
        return HttpResponse(simplejson.dumps(errors),content_type='application/json', status=400)
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'usuarios/change_password.html', {
        'form': form
    })


class AvatarClienteForm(supra.SupraFormView):
    model = Cliente
    form_class = forms.ClienteAvatar
    response_json = False

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(AvatarClienteForm, self).dispatch(request, *args, **kwargs)
    # end def
# end class


class AvatarAsistenteForm(supra.SupraFormView):
    model = models.Asistente
    form_class = forms.AsistenteAvatar
    response_json = False

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(AvatarAsistenteForm, self).dispatch(request, *args, **kwargs)
    # end def
# end class


class AvatarEmpleadoForm(supra.SupraFormView):
    model = models.Empleado
    form_class = forms.EmpleadoAvatar
    response_json = False

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(AvatarEmpleadoForm, self).dispatch(request, *args, **kwargs)
    # end def
# end class
