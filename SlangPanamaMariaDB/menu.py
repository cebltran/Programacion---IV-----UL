import BD
opcion = -1
def menu():
    print("***********LANG PANAMEÑO***********")
    print("1- Crear BD (Reinicia datos)")
    print("2- Agregar palabra")
    print("3- Editar palabra")
    print("4- Borrar Palabra")
    print("5- Buscar Palabra")
    print("-----------------------------------")
    print("0- Salir")
    print("-----------------------------------")

while opcion != 0:
    menu()
    opcion = int(input("Ingrese opcion del menun (0-5): "))
    if opcion == 1:
        base = BD
        base.CreaBD()
    elif opcion == 2:
        base = BD
        palabra = input("Palabra: ")
        significado = input("Significado: ")
        base.Insertadato(palabra.upper(), significado.upper())
    elif opcion == 3:
        print("3- Editar palabra")
        base = BD
        palabra = input("loa palabra que busca contiene: ")
        base.BuscaDato(palabra.upper(), 0)
        idpalabra = int(input("De la lista desplegada elija el numero para modificar: "))
        palabra = input("Palabra: ")
        significado = input("Significado: ")
        base.Editadato(palabra.upper(), significado.upper(), idpalabra)

    elif opcion == 4:
        base = BD
        palabra = input("loa palabra que busca contiene: ")
        base.BuscaDato(palabra.upper(), 0)
        idpalabra = int(input("De la lista desplegada elija el numero para borrarla: "))
        base.Borradato(idpalabra)


    elif opcion == 5:
        base = BD
        palabra = input("lo que busca contiene: ")
        base.BuscaDato(palabra.upper(), 1)
