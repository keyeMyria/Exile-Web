from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^login/$', views.LoginU.as_view(), name="loginU"),
    #url(r'^logout/$', views.logoutUser, name="loginU"),
    url(r'^login/empleado/$', views.LoginE.as_view(), name="LoginE"),
    url(r'^is/login/$', views.islogin, name="isLogin"),
]

"""
    Urls asistente
"""

urlpatterns += [
    url(r'^asistente/form/$', views.AsistenteSupraForm.as_view(), name="asistente"),
    url(r'^asistente/list/$', views.AsistenteList.as_view(), name="asistente_list"),
    url(r'^asistente/form/(?P<pk>\d+)/$',
        views.AsistenteSupraForm.as_view(), name="asistente_edit"),
    url(r'^asistente/delete/(?P<pk>\d+)/$',
        views.AsistenteSupraFormDelete.as_view(), name="asistente_delete"),
]


"""
    Urls Cargo
"""

urlpatterns += [
    url(r'^cargo/form/$', views.CargoSupraForm.as_view(), name="cargo"),
    url(r'^cargo/form/(?P<pk>\d+)/$', views.CargoSupraForm.as_view(), name="cargo_edit"),
    url(r'^cargo/list/$', views.CargoList.as_view(), name="cargo_list"),
    url(r'^cargo/delete/(?P<pk>\d+)/$',
        views.CargoDeleteSupra.as_view(), name="cargo_delete"),
]


"""
    Urls empleado
"""

urlpatterns += [
    url(r'^empleado/form/$', views.EmpleadoSupraForm.as_view(), name="empleado"),
    url(r'^empleado/form/(?P<pk>\d+)/$', views.EmpleadoSupraForm.as_view(), name="empleado_edit"),
    url(r'^empleado/list/$', views.EmpleadoList.as_view(), name="empleado_list"),
    url(r'^empleado/delete/(?P<pk>\d+)/$',
        views.EmpleadoSupraFormDelete.as_view(), name="empleado_delete"),
]


"""
    Urls grupo
"""

urlpatterns += [
    url(r'^grupo/form/$', views.GrupoSupraForm.as_view(), name="grupo"),
    url(r'^grupo/form/(?P<pk>\d+)/$', views.GrupoSupraForm.as_view(), name="grupo_edit"),
    url(r'^grupo/list/$', views.GrupoList.as_view(), name="grupo_list"),
    url(r'^grupo/delete/(?P<pk>\d+)/$',
        views.GrupoSupraFormDelete.as_view(), name="grupo_delete"),
]
