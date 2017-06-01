from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^login/$', views.LoginU.as_view(), name="loginU"),
    url(r'^logout/$', views.logoutUsers, name="loginOut"),
    url(r'^is/login/$', views.islogin, name="isLogin"),
    url(r'^asistente/form/$', views.AsistenteSupraForm.as_view(), name="asistente"),
    url(r'^asistente/list/$', views.AsistenteList.as_view(), name="asistente_list"),
    url(r'^asistente/form/(?P<pk>\d+)/$', views.AsistenteSupraForm.as_view(), name="asistente_edit"),
    url(r'^asistente/delete/(?P<pk>\d+)/$', views.AsistenteSupraFormDelete.as_view(), name="asistente_delete"),
]
