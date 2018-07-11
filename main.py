from BD import DB
from cliente import Cliente
from productos import Producto
from empleados import Empleado
from empresa import Empresa


DB().setconnection("localhost", "root", "alumno", "mydb")
unaEmpresa = Empresa()
unaEmpresa.idEmpresa = 1
unaEmpresa.modificarEmpresa('Coca-Cola')