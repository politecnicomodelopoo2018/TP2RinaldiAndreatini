from productos import  Producto
from cliente import Cliente
from BD import  DB

class Compras(object):
    Cliente = None
    Producto = None
    Cantidad = None
    Pago = None

    def altaCompra(self):
        DB().run("INSERT INTO Compras(ClienteIdCliente, ProductosIdProductos, Cantidad, Pago) VALUES (" + str(self.Cliente.idCliente) + ", " + str(self.Producto.idProducto) + ", " + str(self.Cantidad) + ", '" + self.Pago + "');")

    def bajaCompra(self):
        DB().run("DELETE FROM Compras WHERE  ClienteIdCliente = " + str(self.Cliente.idCliente) +";")

    def modificarCompra(self):
        DB().run("UPDATE Compras SET Cantidad = '" + str(self.Cantidad) + "' , Modo_de_pago = " + str(
            self.Pago) + " WHERE ClienteIdCliente = " + str(self.Cliente.idCliente) + "AND ProductosIdProductos = " + str(self.Producto.idProducto) + ";")