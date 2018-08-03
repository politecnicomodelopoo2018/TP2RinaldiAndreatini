import pymysql
from BD import DB


class Producto(object):
    idProducto = None
    nombreProducto = None
    precio = None
    Empresa = None

    def altaProducto(self):
        DB().run("INSERT INTO Productos( idProducto,Nombre_Producto,Precio, Empresa_idEmpresa) VALUES (" + str(
            self.idProducto) + ",'" + self.nombreProducto + "'," + str(self.precio) + "," + str(
            self.Empresa.idEmpresa) + ")")

    def bajaProducto(self):
        DB().run("DELETE FROM Productos WHERE idProducto = " + str(self.idProducto) + ";")

    def modificarProducto(self, nuevonombre, nuevoprecio):
        DB().run("UPDATE Productos SET Nombre_Producto = '" + nuevonombre + "' , Precio = "+ str(nuevoprecio) + " WHERE idProducto = " + str(self.idProducto) + ";")


