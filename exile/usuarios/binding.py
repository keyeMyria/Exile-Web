import models
from channels.binding.websockets import WebsocketBinding


class CargoValueBinding(WebsocketBinding):
    model = models.Cargo
    stream = "cargo"
    fields = ["cuenta", 'nombre', 'fecha', ]

    @classmethod
    def group_names(cls, instance):
        return ["noti-%d" % instance.cuenta.id]
    # end def

    def has_permission(self, user, action, pk):
        print "######", user, action, pk
        return True
    # end def
# end class


class EmpleadoValueBinding(WebsocketBinding):
    model = models.Empleado
    stream = "empleado"
    fields = ["cuenta", 'first_name', 'last_name', 'email', 'identificacion', 'fecha_nacimiento', 'direccion', 'telefono', 'fijo', 'imagen', 'cargo', 'fecha_ingreso', 'fecha_retiro']

    @classmethod
    def group_names(cls, instance):
        return ["noti-%d" % instance.cuenta.id]
    # end def

    def has_permission(self, user, action, pk):
        print "######", user, action, pk
        return True
    # end def
# end class


class AsistenteValueBinding(WebsocketBinding):
    model = models.Asistente
    stream = "asistente"
    fields = ["cuenta", 'first_name', 'last_name', 'email', 'identificacion', 'fecha_nacimiento', 'direccion', 'telefono', 'fijo', 'imagen']

    @classmethod
    def group_names(cls, instance):
        return ["noti-%d" % instance.cuenta.id]
    # end def

    def has_permission(self, user, action, pk):
        print "######", user, action, pk
        return True
    # end def
# end class


class GrupoValueBinding(WebsocketBinding):
    model = models.Grupo
    stream = "grupo"
    fields = ["cuenta", 'nombre', 'empleados']

    @classmethod
    def group_names(cls, instance):
        return ["noti-%d" % instance.cuenta.id]
    # end def

    def has_permission(self, user, action, pk):
        print "######", user, action, pk
        return True
    # end def
# end class
