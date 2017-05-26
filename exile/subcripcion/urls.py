from django.conf.urls import url
import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

#empleado
urlpatterns = [
    url(r'^login/empleado/$',login_required(views.LoginEmpleado.as_view()) ,name='login_empleado'),
]
