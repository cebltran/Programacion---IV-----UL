import pymongo

from pymongo import MongoClient

MONGO_UBI = 'mongodb://localhost'
engine = MongoClient(MONGO_UBI)
db = engine['inventario']


def numerador():
    secuencia = db['secuencia']
    contador = secuencia.find_one_and_update(filter={'id': 'identity'},
                                             update={'$inc': {'seq': 1}},
                                             upsert=True,
                                             return_document=pymongo.ReturnDocument.AFTER)
    dato = contador["seq"]
    return dato


def Insertadato(palabra, significado):
    palabras = db['articulos']
    palabras.insert_one({'id': numerador(), 'Articulo': palabra, 'Descripción': significado})

    print("")
    print("                                 -->Registro Insertado Con exito")
    print("")
    p = input("Presione una <Enter> para continuar")


def Editadato(palabra, significado, idpalabra):
    palabras = db['articulos']
    palabras.update({'id': idpalabra}, {'id': idpalabra, 'Articulo': palabra, 'Descripción': significado})

    print("                                 --> Registro Actualizado con Exito")
    print("")
    p = input("Presione una <Enter> para continuar")


def Borradato(idpalabra):
    palabras = db['articulos']
    palabras.remove({'id': idpalabra})

    print("                                 --> Registro Eliminado con Exito")
    print("")
    p = input("Presione una <Enter> para continuar")


def BuscaDato(palabra, muestra):
    palabras = db['articulos']
    palabra: eval("/" + palabra + "/i")
    salida = palabras.find({"Articulo": {"$regex": palabra}})


    for dato in salida:
        print(dato['id'], " - " + dato['Articulo'], " - " + dato['Descripción'])

    if muestra == 1:
        print("                                 --> Registros encontrados")
        print("")
        p = input("Presione una <Enter> para continuar")


def CreaBD():
    secuencia = db['secuencia']
    secuencia.drop()
    secuencia.insert_one({'id': 'identity', 'seq': 0})

    coleccion = db['articulos']
    coleccion.drop()
    coleccion.insert_one({'id': numerador(), 'Articulo': 'Laptop Dell Optima', 'Descripción': ' Laptop Optima'})