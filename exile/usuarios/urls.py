from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^login/$', views.Login.as_view(), name="loginU"),
    url(r'^logout/$', views.logoutUsers, name="loginOut"),
    url(r'^is/login/$', views.islogin, name="isLogin"),
    url(r'^asistente/form/$', views.AsistenteSupraForm.as_view(), name="asistente"),
    url(r'^asistente/form/(?P<pk>\d+)/$', views.AsistenteSupraForm.as_view(), name="asistente_edit"),
]
