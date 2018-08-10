from productos import  Producto
from cliente import Cliente
from BD import  DB

class Compras(object):
    Cliente = None
    Producto = None
    Cantidad = None
    Pago = None

    def altaCompra(self):
        DB().run("INSERT INTO Productos( Cliente_idCliente, Productos_idProductos, Cantidad, Modo_de_pago) VALUES (" + str(self.Cliente.idCliente) + ", " + str(self.Producto.idProducto) + ", " + str(self.Cantidad) + ",'" + self.Pago + "');")

    def bajaCompra(self):
        DB().run("DELETE FROM Compras WHERE  Cliente_idCliente= " + str(self.Cliente.idCliente) + "AND Productos_idProductos = " + str(self.Producto.idProducto) + ";")

    def modificarCompra(self):
        DB().run("UPDATE Compras SET Cantidad = '" + str(self.Cantidad) + "' , Modo_de_pago = " + str(
            self.Pago) + " WHERE Cliente_idCliente = " + str(self.Cliente.idCliente) + "AND Productos_idProductos = " + str(self.Producto.idProducto) + ";")