from BD import DB

class Cliente(object):
    idCliente = None
    nombreCliente = None
    apellidoCliente = None
    fechaNac = None
    Empresa = None

    def altaCliente(self):
        DB().run("INSERT INTO Cliente( idCliente, Nombre_Cliente, Apellido_Cliente, Fecha_Nac, Empresa_idEmpresa) VALUES (" + str(self.idCliente) + ",'" + self.nombreCliente + "','" + self.apellidoCliente + "', '" + self.fechaNac + "', "+str(self.Empresa.idEmpresa) + ");")

    def bajaCliente(self):
        DB().run("DELETE FROM Cliente WHERE idCliente = " + str(self.idCliente) + ";")

    def modificarCliente(self):
        DB().run("UPDATE Cliente SET Nombre_Cliente = '" + self.nombreCliente + "' , Apellido_Cliente = '"+ self.apellidoCliente + "',Fecha_Nac = '" + self.fechaNac + "' WHERE idCliente = " + str(self.idCliente) + ";")


