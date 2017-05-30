# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render, redirect
from supra import views as supra
import forms
import models
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from cuser.middleware import CuserMiddleware
from django.views.generic import View, DeleteView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, get_object_or_404, HttpResponse
from django.views.generic import TemplateView
from django.views.generic.edit import BaseFormView
from django.contrib.auth.views import logout
from django.db.models import Q
# Create your views here.


class ListPlan(supra.SupraListView):
    model = models.Plan
    search_key = 'q'
    list_display = ['id','nombre','descripcion','operadores','asistentes','valor','modulos']
    search_fields = ['id']
    paginate_by = 100

    def modulos(self, obj, row):
        return 'Lunes martes'
    # end def

    def get_queryset(self):
        queryset = super(ListConfiguracion, self).get_queryset()
        user = CuserMiddleware.get_user()
        confi = queryset.filter(estado=True)
        return confi

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(ListPlan, self).dispatch(*args, **kwargs)
    # end def
# end class
