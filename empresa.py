from productos import Producto
from BD import DB

class Empresa(object):
    idEmpresa = None
    nombre = None

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

    def __init__(self):
        self.listaProductos = []

    def altaEmpresa(self):
        DB().run("INSERT INTO Empresa( idEmpresa,Nombre_Empresa) VALUES (" + str(
            self.idEmpresa) + ",'" + self.nombre + "');")
    def bajaEmpresa(self):
        DB().run("DELETE FROM Empresa WHERE idEmpresa = " + str(self.idEmpresa) + ";")

    def modificarEmpresa(self, nuevo):
        DB().run("UPDATE Empresa SET Nombre_Empresa = '" + nuevo + "' WHERE idEmpresa = " + str(self.idEmpresa) + ";")


