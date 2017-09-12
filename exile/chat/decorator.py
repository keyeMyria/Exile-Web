from django.http import HttpResponse
import json as simplejson
from supra import views as supra
from exile.settings import ORIGIN
from django.db.models import Q
from subcripcion.models import Cuenta
from cuser.middleware import CuserMiddleware

# Create your views here.
supra.SupraConf.ACCECC_CONTROL["allow"] = True
supra.SupraConf.ACCECC_CONTROL["origin"] = ORIGIN
supra.SupraConf.ACCECC_CONTROL["credentials"] = "true"
supra.SupraConf.ACCECC_CONTROL["headers"] = "origin, content-type, accept"
supra.SupraConf.ACCECC_CONTROL["methods"] = "POST, GET, PUT, DELETE ,OPTIONS"


def check_login(funcion):
    @supra.access_control
    def check(request, *args, **kwargs):
        if request.user.is_authenticated() or request.method == "OPTIONS":
            return funcion(request, *args, **kwargs)
            # end if
        return HttpResponse(simplejson.dumps({"error": "Debes iniciar sesion"}), 403)
    # end def
    return check
# end def

def get_cuenta(funcion):
    def _cuenta(*args, **kwargs):
        user = CuserMiddleware.get_user()
        cuenta = Cuenta.objects.filter(
            Q(cliente=user.pk) | Q(asistente=user.pk) | Q(empleado=user.pk)).first()
        return funcion(cuenta, *args, **kwargs)
        # end if
    return _cuenta
# end def
