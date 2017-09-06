from channels import include

channel_routing = [
    include("usuarios.routing.websocket_routing", path=r"^/noti/(?P<pk>\d+)/"),
    #route_class(UsuariosDemultiplexerBiding, path="^/binding/usuarios/(?P<pk>\d+)/"),
    #route_class(NovedadesDemultiplexerBiding, path="^/binding/novedades/(?P<pk>\d+)/"),
    #route_class(OperacionDemultiplexerBiding, path="^/binding/operacion/(?P<pk>\d+)/"),
    include("chat.routing.websocket_routing", path=r"^/chat/stream"),
    include("chat.routing.custom_routing"),
]
