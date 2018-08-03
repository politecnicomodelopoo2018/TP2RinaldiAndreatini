from BD import DB
from cliente import Cliente
from productos import Producto
from empleados import Empleado
from empresa import Empresa

DB().setconnection("localhost", "root", "alumno", "mydb")

opcion = 0
while opcion is not 13:

    print('1.Alta Empresa')
    print('2.Baja Empresa')
    print('3.Modificar Empresa')
    print('4.Alta Producto')
    print('5.Baja Producto')
    print('6.Modificcar Producto')
    print('7.Alta Empleado')
    print('8.Baja Empleado')
    print('9.Modificar Empleado')
    print('10.Alta Cliente')
    print('11.Baja Cliente')
    print('12.Modificar Cliente')
    print('13. Salir')

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
        for item in Empresa.getEmpresas():
            print(str(item.idEmpresa) + ' ' + item.nombre)
        opcionEmpresa = int(input('A que empresa agrega el producto: '))

        unProducto = Producto()
        idProducto = input('Ingrese id del Producto: ')
        unProducto.idProducto = idProducto
        nombreProducto = input('Ingrese nombre del Producto: ')
        unProducto.nombreProducto = nombreProducto
        precioProducto = input('Ingrese precio del producto: ')
        unProducto.precio = precioProducto

        for item in Empresa.getEmpresas():
            if item.idEmpresa == opcionEmpresa:
                unProducto.Empresa = item

        unProducto.altaProducto()

    if opcion == 5:
        for item in Empresa.getEmpresas():
            print(str(item.idEmpresa) + ' ' + item.nombre)
        opcionEmpresa = int(input('De que empresa elimino el producto: '))
        for item in Empresa.getProductos():
            print(str(item.idProducto) + ' ' + item.nombreProducto)
        idaEliminar = int(input('Ingrese que id de Producto eliminar: '))

        for item in Empresa.getProductos():
            if item.idProducto == idaEliminar and item.Empresa.idEmpresa == opcionEmpresa:
                item.bajaProducto()
                print('Se ha eliminado el producto de la Empresa')

    if opcion == 6:
        for item in Empresa.getEmpresas():
            print(str(item.idEmpresa) + ' ' + item.nombre)
        opcionEmpresa = int(input('De que empresa modifico el producto: '))
        for item in Empresa.getProductos():
            print(str(item.idProducto) + ' ' + item.nombreProducto)
        idaModificar = int(input('Ingrese que id de Producto modificar: '))


        for item in Empresa.getProductos():

            if item.idProducto == idaModificar and item.Empresa.idEmpresa == opcionEmpresa:
                opcion = input('Quiere modificar el nombre?')

                if opcion == 's':
                    nuevonombre = input('Ingrese nuevo nombre: ')
                    opcion2 = input('Quiere modificar el precio?')
                    if opcion2 == 's':
                        nuevoprecio = input('Ingrese nuevo precio: ')
                        item.modificarProducto(nuevonombre, nuevoprecio)
                    if opcion2 == 'n':
                        item.modificarProducto(nuevonombre, item.precio)

                if opcion == 'n':
                    opcion2 = input('Quiere modificar el precio?')
                    if opcion2 == 's':
                        nuevoprecio = input('Ingrese nuevo precio: ')
                        item.modificarProducto(item.nombreProducto, nuevoprecio)
                    if opcion2 == 'n':
                        item.modificarProducto(item.nombreProducto, item.precio)

    if opcion == 7:
        for item in Empresa.getEmpresas():
            print(str(item.idEmpresa) + ' ' + item.nombre)
        opcionEmpresa = int(input('A que empresa agrega el empleado: '))

        unEmpleado = Empleado()
        idEmpleado = input('Ingrese id del Empleado: ')
        unEmpleado.idEmpleado = idEmpleado
        nombreEmpleado = input('Ingrese nombre del Empleado: ')
        unEmpleado.nombreEmpleado = nombreEmpleado
        apellido = input('Ingrese apellido del Empleado: ')
        unEmpleado.apellidoEmpleado = apellido
        fechaNac = input('Ingrese fecha de nacimiento: ')
        unEmpleado.fechaNac = fechaNac
        fechaIngreso = input('Ingrese fecha de ingreso: ')
        unEmpleado.fechaIngreso = fechaIngreso

        for item in Empresa.getEmpresas():
            if item.idEmpresa == opcionEmpresa:
                unEmpleado.Empresa = item

        unEmpleado.altaEmpleado()


