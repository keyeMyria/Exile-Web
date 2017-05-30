from django.conf.urls import url
import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

#empleado
urlpatterns = [
    url(r'^login/empleado/$',login_required(views.LoginEmpleado.as_view()) ,name='login_empleado'),
]

#lista de planes
urlpatterns += [
    url(r'get/planes/$',login_required(views.ListPlan.as_view()), name='list_planes'),
]
