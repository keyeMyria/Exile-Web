from django.conf.urls import include, url
import views

"""
    Tipo de indentificacion
"""

urlpatterns = [
    url(r'^tipo/form/$', views.TipoSupraForm.as_view(), name="tipo"),
    url(r'^tipo/list/$', views.TipoList.as_view(), name="tipo_list"),
    url(r'^tipo/form/(?P<pk>\d+)/$', views.TipoSupraForm.as_view(), name="tipo_edit"),
    url(r'^tipo/delete/(?P<pk>\d+)/$', views.TipoDeleteSupra.as_view(), name="tipo_delete"),
]


"""
    Mis clientes
"""

urlpatterns += [
    url(r'^cliente/form/$', views.ClienteSupraForm.as_view(), name="cliente"),
    url(r'^cliente/list/$', views.ClienteList.as_view(), name="cliente_list"),
    url(r'^cliente/form/(?P<pk>\d+)/$', views.ClienteSupraForm.as_view(), name="cliente_edit"),
    url(r'^cliente/delete/(?P<pk>\d+)/$', views.ClienteDeleteSupra.as_view(), name="cliente_delete"),
]


"""
    Lugares
"""


urlpatterns += [
    url(r'^lugar/form/$', views.LugarSupraForm.as_view(), name="lugar"),
    url(r'^lugar/list/$', views.LugarList.as_view(), name="lugar_list"),
    url(r'^lugar/form/(?P<pk>\d+)/$', views.LugarSupraForm.as_view(), name="lugar_edit"),
    url(r'^lugar/delete/(?P<pk>\d+)/$', views.LugarDeleteSupra.as_view(), name="lugar_delete"),
]


"""
    Tareas
"""

urlpatterns += [
    url(r'^tarea/form/$', views.TareaSupraForm.as_view(), name="tarea"),
    url(r'^tarea/list/$', views.TareaList.as_view(), name="tarea_list"),
    url(r'^tareas/periodicas/list/$', views.TareasPeriodicasList.as_view(), name="tareas_periodicas_list"),
    url(r'^notificacion/list/$', views.NotificacionList.as_view(), name="notificacion_list"),
    url(r'^tarea/form/(?P<pk>\d+)/$', views.TareaSupraForm.as_view(), name="tarea_edit"),
    url(r'^tarea/delete/(?P<pk>\d+)/$', views.TareaDeleteSupra.as_view(), name="tarea_delete"),
    url(r'^completado/form/$', views.CompletadoForm.as_view(), name="completado_add"),
    url(r'^completado/delete/(?P<pk>\d+)/$', views.CompletadoDelete.as_view(), name="completado_delete"),
]

"""
    SubTareas
"""

urlpatterns += [
    url(r'^sub/tarea/form/$', views.SubTareaSupraForm.as_view(), name="sub_tarea"),
    url(r'^sub/tarea/form/(?P<pk>\d+)/$', views.SubTareaSupraForm.as_view(), name="sub_tarea_edit"),
    url(r'^sub/tarea/delete/(?P<pk>\d+)/$', views.SubTareaDeleteSupra.as_view(), name="sub_tarea_delete"),
    url(r'^sub/completado/form/$', views.CompletadoSubForm.as_view(), name="subcompletado_delete"),
    url(r'^sub/completado/delete/(?P<pk>\d+)/$', views.CompletadoSubDelete.as_view(), name="subcompletado_delete"),
]

"""
    Multimedia
"""


urlpatterns += [
    url(r'^multimedia/form/$', views.MultimediaSupraForm.as_view(), name="multimedia"),
    url(r'^multimedia/list/$', views.MultimediaList.as_view(), name="multimedia_list"),
    url(r'^multimedia/form/(?P<pk>\d+)/$', views.MultimediaSupraForm.as_view(), name="multimedia_edit"),
    url(r'^multimedia/delete/(?P<pk>\d+)/$', views.MultimediaDeleteSupra.as_view(), name="multimedia_delete"),
]



"""
    CronTab & Interval
"""

urlpatterns += [
    url(r'^crontab/form/$', views.CrontabScheduleSupraForm.as_view(), name="crontab"),
    url(r'^crontab/form/(?P<pk>\d+)/$', views.CrontabScheduleSupraForm.as_view(), name="crontab_edit"),
    url(r'^crontab/delete/(?P<pk>\d+)/$', views.IntervalScheduleDeleteSupra.as_view(), name="crontab_delete"),

    url(r'^interval/form/$', views.IntervalScheduleSupraForm.as_view(), name="interval"),
    url(r'^interval/form/(?P<pk>\d+)/$', views.IntervalScheduleSupraForm.as_view(), name="interval_edit"),
    url(r'^interval/delete/(?P<pk>\d+)/$', views.CrontabScheduleDeleteSupra.as_view(), name="interval_delete"),
]


