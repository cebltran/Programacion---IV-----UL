import pymongo

from pymongo import MongoClient

MONGO_UBI = 'mongodb://localhost'
engine = MongoClient(MONGO_UBI)
db = engine['citas']


def numerador():
    secuencia = db['secuencia']
    contador = secuencia.find_one_and_update(filter={'id': 'identity'},
                                             update={'$inc': {'seq': 1}},
                                             upsert=True,
                                             return_document=pymongo.ReturnDocument.AFTER)
    dato = contador["seq"]
    return dato


def Insertadato(documento, nombre, correo, telefono, fecha, hora):
    palabras = db['citas']
    palabras.insert_one({'id': numerador(), 'DOCUMENTO' : documento, 'NOMBRE' : nombre, 'CORREO' : correo, 'TELEFONO' : telefono, 'FECHA' : fecha, 'HORA' : hora})
    print("                                 -->Registro Insertado Con exito")


def Editadato(documento, nombre, correo, telefono, fecha, hora, idpalabra):
    palabras = db['citas']
    idpalabra = int(idpalabra)
    palabras.update({'id': idpalabra}, {'id': idpalabra, 'DOCUMENTO' : documento, 'NOMBRE' : nombre, 'CORREO' : correo, 'TELEFONO' : telefono, 'FECHA' : fecha, 'HORA' : hora})
    print("                                 --> Registro Actualizado con Exito")


def Borradato(idpalabra):
    palabras = db['citas']
    idpalabra = int(idpalabra)
    palabras.remove({'id': idpalabra})

    print("                                 --> Registro Eliminado con Exito")


def BuscaDato(palabra, muestra):
    palabras = db['citas']

    if muestra == 3:
        palabra = int(palabra)
        salida = palabras.find({"id":palabra})
        return salida
    if muestra == 2:
        salida = palabras.find()
        return salida
    if muestra == 1:
        palabra: eval("/" + palabra + "/i")
        salida = palabras.find({"EXPRESION": {"$regex": palabra}})
        # salida = (palabras.find({"EXPRESION""": palabra}))
        for dato in salida:
            print(dato['id'], " - " + dato['EXPRESION'], " - " + dato['SIGNIFICADO'])


def CreaBD():
    secuencia = db['secuencia']
    secuencia.drop()
    secuencia.insert_one({'id': 'identity', 'seq': 0})

    coleccion = db['citas']
    coleccion.drop()
    coleccion.insert_one(
        {'id': numerador(), 'DOCUMENTO' : 'E-8-161077', 'NOMBRE' : 'CESAR BELTRAN','CORREO' : 'CESARBELTRAN.CO@GMAIL.COM', 'TELEFONO' : '60703617', 'FECHA' : '20210501', 'HORA' : '14:20'})


    # coleccion.insert_one({'id':numerador(),'EXPRESION': 'A guanchinche', 'SIGNIFICADO': ' a caballito, cargando a espaldas'})
