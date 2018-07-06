class Empleado(object):
    idEmpleado = None
    nombreEmpleado = None
    apellidoEmpleado = None
    fechaNac = None
    fechaIngreso = None

    def __init__(self, id, nombre, apellido, fechaN, fechaI):
        self.idEmpleado = id
        self.nombreEmpleado = nombre
        self.apellidoEmpleado = apellido
        self.fechaNac = fechaN
        self.fechaIngreso = fechaI