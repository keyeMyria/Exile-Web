from channels.routing import route, route_class
from usuarios.consumers import Demultiplexer, UsuariosDemultiplexerBiding
from operacion.consumers import OperacionDemultiplexerBiding
from novedades.consumers import NovedadesDemultiplexerBiding

channel_routing = [
    route_class(Demultiplexer, path="^/noti/(?P<pk>\d+)/"),
    route_class(UsuariosDemultiplexerBiding, path="^/binding/usuarios/(?P<pk>\d+)/"),
    route_class(NovedadesDemultiplexerBiding, path="^/binding/novedades/(?P<pk>\d+)/"),
    route_class(OperacionDemultiplexerBiding, path="^/binding/operacion/(?P<pk>\d+)/")
]
