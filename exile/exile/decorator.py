from django.http import HttpResponse
import json as simplejson
from supra import views as supra
from exile.settings import ORIGIN

# Create your views here.
supra.SupraConf.ACCECC_CONTROL["allow"] = True
supra.SupraConf.ACCECC_CONTROL["origin"] = ORIGIN
supra.SupraConf.ACCECC_CONTROL["credentials"] = "true"
supra.SupraConf.ACCECC_CONTROL["headers"] = "origin, content-type, accept"
supra.SupraConf.ACCECC_CONTROL["methods"] = "POST, GET, PUT, DELETE ,OPTIONS"


@supra.access_control
def check_login(funcion):
    def check(request, *args, **kwargs):
        if request.user.is_authenticated():
            return funcion(request, *args, **kwargs)
            # end if
        return HttpResponse(simplejson.dumps({"error": "Debes iniciar sesion"}), 403)
    # end def
    return check
# end def
