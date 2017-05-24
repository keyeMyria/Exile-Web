from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^login/$', views.Login.as_view(), name="loginU"),
    url(r'^logout/$', views.logoutUsers, name="loginOut"),
]
