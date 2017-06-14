# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from subcripcion.models import Cuenta
from django.db.models import Q

# Create your views here.


def index(request):
    cuenta = Cuenta.objects.filter(Q(cliente=request.user.pk) | Q(asistente=request.user.pk) | Q(empleado=request.user.pk)).first()
    return render(request, 'index.html', {"cuenta": cuenta})
# end def
