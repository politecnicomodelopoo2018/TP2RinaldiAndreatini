from productos import Producto
from empleados import Empleado
from datetime import datetime
from BD import DB

class Empresa(object):
    idEmpresa = None
    nombre = None

    def altaEmpresa(self):
        DB().run("INSERT INTO Empresa( idEmpresa,Nombre_Empresa) VALUES (" + str(
            self.idEmpresa) + ",'" + self.nombre + "');")
    def bajaEmpresa(self):
        DB().run("DELETE FROM Productos WHERE Empresa_idEmpresa = " + str(self.idEmpresa) + ";")
        DB().run("DELETE FROM Empleados WHERE Empresa_idEmpresa = " + str(self.idEmpresa) + ";")
        DB().run("DELETE FROM Cliente WHERE Empresa_idEmpresa = " + str(self.idEmpresa) + ";")
        DB().run("DELETE FROM Empresa WHERE idEmpresa = " + str(self.idEmpresa) + ";")

    def modificarEmpresa(self):
        DB().run("UPDATE Empresa SET Nombre_Empresa = '" + self.nombre + "' WHERE idEmpresa = " + str(self.idEmpresa) + ";")

    @staticmethod
    def getEmpresas():
        listaEmpresas = []

        cursor = DB().run('SELECT * FROM Empresa;')
        for item in cursor:
            unaEmpresa = Empresa()
            unaEmpresa.idEmpresa = item['idEmpresa']
            unaEmpresa.nombre = item['Nombre_Empresa']
            listaEmpresas.append(unaEmpresa)

        return listaEmpresas

    @staticmethod
    def getProductos():

        listaProductos = []

        cursor = DB().run('SELECT * FROM Productos;')
        for item in cursor:
            unProducto = Producto()
            unProducto.idProducto = item['idProductos']
            unProducto.nombreProducto = item['Nombre_Producto']
            unProducto.precio = item['Precio']

            for item2 in Empresa.getEmpresas():
                if item2.idEmpresa == item['Empresa_idEmpresa']:
                    unProducto.Empresa = item2

            listaProductos.append(unProducto)

        return listaProductos

    @staticmethod
    def getEmpleados():
        listaEmpleados = []

        cursor = DB().run('SELECT * FROM Empleados;')
        for item in cursor:
            unEmpleado = Empleado()
            unEmpleado.idEmpleado = item['idEmpleados']
            unEmpleado.nombreEmpleado = item['Nombre_Empleado']
            unEmpleado.apellidoEmpleado = item['Apellido_Empleado']
            unEmpleado.fechaNac = item['Fecha_Nac']
            unEmpleado.fechaIngreso = item['Ingreso_Fecha']

            for item2 in Empresa.getEmpresas():
                if item2.idEmpresa == item['Empresa_idEmpresa']:
                    unEmpleado.Empresa = item2

            listaEmpleados.append(unEmpleado)

        return listaEmpleados

