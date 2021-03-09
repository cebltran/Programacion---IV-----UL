import DB
opcion = -1
def menu():
    print("***********PARCIAL NRO 1***********")
    print("1- Crear BD (Reinicia datos)")
    print("2- Agregar articulo")
    print("3- Editar articulo")
    print("4- Borrar articulo")
    print("5- Buscar articulo")
    print("-----------------------------------")
    print("0- Salir")
    print("-----------------------------------")

while opcion != 0:
    menu()
    opcion = int(input("Ingrese opcion del menun (0-5): "))
    if opcion == 1:
        base = DB
        base.CreaBD()
    elif opcion == 2:
        base = DB
        palabra = input("Articulo: ")
        significado = input("Descripción: ")
        base.Insertadato(palabra.upper(), significado.upper())
    elif opcion == 3:
        base = DB
        palabra = input("Necesitamos ubicar el articulo, escriba el nombre o parte del nombre para ubicarlo: ")
        base.BuscaDato(palabra.upper(), 0)
        idpalabra = int(input("De la lista desplegada elija el numero para modificar: "))
        palabra = input("Articulo: ")
        significado = input("Descripción: ")
        base.Editadato(palabra.upper(), significado.upper(), idpalabra)

    elif opcion == 4:
        base = DB
        palabra = input("Necesitamos ubicar el articulo, escriba el nombre o parte del nombre para ubicarlo: ")
        base.BuscaDato(palabra.upper(), 0)
        idpalabra = int(input("De la lista desplegada elija el numero para borrarla: "))
        base.Borradato(idpalabra)


    elif opcion == 5:
        base = DB
        palabra = input("Escriba el nombre o parte del nombre para ubicarlo:: ")
        base.BuscaDato(palabra.upper(), 1)
