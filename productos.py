import pymysql
from BD import DB


class Producto(object):
    idProducto = None
    nombreProducto = None
    precio = None
    Empresa = None

    def __init__(self, id, nombre, precio, unaEmp):
        self.idProducto = id
        self.nombreProducto = nombre
        self.precio = precio
        self.Empresa = unaEmp

    def insertar(self):
        db = pymysql.connect(host= 'localhost' , user= 'root', passwd= 'alumno', db= 'mydb')

        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("INSERT INTO Productos(idProductos,Nombre_Producto,Precio) VALUES ("+ str(self.idProducto) + ",'" + self.nombreProducto + "'," + str(self.precio) + "'," + str(self.Empresa.idEmpresa) + ")")