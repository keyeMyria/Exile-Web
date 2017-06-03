from django.http import HttpResponse
import json as simplejson
from http import response


def check_login(funcion):
    def check(request, *args, **kwargs):
        if request.user.is_authenticated():
            return funcion(request, *args, **kwargs)
            # end if
        return response(simplejson.dumps({"error": "Debes iniciar sesion"}), 403)
    # end def
    return check
# end def
