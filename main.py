from BD import DB
from cliente import Cliente
from productos import Producto
from empleados import Empleado
from empresa import Empresa

DB().setconnection("localhost", "root", "alumno", "mydb")

opcion = 0
while opcion is not '7':

    print('1.Alta Empresa')
    print('2.Baja Empresa')
    print('3.Modificar Empresa')
    print('4.Alta Producto')
    print('5.Baja Producto')
    print('6.Modificcar Producto')
    opcion = int(input('Ingrese opcion: '))

    if opcion == 1:
        unaEmpresa = Empresa()
        idEmpresa = input('Ingrese id empresa: ')
        unaEmpresa.idEmpresa = idEmpresa
        nombreEmpresa = input('Ingrese Nombre Empresa: ')
        unaEmpresa.nombre = nombreEmpresa
        unaEmpresa.altaEmpresa()

    if opcion == 2:
        for item in Empresa.getEmpresas():
            print(str(item.idEmpresa) + ' ' + item.nombre)
        idAEliminar = int(input('Ingrese que id de Empresa elimina: '))
        for item in Empresa.getEmpresas():
            if item.idEmpresa == idAEliminar:
                item.bajaEmpresa()
                print('Se ha eliminado la Empresa')

    if opcion == 3:
        for item in Empresa.getEmpresas():
            print(str(item.idEmpresa) + ' ' + item.nombre)
        idAModificar = int(input('Ingrese que id de Empresa modifica: '))
        for item in Empresa.getEmpresas():
            if item.idEmpresa == idAModificar:
                nuevoNombre = input('Ingrese nuevo nombre para la Empresa: ')
                item.modificarEmpresa(nuevoNombre)
                print('Se ha modificado el nombre de la Empresa')

    if opcion == 4:
        opcionEmpresa = input('A que empresa agrega el producto: ')
        unProducto = Producto()
        idProducto = input('Ingrese id del Producto: ')
        unProducto.idProducto = idProducto
        nombreProducto = input('Ingrese nombre del Producto: ')
        unProducto.nombreProducto = nombreProducto
        precioProducto = input('Ingrese precio del producto: ')
        unProducto.precio = precioProducto
        opcionEmpresa = input('A que empresa agrega el producto: ')

        for item in Empresa.getEmpresas():
            if item.idEmpresa == opcionEmpresa:
                unProducto.Empresa = item

        unProducto.altaProducto()

    if opcion == 5:


    if opcion == 6: