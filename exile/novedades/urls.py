from django.conf.urls import include, url
import views

"""
    Tipo
"""
urlpatterns = [
    url(r'^tipo/form/$', views.TipoSupraForm.as_view(), name="tipo"),
    url(r'^tipo/list/$', views.TipoList.as_view(), name="tipo_list"),
    url(r'^tipo/form/(?P<pk>\d+)/$',
        views.TipoSupraForm.as_view(), name="tipo_edit"),
    url(r'^tipo/delete/(?P<pk>\d+)/$',
        views.TipoDeleteSupra.as_view(), name="tipo_delete"),
]

"""
    Reporte
"""
urlpatterns += [
    url(r'^reporte/list/$', views.ReporteListView.as_view()),
    url(r'^reporte/form/$', views.ReporteForm.as_view()),
    url(r'^reporte/form/(?P<pk>\d+)/$', views.ReporteForm.as_view()),
    url(r'^reporte/delete/(?P<pk>\d+)/$',
        views.ReporteDeleteSupra.as_view(), name="reporte_delete"),
]


"""
    Fotos Reporte
"""
urlpatterns += [
    url(r'^foto/form/$', views.FotoReporteForm.as_view()),
    url(r'^foto/list/$', views.FotoReporteListView.as_view()),
    url(r'^foto/delete/(?P<pk>\d+)/$',
        views.FotoDeleteSupra.as_view(), name="foto_delete"),
    url(r'^foto/delete/list/$', views.FotoListDelete, name="foto_delete_list"),
]
