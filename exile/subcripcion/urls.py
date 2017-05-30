from django.conf.urls import url
import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

#empleado
urlpatterns = [
    url(r'^login/empleado/$',login_required(views.LoginEmpleado.as_view()) ,name='login_empleado'),
]

#servicios de planes
urlpatterns += [
    url(r'get/planes/$',login_required(views.ListPlan.as_view()), name='list_planes'),
    url(r'add/plan/$',login_required(views.AddPlan.as_view()), name='add_plan'),
    url(r'edit/plan/(?P<pk>\d+)/$',login_required(views.AddPlan.as_view()), name='edit_plan'),
    url(r'delete/plan/(?P<pk>\d+)/$',login_required(views.AddPlan.as_view()), name='delete_plan'),
]

#servicios de instancias de modulos
urlpatterns += [
    url(r'get/planes/$',login_required(views.ListPlan.as_view()), name='list_planes'),
    url(r'add/plan/$',login_required(views.AddPlan.as_view()), name='add_plan'),
    url(r'edit/plan/(?P<pk>\d+)/$',login_required(views.AddPlan.as_view()), name='edit_plan'),
    url(r'delete/plan/(?P<pk>\d+)/$',login_required(views.AddPlan.as_view()), name='delete_plan'),
]
