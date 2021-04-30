import pymongo
import json
from bson.json_util import dumps
from bson import json_util

from pymongo import MongoClient

MONGO_UBI = 'mongodb://localhost'
engine = MongoClient(MONGO_UBI)
db = engine['slam']


def numerador():
    secuencia = db['secuencia']
    contador = secuencia.find_one_and_update(filter={'id': 'identity'},
                                             update={'$inc': {'seq': 1}},
                                             upsert=True,
                                             return_document=pymongo.ReturnDocument.AFTER)
    dato = contador["seq"]
    return dato


def Insertadato(palabra, significado):
    palabras = db['slam']
    palabras.insert_one({'id': numerador(), 'EXPRESION': palabra, 'SIGNIFICADO': significado})

    print("")
    print("                                 -->Registro Insertado Con exito")
    print("")



def Editadato(palabra, significado, idpalabra):
    palabras = db['slam']
    idpalabra = int(idpalabra)
    palabras.update({'id': idpalabra}, {'id': idpalabra, 'EXPRESION': palabra, 'SIGNIFICADO': significado})

    print("                                 --> Registro Actualizado con Exito")
    print("")



def Borradato(idpalabra):
    idpalabra = int(idpalabra)
    palabras = db['slam']
    palabras.remove({'id': idpalabra})
    print(idpalabra)
    print("                                 --> Registro Eliminado con Exito")
    print("")



def BuscaDato(palabra, muestra):
    palabras = db['slam']
    palabra: eval("/" + palabra + "/i")
    if muestra == 3:
        palabra = int(palabra)
        salida = palabras.find({"id":palabra})
        return salida
    if muestra == 2:
        salida = palabras.find()
        return salida

    if muestra == 1:
        salida = palabras.find({"EXPRESION": {"$regex": palabra}})
        # salida = (palabras.find({"EXPRESION""": palabra}))
        for dato in salida:
            print(dato['id'], " - " + dato['EXPRESION'], " - " + dato['SIGNIFICADO'])




def CreaBD():
    secuencia = db['secuencia']
    secuencia.drop()
    secuencia.insert_one({'id': 'identity', 'seq': 0})

    coleccion = db['slam']
    coleccion.drop()
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'A guanchinche', 'SIGNIFICADO': ' a caballito, cargando a espaldas'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'A monchinche', 'SIGNIFICADO': ' a caballito, cargando a espaldas'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Abuelazón',
                          'SIGNIFICADO': ' Dícese de la conducta de entusiasmo excesivo que los abuelos sienten por los nietos; actitud típica de personas ancianas.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Agarrar los mangos bajitos',
                          'SIGNIFICADO': 'hacer algo de la forma más facil.'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Ahuevado', 'SIGNIFICADO': ' sinónimo de huevón, lento, imbécil'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'ahuevao', 'SIGNIFICADO': ' sinónimo de huevón, lento, imbécil'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Ahuevazón',
                          'SIGNIFICADO': ' Situacion calificada de ahuevada (situación causada pur una tontera/por un tonto).'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Allá adonde uno ',
                          'SIGNIFICADO': ' El interior.(normalmente pronunciado alla onde uno)'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Arrabalero', 'SIGNIFICADO': ' Buscapleitos'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Arrabalera', 'SIGNIFICADO': ' Buscapleitos'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Arranque',
                          'SIGNIFICADO': ' Parranda.((de arrancarse [irse de fiesta/a parrandear]))'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Arrebatiña, pata y puñete',
                          'SIGNIFICADO': ' lo que pasa despues que alguien rompe la piñata.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Arrecho',
                          'SIGNIFICADO': ' persona que esta excitada sexualmente. Persona que puede realizar cualquier trabajo o hazaña(termino utilizado con mayor frecuencia en el interior del país).'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Arrecha',
                          'SIGNIFICADO': ' persona que esta excitada sexualmente. Persona que puede realizar cualquier trabajo o hazaña(termino utilizado con mayor frecuencia en el interior del país).'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Arrepinchoso', 'SIGNIFICADO': ' Persona que le gusta el arranque'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Arrepinchosa', 'SIGNIFICADO': ' Persona que le gusta el arranque'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Arropar',
                          'SIGNIFICADO': ' hacer el amor con la ropa, comúnmente visto en saraos o en lugares con poca intimidad.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Arroz con Mango', 'SIGNIFICADO': ' Grandes problemas'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Trepa que sube', 'SIGNIFICADO': ' Grandes problemas'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'pandemonio', 'SIGNIFICADO': ' Grandes problemas'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Ayala',
                          'SIGNIFICADO': ' interjección de sorpresa o enojo. Adaptado de Vaya la. Usualmente utilizado con palabras curiosas y soeces. Ejm: Ayala Peste, áyala máquina, áyala vida. (pronunciado también áshala)'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Bagre', 'SIGNIFICADO': ' Mujer horrible o poco agraciada físicamente'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Cangreja', 'SIGNIFICADO': ' Mujer horrible o poco agraciada físicamente'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Gárgola', 'SIGNIFICADO': ' Mujer horrible o poco agraciada físicamente'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Cocobola', 'SIGNIFICADO': ' Mujer horrible o poco agraciada físicamente'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Baño de pueblo',
                          'SIGNIFICADO': ' participar de alguna actividad normalmente de tipo folklorica para renovar el espiritu Panameno... irse a un pindin, cantaderas, comer frituras, baile tipico, etc.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Barriada Bruja',
                          'SIGNIFICADO': 'Asentamiento HumanoInformal/ Villa mísera o Favela.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Barrio Brujo',
                          'SIGNIFICADO': 'Asentamiento HumanoInformal/ Villa mísera o Favela.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Bate',
                          'SIGNIFICADO': 'Excusa difícil de creer, o golpe de suerte. Ejm:James Bond es un batoso, me metió un bate; cigarro de Marihuana de gran tamaño'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Batería', 'SIGNIFICADO': ' papel con respuestas de un examen'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Berraco',
                          'SIGNIFICADO': ' (sust) persona diestra, hábil; (adj) furioso; (adj) díficil.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Berraca',
                          'SIGNIFICADO': ' (sust) persona diestra, hábil; (adj) furioso; (adj) díficil.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Berrinche',
                          'SIGNIFICADO': ' Armar un escándalo o necedad[Ejm. Ese niño tiene un berrinche]. Olor fuerte a orine[Ejm. Este baño huele a berrinche].'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Biencuidao',
                          'SIGNIFICADO': ' Individuo que se gana la vida cuidando autos y consiguiendo estacionamientos en lugares como centros comerciales, discotecas, cines, almacenes.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Birria',
                          'SIGNIFICADO': ' Juego muy repetitivo sin espiritu de competencia o finalidad alguna, comunmente usado para los videojuegos, futbol o baloncesto.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Blanco', 'SIGNIFICADO': ' cigarrillo'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Blazear',
                          'SIGNIFICADO': ' Ofender.(se utiliza como verbo en infinitivo-gerundio, ej: Juan me estaba blazeando.)'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Bochinche', 'SIGNIFICADO': ' chisme.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Borrador', 'SIGNIFICADO': ' Un gran Autobús o Camion.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Bote',
                          'SIGNIFICADO': ' Pedir que te lleven o te den un aventon a algun lugar (Hey un bote pue).'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Botella',
                          'SIGNIFICADO': ' Persona que cobra pero no trabaja; se da mucho esta situación en sector público panameño.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Bravos de Boston',
                          'SIGNIFICADO': ' El mejor de una profesión. dedicado a los bravos de boston de 1914.[1]'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Brujo', 'SIGNIFICADO': ' barato, de poca calidad.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Gallo', 'SIGNIFICADO': ' barato, de poca calidad.'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Buco', 'SIGNIFICADO': ' mucho (galicismo; derivado de beaucoup).'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Bueno',
                          'SIGNIFICADO': ' que esta muy bonita o bonita y tiene buen fisico,[ejm. Mami tas wena]; también pay (como en es un pay).'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Buena',
                          'SIGNIFICADO': ' que esta muy bonita o bonita y tiene buen fisico,[ejm. Mami tas wena]; también pay (como en es un pay).'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Bulto',
                          'SIGNIFICADO': ' Persona que no tiene un buen desempeño de sus funciones, viene de ocupar un espacio determinado siendo irrelevante para la situacion.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Burundanga',
                          'SIGNIFICADO': 'alimento de poco valor nutritivo. Ejm: caramelos, chocolates, chicles, etc...'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Cafá', 'SIGNIFICADO': ' Una Palmada fuerte átras en la cabeza.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Camarón',
                          'SIGNIFICADO': ' actividad extracurricular que permite a un individuo ganar dinero extra. Su origen se remonta a los tiempos en que los gringos le decían a los localesCome around...(pásate por aquí).[Ejm. Voy a hacer un camarón]'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Cangreja',
                          'SIGNIFICADO': ' Mujer de baja categoria que usalmente sale por las noches y no puede caminar normalmente de tanta profesion... baja la marea y suben las cangrejas expresion que se usa cuando cae la noche en Panama.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Chachai', 'SIGNIFICADO': ' Vestido de niña.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Chambón', 'SIGNIFICADO': ' Torpe'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Chantin', 'SIGNIFICADO': ' casa, hogar.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Chen chen', 'SIGNIFICADO': ' Dinero'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Chequear', 'SIGNIFICADO': ' revisar'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Chicha',
                          'SIGNIFICADO': ' Refresco o bebida fermentada. (Esta palabra, recogida por laRAEy de etimología panameña es usada en Centroamérica, Chile y Perú, con ciertas variaciones)'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Chichí',
                          'SIGNIFICADO': ' 1)Forma cariñosa de decir Bebe; Forma cariñosa de deicirle a novia o novio'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Chifear', 'SIGNIFICADO': ' No invitar/ignorar a alguna persona.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Chilin',
                          'SIGNIFICADO': ' del ingles Chilling estar tranquilo; parkear cool; ejm: estaba parkeando chillin en la chantin.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Chinguear', 'SIGNIFICADO': ' apostar'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Chino o Chinito',
                          'SIGNIFICADO': ' bodega / tienda de abarrotes (dícese porque generalmente están administradas por chinos)'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Chiquishow',
                          'SIGNIFICADO': 'Dicese de un espectáculo púgil no programado en el que los combatientes por lo general no saben pelear de forma vistosa. También utilizado para indicar cuando a alguien le hacen un espectaculo frente a otras personas, regularmente realizado por el sexo femenino.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Chirrisco',
                          'SIGNIFICADO': ' Bebida hecha en casa proveniente comúnmente de la fermentacion y destilacion del maiz o la caña.'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Chiva', 'SIGNIFICADO': ' Transporte colectivo de capacidad media'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Choborro',
                          'SIGNIFICADO': ' persona brusca y de poca capacidad para desarrollar una actividad.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Choborra',
                          'SIGNIFICADO': ' persona brusca y de poca capacidad para desarrollar una actividad.'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Cholipay', 'SIGNIFICADO': ' mujer mestiza/indígena atractiva físicamente'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Cholo',
                          'SIGNIFICADO': ' En zonas del interior haciendo referencia a amigo, en la ciudad hace referencia a personas del interior.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Cholometal',
                          'SIGNIFICADO': ' cholo o indigena que sigue modismos de roqueros, punks y/o heavymetals.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'CholoPop',
                          'SIGNIFICADO': ' un compa que acaba de llegar a la capital vestido como en los 70s, con el pecho afuero y usando essencia de pacholi como perfume.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Cholywood',
                          'SIGNIFICADO': ' Forma graciosa, despectiva o una manera para definir la farándula panameña.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Chombo', 'SIGNIFICADO': ' persona de raza negra.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Chomba', 'SIGNIFICADO': ' persona de raza negra.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Chonta', 'SIGNIFICADO': ' cabeza'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Chota',
                          'SIGNIFICADO': ' minivan de la policía. También utilizada para referirse a joder.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Chota', 'SIGNIFICADO': ' Policia.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Tongo', 'SIGNIFICADO': ' Policia.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Chuain',
                          'SIGNIFICADO': ' (de pronunciación rápida) Esta es un sinónimo de Yeye y es una persona acomodada, alta alcurnia, delicada o adinerada.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Chucha',
                          'SIGNIFICADO': ' Vulva; también usado como interjección (Ejemplo:¡Chucha!, Que chucha me importa!)'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Chuchita',
                          'SIGNIFICADO': ' véaseCongo.[Ejm. Te tan (están) cogiendo de congo!!!]'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Chuleta', 'SIGNIFICADO': ' Exclamacion de sorpresa o admiracion'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Chupar', 'SIGNIFICADO': ' Ingerir bebidas alcoholicas'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Chuzo', 'SIGNIFICADO': ' Ver Chuleta'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Cocho',
                          'SIGNIFICADO': ' Golpe en la cabeza propinado con los nudillos de la mano. ejemplo Te voy a dar un cocho!'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Cocoa',
                          'SIGNIFICADO': ' Cuento o historia relacionada a un suceso o evento, normalmente un bochinche o chisme.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Cinta',
                          'SIGNIFICADO': ' Cuento o historia relacionada a un suceso o evento, normalmente un bochinche o chisme.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Compa',
                          'SIGNIFICADO': ' frase cariñosa refiriendose a un campesino o a un compadre... buen amigo.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Conflei',
                          'SIGNIFICADO': ' Cualquier cereal de cualquier marca que se come en el desayuno, del inglés Corn Flakes'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Coscorrón',
                          'SIGNIFICADO': ' insecto redondo y cafe, golpe dado con los nudillos (vease cocho).(normalmente cocorrón) '})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Cuatrera',
                          'SIGNIFICADO': ' Mujer la cual esta en busca o acecho de algun hombre cazado.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Cueco', 'SIGNIFICADO': 'homosexualolesbiana'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Cueca', 'SIGNIFICADO': 'homosexualolesbiana'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Culantro',
                          'SIGNIFICADO': ' Una bella dama. Proveniente del Segmento Doble Vida del programa televisivo Parecen Noticias. Tambien es una un planta que se utiliza para sazonar la sopa y otros alimentos.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Culear',
                          'SIGNIFICADO': ' manera vulgar de decir tener relaciones sexuales osexocon una persona .'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Culillo', 'SIGNIFICADO': ' miedo, terror o temor a una cosa'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'ñáñara', 'SIGNIFICADO': ' miedo, terror o temor a una cosa'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Culito', 'SIGNIFICADO': ' Ver Pay'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Culo', 'SIGNIFICADO': ' Nalgas'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Datien', 'SIGNIFICADO': ' traspalante de tienda'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'De a vaina',
                          'SIGNIFICADO': ' ganar algo por pura buena suerte en el ultimo momento.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'De a vainilla',
                          'SIGNIFICADO': ' ganar algo por pura buena suerte en el ultimo momento.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'por un pelito',
                          'SIGNIFICADO': ' ganar algo por pura buena suerte en el ultimo momento.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'por un cocoazo',
                          'SIGNIFICADO': ' ganar algo por pura buena suerte en el ultimo momento.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'por pura leche',
                          'SIGNIFICADO': ' ganar algo por pura buena suerte en el ultimo momento.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'De agencia ', 'SIGNIFICADO': 'nítido, bonito, nuevo'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'De vez', 'SIGNIFICADO': ' de una vez, en el acto'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Diablo rojo',
                          'SIGNIFICADO': ' Autobus generalmente pintado de varios colores procedente de las escuelas estadounidenses que comúnmente se les llama borradores por el efecto que produce durante una colision.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'En tuco',
                          'SIGNIFICADO': ' Sinonimo quiebra de no tener dinero, hace referencia a cuando un automovil esta montado sobre pedazos de madera, generalmente sin llantas o en reparacion.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'En verga',
                          'SIGNIFICADO': ' Algo de mala calidad, no complaciente al gusto de nadie ese show esta en verga'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Falta de todo',
                          'SIGNIFICADO': ' Versión moderna de la famosa frase venezolana popularizada en los 80 falta de glamour. Significa falta de respeto, falta de ética, falta de elegancia, falta de clase, falta de consideración, falta de... todo.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Ficha', 'SIGNIFICADO': ' persona importante'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Filo', 'SIGNIFICADO': ' Arma punzocortante'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Flintin',
                          'SIGNIFICADO': ' Proveniente de el Patois( ver Guari-Guari), referente a una pareja peleando, donde la mujer le tira cosas al hombre, en ingles Jamaiquino(patois) flying things , usado para describir un problema, conflicto o pelea. Yo no quiero flintin con ese man.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Fulo', 'SIGNIFICADO': ' Rubio/a.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Fula', 'SIGNIFICADO': ' Rubio/a.'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Fundillo', 'SIGNIFICADO': ' especificamente el orificio anal.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Fuste', 'SIGNIFICADO': ' Nalgas, Trasero.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Gadaca',
                          'SIGNIFICADO': ' traspalante de. cagada(algo que sale mal de momento)'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Gallinero',
                          'SIGNIFICADO': 'la entreda general o area popular de algun evento cultural (concierto) o evento deportivo.'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Gallo', 'SIGNIFICADO': ' Barato, de poca calidad; persona sin gracia.'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Galla', 'SIGNIFICADO': ' Barato, de poca calidad; persona sin gracia.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Gandoca', 'SIGNIFICADO': ' traspalante de cagando(defecar)'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Garnatón',
                          'SIGNIFICADO': ' Bofetón. *Garnatada normalmente se dice garnatá.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Garnatada',
                          'SIGNIFICADO': ' Bofetón. *Garnatada normalmente se dice garnatá.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Globito',
                          'SIGNIFICADO': ' Condon, preservativo; *forrito ha sido popularizado por el homónimo personaje condón del popular programa La Cáscara.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Forrito',
                          'SIGNIFICADO': ' Condon, preservativo; *forrito ha sido popularizado por el homónimo personaje condón del popular programa La Cáscara.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Golpe de ala',
                          'SIGNIFICADO': ' aroma intolerable que procede de las exilas... vulg. ver Grajo'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Grajo', 'SIGNIFICADO': ' sudor de las exilas sumamente apestoso'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Grubeo',
                          'SIGNIFICADO': ' Estar con una persona por un tiempo o por una noche para pasarla bien y para nada serio o formal.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Grubear',
                          'SIGNIFICADO': ' Estar con una persona por un tiempo o por una noche para pasarla bien y para nada serio o formal.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Guabazo',
                          'SIGNIFICADO': ' Gran golpe, usualmente seguido de hematoma de alguna clase.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Guabanazo',
                          'SIGNIFICADO': ' Gran golpe, usualmente seguido de hematoma de alguna clase.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Guacho',
                          'SIGNIFICADO': 'es una sopa espesa que lleva ñame, yuca, culantro, arroz, verduras y alguna carne, que puede ser res, rabito de puerco o chicharrón. El guacho se sirve tradicionalmente en una totuma, plato que se fabrica partiendo a la mitad unos frutos redondos y duros que crecen en el monte. Tambien siginfica la combinacion de varias cosas.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Guagua',
                          'SIGNIFICADO': ' se dice de un automóvil muy viejo o en mal estado.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Guapin',
                          'SIGNIFICADO': ' Saludo que indica que pasa. Del inglésWhat happened? / What is happening?.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Juatapin',
                          'SIGNIFICADO': ' Saludo que indica que pasa. Del inglésWhat happened? / What is happening?.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Guapote',
                          'SIGNIFICADO': ' individuo usualmente con poca autoestima que hace mucha fisicultura pero que al final siempre sigue siendo bien FEO'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Guari-guari',
                          'SIGNIFICADO': ' Dialecto de la Provincia de Bocas del Toro, es una mezcla de Español, Francés, Inglés y lenguas indígenas.'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Guaro', 'SIGNIFICADO': ' Alcohol; bebiba alcohólica; licor.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Guillado',
                          'SIGNIFICADO': ' 1.influenciado por alucinógenos 2.emocionado, inspirado. (normalmente se dice guillao) '})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Huevear',
                          'SIGNIFICADO': ' Perder el tiempo de la peor forma.[Ejm. Pónte a trabajá y deja de ta webiando!!!]'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Ir al choque', 'SIGNIFICADO': ' ir de frente ante cualquier adversidad.'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Joder', 'SIGNIFICADO': ' Bromear, molestar, irritar. Ejm: No jodas!'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Juega vivo',
                          'SIGNIFICADO': ' con astucia, generalmente sin moral, oportunista.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Jugo-e-Policia', 'SIGNIFICADO': ' agua'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Kenke', 'SIGNIFICADO': ' Bate de marihuana'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'la Kenton',
                          'SIGNIFICADO': ' llave en lucha libre que se usa para amarrar al adversario, usando las piernas, mientras lo repletan de roncabalaos... usalmente esta llave se usa por mujeres que quieren tener hijos obligando al novio a ejacular dentro del vientre... por eso se dice cuidao y te hace la kenton.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Labia',
                          'SIGNIFICADO': ' Adulación, normalmente para convencer a la persona de cual es la mejor alternativa en una situación dada o para conseguir apoyo de la misma; muy comun en el ambito de la politica.'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Láiter', 'SIGNIFICADO': ' Encendedor, anglicismo [de lighter].'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Laopé', 'SIGNIFICADO': ' traspalante de pelao (muchacho)'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Levante',
                          'SIGNIFICADO': 'Novio/a, quiénes se gustan y tienen química entre ellos.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Limado',
                          'SIGNIFICADO': ' Dicese de la persona que se encuentra muy cansada luego de trabajar o beber mucho.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Limpio (a)', 'SIGNIFICADO': ' Sin dinero.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Lleca', 'SIGNIFICADO': 'traspalantederivado de Calle'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Loco',
                          'SIGNIFICADO': ' Es como se llaman los amigos de cariño. Muy comun entre oriundos de Panamá.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Machiua',
                          'SIGNIFICADO': ' Mas cholo que un Cholo Pop... usualmente un indigena.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Machigua',
                          'SIGNIFICADO': ' Mas cholo que un Cholo Pop... usualmente un indigena.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Machihua',
                          'SIGNIFICADO': ' Mas cholo que un Cholo Pop... usualmente un indigena.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Machoemonte', 'SIGNIFICADO': ' Tipo mas tof que Rambo'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Mafá',
                          'SIGNIFICADO': ' abrebocas de harina (fritura) en forma de trenza; dícese de un enredo, asunto complicado, o personas abrazadas de forma muy afectiva (como mafá).'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Maleante',
                          'SIGNIFICADO': ' Delincuente o persona que quiere ser como los delincuentes.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Manacho',
                          'SIGNIFICADO': ' Hombre joven de clase obrera, cuerpo atlético y aspecto un poco rudo y muy masculino. Manacha: Lesbiana.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Manzanillo',
                          'SIGNIFICADO': ' sin personalidad, influenciable con facilidad, también se dice así a los vividores.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Matapuerco o Soplamoco',
                          'SIGNIFICADO': ' Golpe exagerado y certero, que duele mucho. Nótese que soplamoco es ehn la mejilla.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Me vale verga',
                          'SIGNIFICADO': ' Situación que no genera ninguna clase de reacción ni de interés en la persona.(vulgar)/un pepino/un comino'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Meña',
                          'SIGNIFICADO': ' jóvenes de la calle de mal hablar y vestir. Denota las últimas 4 letras de la nacionalidad Panameña. También traspalante del tubérculo ñame)'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Meto',
                          'SIGNIFICADO': ' una expresión que denota una frase de admiración y afirmación muy utilizada en la provincia de Chiriquí. En la ciudad de Panamá (sobretodo) ofi.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Millo',
                          'SIGNIFICADO': ' Palomitas de maíz. Millo viene de la lengua gallega y quiere decir maíz. En Galicia se le llama a las palomitas de maíz, flocos de millo.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Mococoa',
                          'SIGNIFICADO': ' liquido producido por los miembros nasales, regularmente de color verde, esta se bebe en grandes cantidades usualmente luego de que a uno lo han traicionado (ver quemado) en una relacion se creia seria.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Montado',
                          'SIGNIFICADO': ' Que tiene buena situación económica. (normalmente se dice montao/a)'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Ñamería', 'SIGNIFICADO': ' Locura.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Ñampearse', 'SIGNIFICADO': ' volverse loco/a.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Ñángara',
                          'SIGNIFICADO': ' forma despectiva de definir a los comunistas o miembros de partido de izquierda o extrema izquierda.'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Ñangotado', 'SIGNIFICADO': ' Persona que camina en cuclillas'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Añingotado', 'SIGNIFICADO': ' Persona que camina en cuclillas'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Ñapa',
                          'SIGNIFICADO': ' Un regalo que dan cuando se compra algo en un tienda o abarroterria (introducido por los chinos para captar clientes frecuentes).'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Ñecks',
                          'SIGNIFICADO': ' Versión decente de mierda.[Ejm. Te wa (voy a) sacá la ñecks!!!]'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Nevera',
                          'SIGNIFICADO': ' refrigeradora; autobús con aire acondicionado (dícese de los trans-provinciales [ejm: Panamá-David] porque normalmente van a temperaturas muy frías); mujer cuadrada.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'No me parece',
                          'SIGNIFICADO': ' Frase popularmente utilizada para demostrar descontento por algo.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Ñorro ', 'SIGNIFICADO': ' Homosexual/ Ese man es ñorro.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Ofi',
                          'SIGNIFICADO': ' entendido, OK (acortación de oficial, utilizado para aprobar o recibir aprobación).'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Palante', 'SIGNIFICADO': ' reducción derivada depara adelante'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Paciero(s)',
                          'SIGNIFICADO': ' Amigo, generalmente amigos con quienes se comparte parrandas.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Paja', 'SIGNIFICADO': ' masturbarse'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Volar Cometa', 'SIGNIFICADO': ' masturbarse'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Pajizo',
                          'SIGNIFICADO': ' persona que se masturba constantemente; persona que muestra debilidad ante una actividad física.[Ejm. Jo! no puedes ni levantar eso... tas pajizo!!!].'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Pajiza',
                          'SIGNIFICADO': ' persona que se masturba constantemente; persona que muestra debilidad ante una actividad física.[Ejm. Jo! no puedes ni levantar eso... tas pajizo!!!].'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Paka',
                          'SIGNIFICADO': ' Cargamento de droga; persona que tiene fardos/mochilas/ bultos [del inglés packs]; referente a cartuchos de balas; delincuente.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Paracaídas',
                          'SIGNIFICADO': ' persona que acude a una reunión o fiesta sin invitación.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Parapapeo',
                          'SIGNIFICADO': ' Palabra que describe el baile de las reinas de carnaval. Verbo: parapapear; ejm: está parapapeando. El término se deriva del sonido de las trompetas de una murga: Para pa pá'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Parkin', 'SIGNIFICADO': ' Fiesta o reunión entre amigos.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Parquearr',
                          'SIGNIFICADO': ' Salir con alguien a pasar el rato: parquear con mis amigos; poner a alguien en su sitio Quiso insultarme y lo parqueé. Normalmente la gente dice parquiar.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Patacón',
                          'SIGNIFICADO': ' Popular acompañamiento de comida, el cual consiste en rodajas deplátanoaplastadas y luego fritas.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Pataconcito',
                          'SIGNIFICADO': ' Pequeña acumulación de basura, viene del relleno sanitario de la ciudad de Panamá (Cerro Patacón).'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Patatús', 'SIGNIFICADO': ' Desmayo, ataque cardíaco'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Pati-amarillo',
                          'SIGNIFICADO': ' Cigarrillo con el filtro de color amarillo o anaranjado.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Pato ',
                          'SIGNIFICADO': ' ver sacalodo, tutifruti, punky-punch ...i.e. homosexual'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'ñorro',
                          'SIGNIFICADO': ' ver sacalodo, tutifruti, punky-punch ...i.e. homosexual'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': ' ñaño',
                          'SIGNIFICADO': ' ver sacalodo, tutifruti, punky-punch ...i.e. homosexual'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Pebre', 'SIGNIFICADO': ' comida'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'refine', 'SIGNIFICADO': ' comida'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Pelo pelo', 'SIGNIFICADO': ' Baile erótico'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Pelonera',
                          'SIGNIFICADO': ' Golpiza propiciada entre varios sin ser fuerte, comúnmente en la cebeza y en la secundaria.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Perro',
                          'SIGNIFICADO': ' Despectivo utilizado como sinónimo de mujeriego; usado como insulto.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Perron',
                          'SIGNIFICADO': ' Persona de poca capacidad. Dicese de una persona que no es muy popular dentro de un circulo'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Perrón',
                          'SIGNIFICADO': ' Persona que no desempeña bien una funcion referenciada o exageracion de perro.'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Pescuezona', 'SIGNIFICADO': ' cerveza de botella tamaño grande.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Peso',
                          'SIGNIFICADO': ' Moneda de 50 centavos, viene del periodo de la separación de Panama de Colombia donde equivalía el peso colombiano a 50 centavos de dólar; usado comúnmente en las peleas de gallos para cuantificar las apuestas.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Picando',
                          'SIGNIFICADO': ' algo que está de moda.(Su uso se debe al famoso baile del pique, en Panamá.)'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Pichi', 'SIGNIFICADO': ' Droga, dícese comúnmente a la cocaina'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Piedra', 'SIGNIFICADO': ' crack (droga).'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Piedrero',
                          'SIGNIFICADO': ' persona drogadicta que ha llegado a la indigencia por ser drogadicto.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Piedrera',
                          'SIGNIFICADO': ' persona drogadicta que ha llegado a la indigencia por ser drogadicto.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Pilar',
                          'SIGNIFICADO': ' estudiar con afón; pilón(a) es alguien muy estudiso o sabelotodo.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Pilinqui', 'SIGNIFICADO': ' Persona mezquina.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Pillar',
                          'SIGNIFICADO': ' Synonimo de tomar/coger/Agarrar, ejm: pilla la pluma...; encontrar a hurtadillas una situacion o ver algo en especial.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Pinta', 'SIGNIFICADO': ' cerveza'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Fría', 'SIGNIFICADO': ' cerveza'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Pipí', 'SIGNIFICADO': ' pene, miembro viril; orine.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Plena',
                          'SIGNIFICADO': ' Usado para canciones/ritmos dereggaepero también usada para otros géneros cuando la cancion es buena.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Ponchar',
                          'SIGNIFICADO': ' desinflar; tener sexo; sacar a un bateador por out en béisbol.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Ponchera', 'SIGNIFICADO': ' Desorden, algarabía.'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Porcón', 'SIGNIFICADO': ' Entiéndase popcon o palomitas de mais'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Millo', 'SIGNIFICADO': ' Entiéndase popcon o palomitas de mais'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Praka praka', 'SIGNIFICADO': ' Derivacion de Rakataca.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Puesto Quemado', 'SIGNIFICADO': ' Puesto reservado'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'qué Bate',
                          'SIGNIFICADO': ' usado como descripción de algo ficticio, asombroso o espectacular'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'que es lo que es',
                          'SIGNIFICADO': ' que hay de nuevo. (pronunciado que lo que é o queloqué)'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Qué xopá', 'SIGNIFICADO': 'traspalante, derivado de¿qué paso?'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Quemado',
                          'SIGNIFICADO': ' Persona a la cual su novio/novia esposo/esposa lo ha traicionado con otra/o.'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Queso', 'SIGNIFICADO': ' Cierta atracción meramente física y sexual.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Rakataca',
                          'SIGNIFICADO': ' hombe o mujer sin clase, comunmente utiliza mayormente la jerga panameña autoctona. Derivado del sonido de las metralletas al disparar rakatakatakatakataka popularizado durante una canción del grupo Jam & Suppose en 1992: Camión lleno de gun.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Rambulero',
                          'SIGNIFICADO': ' Persona usualmente de los barrios populares que gusta de las peleas, intrigas, chismes, baile y otras manifestaciones de comunicación sin clase.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Rangálido', 'SIGNIFICADO': ' de mal aspecto, flaco'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Rantan', 'SIGNIFICADO': ' Mucho.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Real',
                          'SIGNIFICADO': ' Moneda de 5 centésimos de balboa. La palabra viene de la época de la colonia en la cual se le denominaba Real a las monedas acuñadas en Potosí, Lima y en algunos otros lugares. En Taboga, Panamá, por ejemplo una familia llegó a encontrar una cantidad de monedas de denominación de pesos de 8 reales, mientras construían su casa.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Pau Pau',
                          'SIGNIFICADO': ' Castigo a los hijos, ya sea darles con la correa (rejera) o con nalgadas (pau pau).'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Rejera',
                          'SIGNIFICADO': ' Castigo a los hijos, ya sea darles con la correa (rejera) o con nalgadas (pau pau).'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Rejeros',
                          'SIGNIFICADO': ' Grupos de hombres (amigos entre sí) que van a una discoteca, clubes nocturnos o fiesta a ligarse con mujeres o que simplemente se reúnen para pasarla bien. También se reúnen en un casa para libar licor y echar historias u apspectos personales que le han pasado. El programa de Humor de la Cascara hizo una parodia de esto.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Rejo', 'SIGNIFICADO': ' azote, pene.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Reventar', 'SIGNIFICADO': ' vacilar, tomar el tiempo.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Detonar', 'SIGNIFICADO': ' vacilar, tomar el tiempo.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Romper', 'SIGNIFICADO': ' vacilar, tomar el tiempo.'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Rompe pecho', 'SIGNIFICADO': ' una Botella de cerveza muy grande.'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Manga larga', 'SIGNIFICADO': ' una Botella de cerveza muy grande.'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Roncabalao', 'SIGNIFICADO': 'Golpe exagerado capaz de matar a una persona.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Sabrosón',
                          'SIGNIFICADO': ' Algo o alguien que se encuentre en excelentes condiciones o algún evento agradable.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Sacalodo', 'SIGNIFICADO': ' ver cuecon'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'tutifruti', 'SIGNIFICADO': ' ver cuecon'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'punkypunch', 'SIGNIFICADO': ' ver cuecon'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Salao',
                          'SIGNIFICADO': ' Persona que tiene mala suerte. Ejm.Mario tuestás saladoen la lotería.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Sarao',
                          'SIGNIFICADO': ' Fiesta o baile organizada generalmente por el segundo ciclo de secundaria. Típicamente se realiza en horas de la tarde, en el gimnasio de la escuela. Dícese de cualquier fiesta en que el objetivo principal es bailar.'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Sólido', 'SIGNIFICADO': 'Significaexcelente. También chévere.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Tallao', 'SIGNIFICADO': 'Bien vestido.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Tarrantan', 'SIGNIFICADO': 'Más que rantan. Muchísimo.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Tatai',
                          'SIGNIFICADO': 'Bye, hasta luego, nos vemos.*Tá bien (viene de: está bien; se le da significado según la dicción, pronunciación y el tono de la voz usada por la persona) Algo sorprendente; falso; exagerado; emocionante; todos los significados anteriores a la vez.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Tella', 'SIGNIFICADO': 'Botella (generalmente de licor).'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Totuma: ',
                          'SIGNIFICADO': 'Es un plato que se fabrica partiendo a la mitad unos frutos redondos y duros que crecen en el monte (calabazo).'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Tongo', 'SIGNIFICADO': ' Policia de bajo rango'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Tontón', 'SIGNIFICADO': ' Vagina'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Micha', 'SIGNIFICADO': ' Vagina'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Mota', 'SIGNIFICADO': ' Vagina'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Trozo', 'SIGNIFICADO': ' Vagina'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Tortillera', 'SIGNIFICADO': 'lesbiana'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Trepaquesube/verguero/chuchamadre/zaperoco',
                          'SIGNIFICADO': ' gran problema, disturbio, desorden, conflicto'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Verguero', 'SIGNIFICADO': ' gran problema, disturbio, desorden, conflicto'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Chuchamadre',
                          'SIGNIFICADO': ' gran problema, disturbio, desorden, conflicto'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Zaperoco', 'SIGNIFICADO': ' gran problema, disturbio, desorden, conflicto'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Trueno', 'SIGNIFICADO': ' Arma de fuego'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Vaca',
                          'SIGNIFICADO': ' Colecta de dinero entre varias personas para comprar algo. Hey hagan una vaca pala Carmen ahí...'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Vaina',
                          'SIGNIFICADO': ' Utilizado como comodín en conversaciones, usado porcosa(también usado en otros países con el mismo significado).'})
    coleccion.insert_one(
        {'id': numerador(), 'EXPRESION': 'Vale cebo', 'SIGNIFICADO': ' Dícese de una situación injusta o estúpida.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Vampira',
                          'SIGNIFICADO': ' Mujeres de alto mantenimiento, sumamente ignorantes en todo menos en el arte de hacer el amor.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Chupasangre',
                          'SIGNIFICADO': ' Mujeres de alto mantenimiento, sumamente ignorantes en todo menos en el arte de hacer el amor.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Vergüero',
                          'SIGNIFICADO': ' Problema, debate discusion acalorada llegando al punto cercano a formarse una trifulca.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Vidajenear',
                          'SIGNIFICADO': ' Husmear, espiar, y entrometerse en la vida ajena.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Violinista',
                          'SIGNIFICADO': ' Persona que acopaña a una pareja pero no debe estar presente pues la pareja quiere arropar. (veáse arropar).'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Yapla',
                          'SIGNIFICADO': ' playa. sale del reverso de playa, yaspla, y quitándole pla.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Yeye',
                          'SIGNIFICADO': ' Persona adinerada que presume de su condición, comúnmente usa anglicismos en su habla.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Rabiblanco',
                          'SIGNIFICADO': ' Persona adinerada que presume de su condición, comúnmente usa anglicismos en su habla.'})
    coleccion.insert_one({'id': numerador(), 'EXPRESION': 'Zambito(a)',
                          'SIGNIFICADO': ' expresión de las provincias de Herrera y Los Santos, significaniño o niña.'})

    # coleccion.insert_one({'id':numerador(),'EXPRESION': 'A guanchinche', 'SIGNIFICADO': ' a caballito, cargando a espaldas'})
