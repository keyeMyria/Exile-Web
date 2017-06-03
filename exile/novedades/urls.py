from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^tiporeporte/list/$', views.TipoReporteListView.as_view()),
    url(r'^tiporeporte/form/$', views.TipoSupraForm.as_view()),
    url(r'^reporte/list/$', views.ReporteListView.as_view()),
    url(r'^foto/form/$', views.FotoReporteForm.as_view()),
    url(r'^reporte/form/$', views.ReporteForm.as_view()),
    url(r'^reporte/form/(?P<pk>\d+)/$', views.ReporteForm.as_view()),
]
