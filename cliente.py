class Cliente(object):
    idCliente = None
    nombreCliente = None
    apellidoCliente = None
    fechaNac = None

    def __init__(self, nombre, apellido, fechaNac, id):
        self.idCliente = id
        self.nombre = nombre
        self.apellido = apellido
        self.fechaNac = fechaNac