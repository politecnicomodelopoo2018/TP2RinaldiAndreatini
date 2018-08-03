from BD import DB
from datetime import datetime

class Empleado(object):
    idEmpleado = None
    nombreEmpleado = None
    apellidoEmpleado = None
    fechaNac = None
    fechaIngreso = None
    Empresa = None

    def altaEmpleado(self):
        DB().run("INSERT INTO Empleados( idEmpleados, Nombre_Empleado, Apellido_Empleado, Fecha_Nac, Ingreso_Fecha,  Empresa_idEmpresa) VALUES (" + str(self.idEmpleado) + ",'" + self.nombreEmpleado + "','" + self.apellidoEmpleado + "','" + self.fechaNac + "', '" + self.fechaIngreso + "'," + str(self.Empresa.idEmpresa) +")")

    def bajaEmpleado(self):
        DB().run("DELETE FROM Empleados WHERE idEmpleados = " + str(self.idEmpleado) + ";")

    def modificarEmpleado(self, nuevonombre, nuevoapellido, nuevaFechaNac, nuevaFechaIngreso):
        DB().run("UPDATE Empleados SET Nombre_Empleado = '" + nuevonombre + "' , Apellido_Empleado = "+ nuevoapellido +
                 ",'" + nuevaFechaNac + "','" + nuevaFechaIngreso +" WHERE idEmpleados = " + str(self.idEmpleado) + ";")


