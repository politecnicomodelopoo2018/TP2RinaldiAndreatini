from productos import Producto
from BD import DB

class Empresa(object):
    idEmpresa = None
    nombre = None

    def __init__(self):
        self.listaProductos = []

    def altaEmpresa(self):
        DB().run("INSERT INTO Empresa( idEmpresa,Nombre_Empresa) VALUES (" + str(
            self.idEmpresa) + ",'" + self.nombre + "');")
    def bajaEmpresa(self):
        DB().run("DELETE FROM Empresa WHERE idEmpresa = " + str(self.idEmpresa) + ";")


    def agregarProducto(self):
        cursor = DB().run("SELECT * FROM Productos;")

        for item in cursor:
            unProducto = Producto(item["idProductos"], item["Nombre_Producto"], item["Precio"], item["Empresa_idEmpresa"])
            self.listaProductos.append(unProducto)

