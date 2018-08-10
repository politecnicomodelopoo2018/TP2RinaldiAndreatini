from BD import DB
from cliente import Cliente
from productos import Producto
from empleados import Empleado
from empresa import Empresa


def getCliente():
    listaClientes = []

    cursor = DB().run('SELECT * FROM Cliente;')
    for item in cursor:
        unCliente = Cliente()
        unCliente.idCliente = item['idCliente']
        unCliente.nombreCliente = item['Nombre_Cliente']
        unCliente.apellidoCliente = item['Apellido_Cliente']
        unCliente.fechaNac = item['Fecha_Nac']

        listaClientes.append(unCliente)

    return listaClientes



DB().setconnection("localhost", "root", "alumno", "mydb")

opcion = 0
while opcion is not 16:

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
    print('13.Alta Compra')
    print('14.Baja Compra')
    print('15.Modificar Compra')
    print('16. Salir')

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
                item.nombre = nuevoNombre
                item.modificarEmpresa()
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

        opcionMod = 0

        for item in Empresa.getProductos():
            while opcionMod is not 3:
                if item.idProducto == idaModificar and item.Empresa.idEmpresa == opcionEmpresa:
                    print('1.Nombre')
                    print('2.Precio')
                    print('3.Salir')
                    opcionMod = int(input('Que desea modificar? '))

                if opcionMod == 1:
                    nuevonombre = input('Ingrese nuevo Nombre: ')
                    item.nombreProducto = nuevonombre
                    item.modificarProducto()

                if opcionMod == 2:
                    nuevoprecio = input('Ingrese nuevo precio: ')
                    item.precio = nuevoprecio
                    item.modificarProducto()

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

    if opcion == 8:

        for item in Empresa.getEmpresas():
            print(str(item.idEmpresa) + ' ' + item.nombre)
        opcionEmpresa = int(input('De que empresa elimino el empleado: '))
        for item in Empresa.getEmpleados():
            print(str(item.idEmpleado) + ' ' + item.nombreEmpleado)
        idaEliminar = int(input('Ingrese que id de Empleado a eliminar: '))
        for item in Empresa.getEmpleados():
            if item.idEmpleado == idaEliminar and item.Empresa.idEmpresa == opcionEmpresa:
                item.bajaEmpleado()
                print('Se ha eliminado el empleado de la Empresa')

    if opcion == 9:
        for item in Empresa.getEmpresas():
            print(str(item.idEmpresa) + ' ' + item.nombre)
        opcionEmpresa = int(input('De que empresa modifico el Empleado: '))
        for item in Empresa.getEmpleados():
            print(str(item.idEmpleado) + ' ' + item.nombreEmpleado)
        idaModificar = int(input('Ingrese que id de Empleado a modificar: '))


        for item in Empresa.getEmpleados():
                opcionMod = 0
                while opcionMod is not 5:
                    if item.idEmpleado == idaModificar and item.Empresa.idEmpresa == opcionEmpresa:
                        print('1.Nombre')
                        print('2.Apellido')
                        print('3.Fecha de Nacimiento')
                        print('4.Fecha de Ingreso')
                        print('5.Salir')
                        opcionMod = int(input('Que desea modificar? '))

                    if opcionMod == 1:
                        nuevonombre = input('Ingrese nuevo Nombre: ')
                        item.nombreEmpleado = nuevonombre
                        item.modificarEmpleado()

                    if opcionMod == 2:
                        nuevoapellido = input('Ingrese nuevo apellido: ')
                        item.apellidoEmpleado = nuevoapellido
                        item.modificarEmpleado()

                    if opcionMod == 3:
                        nuevaFechaNac = input('Ingrese nueva Fecha de Nacimiento: ')
                        item.fechaNac = nuevaFechaNac
                        item.modificarEmpleado()

                    if opcionMod == 4:
                        nuevaFechaIng = input('Ingrese nueva Fecha de Ingreso: ')
                        item.fechaIngreso = nuevaFechaIng
                        item.modificarEmpleado()
    if opcion == 10:
        unCliente = Cliente()
        idCliente = input('Ingrese id del Cliente: ')
        unCliente.idCliente = idCliente
        nombreCliente = input('Ingrese nombre del Cliente: ')
        unCliente.nombreCliente = nombreCliente
        apellido = input('Ingrese apellido del Cliente: ')
        unCliente.apellidoCliente = apellido
        fechaNac = input('Ingrese fecha de nacimiento: ')
        unCliente.fechaNac = fechaNac

        unCliente.altaCliente()

    if opcion == 11:
        for item in getCliente():
            print(str(item.idCliente) + ' ' + item.nombreCliente)
        idAEliminar = int(input('Que Cliente desea eliminar? '))
        for item in getCliente():
            if item.idCliente == idAEliminar:
                item.bajaCliente()
                print('Se a eliminado el cliente.')

    if opcion == 12:
        for item in getCliente():
            print(str(item.idCliente) + ' ' + item.nombreCliente)
        idaModificar = int(input('Ingrese que id de cliente a modificar: '))


        for item in getCliente():
                opcionMod = 0
                while opcionMod is not 4:
                    if item.idCliente == idaModificar:
                        print('1.Nombre')
                        print('2.Apellido')
                        print('3.Fecha de Nacimiento')
                        print('4.Salir')
                        opcionMod = int(input('Que desea modificar? '))

                    if opcionMod == 1:
                        nuevonombre = input('Ingrese nuevo Nombre: ')
                        item.nombreCliente = nuevonombre
                        item.modificarCliente()

                    if opcionMod == 2:
                        nuevoapellido = input('Ingrese nuevo apellido: ')
                        item.apellidoCliente = nuevoapellido
                        item.modificarCliente()

                    if opcionMod == 3:
                        nuevaFechaNac = input('Ingrese nueva Fecha de Nacimiento: ')
                        item.fechaNac = nuevaFechaNac
                        item.modificarCliente()

    if opcion == 13:
