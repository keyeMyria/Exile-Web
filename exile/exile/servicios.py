# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import Q
from subcripcion.models import Cuenta
from cuser.middleware import CuserMiddleware


def get_cuenta():
    user = CuserMiddleware.get_user()
    if user:
        cuenta = Cuenta.objects.filter(
            Q(cliente=user.pk) | Q(usuario=user.pk)).first()
        return cuenta
    # end if
    return None
# end def
