import redis
conexion = redis.StrictRedis(host = '127.0.0.1', port ='6379')


def numerador():
    dato = conexion.incr("secuencia", 1)
    return dato

def buscaid(id):
    datos = conexion.hgetall("slam")
    salida=""
    for dato in datos:
        cadena = str(dato).upper()
        strcade = str(id)
        if cadena.find(strcade, 1,5) != -1:
            salida = dato
    return salida

def Insertadato(palabra, significado):
    conexion.hset("slam", str(numerador()) + '- ' + palabra + ' :', significado)
    print("")
    print("                                 -->Registro Insertado Con exito")
    print("")
    p = input("Presione una <Enter> para continuar")

def Editadato(palabra, significado, idpalabra):
    ax = (buscaid(idpalabra))
    conexion.hdel("slam", ax)
    conexion.hset("slam", str(numerador()) + '- ' + palabra + ' :',  significado)


    print("                                 --> Registro Actualizado con Exito")
    print("")
    p = input("Presione una <Enter> para continuar")

def Borradato(idpalabra):
    ax = (buscaid(idpalabra))
    conexion.hdel("slam", ax)

    print("                                 --> Registro Eliminado con Exito")
    print("")
    p = input("Presione una <Enter> para continuar")

def BuscaDato(palabra, muestra):
    datos = conexion.hgetall("slam")
    for dato in datos:
        cadena = str(dato).upper()
        if cadena.find(palabra) != -1:
            print(dato + conexion.hget("slam", dato))

    if muestra == 1:
        print("                                 --> Registros encontrados")
        print("")
        p = input("Presione una <Enter> para continuar")

def CreaBD():
    conexion.set("secuencia", 0)
    conexion.flushall()
    conexion.hset("slam", str(numerador()) + '- A guanchinche :', ' a caballito, cargando a espaldas')
    conexion.hset("slam", str(numerador()) + '- A monchinche :', ' a caballito, cargando a espaldas')
    conexion.hset("slam", str(numerador()) + '- Abuelazon :',
                  ' Dicese de la conducta de entusiasmo excesivo que los abuelos sienten por los nietos; actitud tipica de personas ancianas.')
    conexion.hset("slam", str(numerador()) + '- Agarrar los mangos bajitos :', 'hacer algo de la forma mas facil.')
    conexion.hset("slam", str(numerador()) + '- Ahuevado :', ' sinonimo de huevon, lento, imbecil')
    conexion.hset("slam", str(numerador()) + '- ahuevao :', ' sinonimo de huevon, lento, imbecil')
    conexion.hset("slam", str(numerador()) + '- Ahuevazon :',
                  ' Situacion calificada de ahuevada (situacion causada pur una tontera/por un tonto).')
    conexion.hset("slam", str(numerador()) + '- Alla adonde uno  :',
                  ' El interior.(normalmente pronunciado alla onde uno)')
    conexion.hset("slam", str(numerador()) + '- Arrabalero :', ' Buscapleitos')
    conexion.hset("slam", str(numerador()) + '- Arrabalera :', ' Buscapleitos')
    conexion.hset("slam", str(numerador()) + '- Arranque :',
                  ' Parranda.((de arrancarse [irse de fiesta/a parrandear]))')
    conexion.hset("slam", str(numerador()) + '- Arrebatiña, pata y puñete :',
                  ' lo que pasa despues que alguien rompe la piñata.')
    conexion.hset("slam", str(numerador()) + '- Arrecho :',
                  ' persona que esta excitada sexualmente. Persona que puede realizar cualquier trabajo o hazaña(termino utilizado con mayor frecuencia en el interior del pais).')
    conexion.hset("slam", str(numerador()) + '- Arrecha :',
                  ' persona que esta excitada sexualmente. Persona que puede realizar cualquier trabajo o hazaña(termino utilizado con mayor frecuencia en el interior del pais).')
    conexion.hset("slam", str(numerador()) + '- Arrepinchoso :', ' Persona que le gusta el arranque')
    conexion.hset("slam", str(numerador()) + '- Arrepinchosa :', ' Persona que le gusta el arranque')
    conexion.hset("slam", str(numerador()) + '- Arropar :',
                  ' hacer el amor con la ropa, comunmente visto en saraos o en lugares con poca intimidad.')
    conexion.hset("slam", str(numerador()) + '- Arroz con Mango :', ' Grandes problemas')
    conexion.hset("slam", str(numerador()) + '- Trepa que sube :', ' Grandes problemas')
    conexion.hset("slam", str(numerador()) + '- pandemonio :', ' Grandes problemas')
    conexion.hset("slam", str(numerador()) + '- Ayala :',
                  ' interjeccion de sorpresa o enojo. Adaptado de Vaya la. Usualmente utilizado con palabras curiosas y soeces. Ejm: Ayala Peste, ayala maquina, ayala vida. (pronunciado tambien ashala)')
    conexion.hset("slam", str(numerador()) + '- Bagre :', ' Mujer horrible o poco agraciada fisicamente')
    conexion.hset("slam", str(numerador()) + '- Cangreja :', ' Mujer horrible o poco agraciada fisicamente')
    conexion.hset("slam", str(numerador()) + '- Gargola :', ' Mujer horrible o poco agraciada fisicamente')
    conexion.hset("slam", str(numerador()) + '- Cocobola :', ' Mujer horrible o poco agraciada fisicamente')
    conexion.hset("slam", str(numerador()) + '- Baño de pueblo :',
                  ' participar de alguna actividad normalmente de tipo folklorica para renovar el espiritu Panameno... irse a un pindin, cantaderas, comer frituras, baile tipico, etc.')
    conexion.hset("slam", str(numerador()) + '- Barriada Bruja :',
                  'Asentamiento HumanoInformal/ Villa misera o Favela.')
    conexion.hset("slam", str(numerador()) + '- Barrio Brujo :', 'Asentamiento HumanoInformal/ Villa misera o Favela.')
    conexion.hset("slam", str(numerador()) + '- Bate :',
                  'Excusa dificil de creer, o golpe de suerte. Ejm:James Bond es un batoso, me metio un bate; cigarro de Marihuana de gran tamaño')
    conexion.hset("slam", str(numerador()) + '- Bateria :', ' papel con respuestas de un examen')
    conexion.hset("slam", str(numerador()) + '- Berraco :',
                  ' (sust) persona diestra, habil; (adj) furioso; (adj) dificil.')
    conexion.hset("slam", str(numerador()) + '- Berraca :',
                  ' (sust) persona diestra, habil; (adj) furioso; (adj) dificil.')
    conexion.hset("slam", str(numerador()) + '- Berrinche :',
                  ' Armar un escandalo o necedad[Ejm. Ese niño tiene un berrinche]. Olor fuerte a orine[Ejm. Este baño huele a berrinche].')
    conexion.hset("slam", str(numerador()) + '- Biencuidao :',
                  ' Individuo que se gana la vida cuidando autos y consiguiendo estacionamientos en lugares como centros comerciales, discotecas, cines, almacenes.')
    conexion.hset("slam", str(numerador()) + '- Birria :',
                  ' Juego muy repetitivo sin espiritu de competencia o finalidad alguna, comunmente usado para los videojuegos, futbol o baloncesto.')
    conexion.hset("slam", str(numerador()) + '- Blanco :', ' cigarrillo')
    conexion.hset("slam", str(numerador()) + '- Blazear :',
                  ' Ofender.(se utiliza como verbo en infinitivo-gerundio, ej: Juan me estaba blazeando.)')
    conexion.hset("slam", str(numerador()) + '- Bochinche :', ' chisme.')
    conexion.hset("slam", str(numerador()) + '- Borrador :', ' Un gran Autobus o Camion.')
    conexion.hset("slam", str(numerador()) + '- Bote :',
                  ' Pedir que te lleven o te den un aventon a algun lugar (Hey un bote pue).')
    conexion.hset("slam", str(numerador()) + '- Botella :',
                  ' Persona que cobra pero no trabaja; se da mucho esta situacion en sector publico panameño.')
    conexion.hset("slam", str(numerador()) + '- Bravos de Boston :',
                  ' El mejor de una profesion. dedicado a los bravos de boston de 1914.[1]')
    conexion.hset("slam", str(numerador()) + '- Brujo :', ' barato, de poca calidad.')
    conexion.hset("slam", str(numerador()) + '- Gallo :', ' barato, de poca calidad.')
    conexion.hset("slam", str(numerador()) + '- Buco :', ' mucho (galicismo; derivado de beaucoup).')
    conexion.hset("slam", str(numerador()) + '- Bueno :',
                  ' que esta muy bonita o bonita y tiene buen fisico,[ejm. Mami tas wena]; tambien pay (como en es un pay).')
    conexion.hset("slam", str(numerador()) + '- Buena :',
                  ' que esta muy bonita o bonita y tiene buen fisico,[ejm. Mami tas wena]; tambien pay (como en es un pay).')
    conexion.hset("slam", str(numerador()) + '- Bulto :',
                  ' Persona que no tiene un buen desempeño de sus funciones, viene de ocupar un espacio determinado siendo irrelevante para la situacion.')
    conexion.hset("slam", str(numerador()) + '- Burundanga :',
                  'alimento de poco valor nutritivo. Ejm: caramelos, chocolates, chicles, etc...')
    conexion.hset("slam", str(numerador()) + '- Cafa :', ' Una Palmada fuerte atras en la cabeza.')
    conexion.hset("slam", str(numerador()) + '- Camaron :',
                  ' actividad extracurricular que permite a un individuo ganar dinero extra. Su origen se remonta a los tiempos en que los gringos le decian a los localesCome around...(pasate por aqui).[Ejm. Voy a hacer un camaron]')
    conexion.hset("slam", str(numerador()) + '- Cangreja :',
                  ' Mujer de baja categoria que usalmente sale por las noches y no puede caminar normalmente de tanta profesion... baja la marea y suben las cangrejas expresion que se usa cuando cae la noche en Panama.')
    conexion.hset("slam", str(numerador()) + '- Chachai :', ' Vestido de niña.')
    conexion.hset("slam", str(numerador()) + '- Chambon :', ' Torpe')
    conexion.hset("slam", str(numerador()) + '- Chantin :', ' casa, hogar.')
    conexion.hset("slam", str(numerador()) + '- Chen chen :', ' Dinero')
    conexion.hset("slam", str(numerador()) + '- Chequear :', ' revisar')
    conexion.hset("slam", str(numerador()) + '- Chicha :',
                  ' Refresco o bebida fermentada. (Esta palabra, recogida por laRAEy de etimologia panameña es usada en Centroamerica, Chile y Peru, con ciertas variaciones)')
    conexion.hset("slam", str(numerador()) + '- Chichi :',
                  ' 1)Forma cariñosa de decir Bebe; Forma cariñosa de deicirle a novia o novio')
    conexion.hset("slam", str(numerador()) + '- Chifear :', ' No invitar/ignorar a alguna persona.')
    conexion.hset("slam", str(numerador()) + '- Chilin :',
                  ' del ingles Chilling estar tranquilo; parkear cool; ejm: estaba parkeando chillin en la chantin.')
    conexion.hset("slam", str(numerador()) + '- Chinguear :', ' apostar')
    conexion.hset("slam", str(numerador()) + '- Chino o Chinito :',
                  ' bodega / tienda de abarrotes (dicese porque generalmente estan administradas por chinos)')
    conexion.hset("slam", str(numerador()) + '- Chiquishow :',
                  'Dicese de un espectaculo pugil no programado en el que los combatientes por lo general no saben pelear de forma vistosa. Tambien utilizado para indicar cuando a alguien le hacen un espectaculo frente a otras personas, regularmente realizado por el sexo femenino.')
    conexion.hset("slam", str(numerador()) + '- Chirrisco :',
                  ' Bebida hecha en casa proveniente comunmente de la fermentacion y destilacion del maiz o la caña.')
    conexion.hset("slam", str(numerador()) + '- Chiva :', ' Transporte colectivo de capacidad media')
    conexion.hset("slam", str(numerador()) + '- Choborro :',
                  ' persona brusca y de poca capacidad para desarrollar una actividad.')
    conexion.hset("slam", str(numerador()) + '- Choborra :',
                  ' persona brusca y de poca capacidad para desarrollar una actividad.')
    conexion.hset("slam", str(numerador()) + '- Cholipay :', ' mujer mestiza/indigena atractiva fisicamente')
    conexion.hset("slam", str(numerador()) + '- Cholo :',
                  ' En zonas del interior haciendo referencia a amigo, en la ciudad hace referencia a personas del interior.')
    conexion.hset("slam", str(numerador()) + '- Cholometal :',
                  ' cholo o indigena que sigue modismos de roqueros, punks y/o heavymetals.')
    conexion.hset("slam", str(numerador()) + '- CholoPop :',
                  ' un compa que acaba de llegar a la capital vestido como en los 70s, con el pecho afuero y usando essencia de pacholi como perfume.')
    conexion.hset("slam", str(numerador()) + '- Cholywood :',
                  ' Forma graciosa, despectiva o una manera para definir la farandula panameña.')
    conexion.hset("slam", str(numerador()) + '- Chombo :', ' persona de raza negra.')
    conexion.hset("slam", str(numerador()) + '- Chomba :', ' persona de raza negra.')
    conexion.hset("slam", str(numerador()) + '- Chonta :', ' cabeza')
    conexion.hset("slam", str(numerador()) + '- Chota :',
                  ' minivan de la policia. Tambien utilizada para referirse a joder.')
    conexion.hset("slam", str(numerador()) + '- Chota :', ' Policia.')
    conexion.hset("slam", str(numerador()) + '- Tongo :', ' Policia.')
    conexion.hset("slam", str(numerador()) + '- Chuain :',
                  ' (de pronunciacion rapida) Esta es un sinonimo de Yeye y es una persona acomodada, alta alcurnia, delicada o adinerada.')
    conexion.hset("slam", str(numerador()) + '- Chucha :',
                  ' Vulva; tambien usado como interjeccion (Ejemplo:¡Chucha!, Que chucha me importa!)')
    conexion.hset("slam", str(numerador()) + '- Chuchita :', ' veaseCongo.[Ejm. Te tan (estan) cogiendo de congo!!!]')
    conexion.hset("slam", str(numerador()) + '- Chuleta :', ' Exclamacion de sorpresa o admiracion')
    conexion.hset("slam", str(numerador()) + '- Chupar :', ' Ingerir bebidas alcoholicas')
    conexion.hset("slam", str(numerador()) + '- Chuzo :', ' Ver Chuleta')
    conexion.hset("slam", str(numerador()) + '- Cocho :',
                  ' Golpe en la cabeza propinado con los nudillos de la mano. ejemplo Te voy a dar un cocho!')
    conexion.hset("slam", str(numerador()) + '- Cocoa :',
                  ' Cuento o historia relacionada a un suceso o evento, normalmente un bochinche o chisme.')
    conexion.hset("slam", str(numerador()) + '- Cinta :',
                  ' Cuento o historia relacionada a un suceso o evento, normalmente un bochinche o chisme.')
    conexion.hset("slam", str(numerador()) + '- Compa :',
                  ' frase cariñosa refiriendose a un campesino o a un compadre... buen amigo.')
    conexion.hset("slam", str(numerador()) + '- Conflei :',
                  ' Cualquier cereal de cualquier marca que se come en el desayuno, del ingles Corn Flakes')
    conexion.hset("slam", str(numerador()) + '- Coscorron :',
                  ' insecto redondo y cafe, golpe dado con los nudillos (vease cocho).(normalmente cocorron) ')
    conexion.hset("slam", str(numerador()) + '- Cuatrera :',
                  ' Mujer la cual esta en busca o acecho de algun hombre cazado.')
    conexion.hset("slam", str(numerador()) + '- Cueco :', 'homosexualolesbiana')
    conexion.hset("slam", str(numerador()) + '- Cueca :', 'homosexualolesbiana')
    conexion.hset("slam", str(numerador()) + '- Culantro :',
                  ' Una bella dama. Proveniente del Segmento Doble Vida del programa televisivo Parecen Noticias. Tambien es una un planta que se utiliza para sazonar la sopa y otros alimentos.')
    conexion.hset("slam", str(numerador()) + '- Culear :',
                  ' manera vulgar de decir tener relaciones sexuales osexocon una persona .')
    conexion.hset("slam", str(numerador()) + '- Culillo :', ' miedo, terror o temor a una cosa')
    conexion.hset("slam", str(numerador()) + '- ñañara :', ' miedo, terror o temor a una cosa')
    conexion.hset("slam", str(numerador()) + '- Culito :', ' Ver Pay')
    conexion.hset("slam", str(numerador()) + '- Culo :', ' Nalgas')
    conexion.hset("slam", str(numerador()) + '- Datien :', ' traspalante de tienda')
    conexion.hset("slam", str(numerador()) + '- De a vaina :',
                  ' ganar algo por pura buena suerte en el ultimo momento.')
    conexion.hset("slam", str(numerador()) + '- De a vainilla :',
                  ' ganar algo por pura buena suerte en el ultimo momento.')
    conexion.hset("slam", str(numerador()) + '- por un pelito :',
                  ' ganar algo por pura buena suerte en el ultimo momento.')
    conexion.hset("slam", str(numerador()) + '- por un cocoazo :',
                  ' ganar algo por pura buena suerte en el ultimo momento.')
    conexion.hset("slam", str(numerador()) + '- por pura leche :',
                  ' ganar algo por pura buena suerte en el ultimo momento.')
    conexion.hset("slam", str(numerador()) + '- De agencia  :', 'nitido, bonito, nuevo')
    conexion.hset("slam", str(numerador()) + '- De vez :', ' de una vez, en el acto')
    conexion.hset("slam", str(numerador()) + '- Diablo rojo :',
                  ' Autobus generalmente pintado de varios colores procedente de las escuelas estadounidenses que comunmente se les llama borradores por el efecto que produce durante una colision.')
    conexion.hset("slam", str(numerador()) + '- En tuco :',
                  ' Sinonimo quiebra de no tener dinero, hace referencia a cuando un automovil esta montado sobre pedazos de madera, generalmente sin llantas o en reparacion.')
    conexion.hset("slam", str(numerador()) + '- En verga :',
                  ' Algo de mala calidad, no complaciente al gusto de nadie ese show esta en verga')
    conexion.hset("slam", str(numerador()) + '- Falta de todo :',
                  ' Version moderna de la famosa frase venezolana popularizada en los 80 falta de glamour. Significa falta de respeto, falta de etica, falta de elegancia, falta de clase, falta de consideracion, falta de... todo.')
    conexion.hset("slam", str(numerador()) + '- Ficha :', ' persona importante')
    conexion.hset("slam", str(numerador()) + '- Filo :', ' Arma punzocortante')
    conexion.hset("slam", str(numerador()) + '- Flintin :',
                  ' Proveniente de el Patois( ver Guari-Guari), referente a una pareja peleando, donde la mujer le tira cosas al hombre, en ingles Jamaiquino(patois) flying things , usado para describir un problema, conflicto o pelea. Yo no quiero flintin con ese man.')
    conexion.hset("slam", str(numerador()) + '- Fulo :', ' Rubio/a.')
    conexion.hset("slam", str(numerador()) + '- Fula :', ' Rubio/a.')
    conexion.hset("slam", str(numerador()) + '- Fundillo :', ' especificamente el orificio anal.')
    conexion.hset("slam", str(numerador()) + '- Fuste :', ' Nalgas, Trasero.')
    conexion.hset("slam", str(numerador()) + '- Gadaca :', ' traspalante de. cagada(algo que sale mal de momento)')
    conexion.hset("slam", str(numerador()) + '- Gallinero :',
                  'la entreda general o area popular de algun evento cultural (concierto) o evento deportivo.')
    conexion.hset("slam", str(numerador()) + '- Gallo :', ' Barato, de poca calidad; persona sin gracia.')
    conexion.hset("slam", str(numerador()) + '- Galla :', ' Barato, de poca calidad; persona sin gracia.')
    conexion.hset("slam", str(numerador()) + '- Gandoca :', ' traspalante de cagando(defecar)')
    conexion.hset("slam", str(numerador()) + '- Garnaton :', ' Bofeton. *Garnatada normalmente se dice garnata.')
    conexion.hset("slam", str(numerador()) + '- Garnatada :', ' Bofeton. *Garnatada normalmente se dice garnata.')
    conexion.hset("slam", str(numerador()) + '- Globito :',
                  ' Condon, preservativo; *forrito ha sido popularizado por el homonimo personaje condon del popular programa La Cascara.')
    conexion.hset("slam", str(numerador()) + '- Forrito :',
                  ' Condon, preservativo; *forrito ha sido popularizado por el homonimo personaje condon del popular programa La Cascara.')
    conexion.hset("slam", str(numerador()) + '- Golpe de ala :',
                  ' aroma intolerable que procede de las exilas... vulg. ver Grajo')
    conexion.hset("slam", str(numerador()) + '- Grajo :', ' sudor de las exilas sumamente apestoso')
    conexion.hset("slam", str(numerador()) + '- Grubeo :',
                  ' Estar con una persona por un tiempo o por una noche para pasarla bien y para nada serio o formal.')
    conexion.hset("slam", str(numerador()) + '- Grubear :',
                  ' Estar con una persona por un tiempo o por una noche para pasarla bien y para nada serio o formal.')
    conexion.hset("slam", str(numerador()) + '- Guabazo :',
                  ' Gran golpe, usualmente seguido de hematoma de alguna clase.')
    conexion.hset("slam", str(numerador()) + '- Guabanazo :',
                  ' Gran golpe, usualmente seguido de hematoma de alguna clase.')
    conexion.hset("slam", str(numerador()) + '- Guacho :',
                  'es una sopa espesa que lleva ñame, yuca, culantro, arroz, verduras y alguna carne, que puede ser res, rabito de puerco o chicharron. El guacho se sirve tradicionalmente en una totuma, plato que se fabrica partiendo a la mitad unos frutos redondos y duros que crecen en el monte. Tambien siginfica la combinacion de varias cosas.')
    conexion.hset("slam", str(numerador()) + '- Guagua :', ' se dice de un automovil muy viejo o en mal estado.')
    conexion.hset("slam", str(numerador()) + '- Guapin :',
                  ' Saludo que indica que pasa. Del inglesWhat happened? / What is happening?.')
    conexion.hset("slam", str(numerador()) + '- Juatapin :',
                  ' Saludo que indica que pasa. Del inglesWhat happened? / What is happening?.')
    conexion.hset("slam", str(numerador()) + '- Guapote :',
                  ' individuo usualmente con poca autoestima que hace mucha fisicultura pero que al final siempre sigue siendo bien FEO')
    conexion.hset("slam", str(numerador()) + '- Guari-guari :',
                  ' Dialecto de la Provincia de Bocas del Toro, es una mezcla de Español, Frances, Ingles y lenguas indigenas.')
    conexion.hset("slam", str(numerador()) + '- Guaro :', ' Alcohol; bebiba alcoholica; licor.')
    conexion.hset("slam", str(numerador()) + '- Guillado :',
                  ' 1.influenciado por alucinogenos 2.emocionado, inspirado. (normalmente se dice guillao) ')
    conexion.hset("slam", str(numerador()) + '- Huevear :',
                  ' Perder el tiempo de la peor forma.[Ejm. Ponte a trabaja y deja de ta webiando!!!]')
    conexion.hset("slam", str(numerador()) + '- Ir al choque :', ' ir de frente ante cualquier adversidad.')
    conexion.hset("slam", str(numerador()) + '- Joder :', ' Bromear, molestar, irritar. Ejm: No jodas!')
    conexion.hset("slam", str(numerador()) + '- Juega vivo :', ' con astucia, generalmente sin moral, oportunista.')
    conexion.hset("slam", str(numerador()) + '- Jugo-e-Policia :', ' agua')
    conexion.hset("slam", str(numerador()) + '- Kenke :', ' Bate de marihuana')
    conexion.hset("slam", str(numerador()) + '- la Kenton :',
                  ' llave en lucha libre que se usa para amarrar al adversario, usando las piernas, mientras lo repletan de roncabalaos... usalmente esta llave se usa por mujeres que quieren tener hijos obligando al novio a ejacular dentro del vientre... por eso se dice cuidao y te hace la kenton.')
    conexion.hset("slam", str(numerador()) + '- Labia :',
                  ' Adulacion, normalmente para convencer a la persona de cual es la mejor alternativa en una situacion dada o para conseguir apoyo de la misma; muy comun en el ambito de la politica.')
    conexion.hset("slam", str(numerador()) + '- Laiter :', ' Encendedor, anglicismo [de lighter].')
    conexion.hset("slam", str(numerador()) + '- Laope :', ' traspalante de pelao (muchacho)')
    conexion.hset("slam", str(numerador()) + '- Levante :', 'Novio/a, quienes se gustan y tienen quimica entre ellos.')
    conexion.hset("slam", str(numerador()) + '- Limado :',
                  ' Dicese de la persona que se encuentra muy cansada luego de trabajar o beber mucho.')
    conexion.hset("slam", str(numerador()) + '- Limpio (a) :', ' Sin dinero.')
    conexion.hset("slam", str(numerador()) + '- Lleca :', 'traspalantederivado de Calle')
    conexion.hset("slam", str(numerador()) + '- Loco :',
                  ' Es como se llaman los amigos de cariño. Muy comun entre oriundos de Panama.')
    conexion.hset("slam", str(numerador()) + '- Machiua :', ' Mas cholo que un Cholo Pop... usualmente un indigena.')
    conexion.hset("slam", str(numerador()) + '- Machigua :', ' Mas cholo que un Cholo Pop... usualmente un indigena.')
    conexion.hset("slam", str(numerador()) + '- Machihua :', ' Mas cholo que un Cholo Pop... usualmente un indigena.')
    conexion.hset("slam", str(numerador()) + '- Machoemonte :', ' Tipo mas tof que Rambo')
    conexion.hset("slam", str(numerador()) + '- Mafa :',
                  ' abrebocas de harina (fritura) en forma de trenza; dicese de un enredo, asunto complicado, o personas abrazadas de forma muy afectiva (como mafa).')
    conexion.hset("slam", str(numerador()) + '- Maleante :',
                  ' Delincuente o persona que quiere ser como los delincuentes.')
    conexion.hset("slam", str(numerador()) + '- Manacho :',
                  ' Hombre joven de clase obrera, cuerpo atletico y aspecto un poco rudo y muy masculino. Manacha: Lesbiana.')
    conexion.hset("slam", str(numerador()) + '- Manzanillo :',
                  ' sin personalidad, influenciable con facilidad, tambien se dice asi a los vividores.')
    conexion.hset("slam", str(numerador()) + '- Matapuerco o Soplamoco :',
                  ' Golpe exagerado y certero, que duele mucho. Notese que soplamoco es ehn la mejilla.')
    conexion.hset("slam", str(numerador()) + '- Me vale verga :',
                  ' Situacion que no genera ninguna clase de reaccion ni de interes en la persona.(vulgar)/un pepino/un comino')
    conexion.hset("slam", str(numerador()) + '- Meña :',
                  ' jovenes de la calle de mal hablar y vestir. Denota las ultimas 4 letras de la nacionalidad Panameña. Tambien traspalante del tuberculo ñame)')
    conexion.hset("slam", str(numerador()) + '- Meto :',
                  ' una expresion que denota una frase de admiracion y afirmacion muy utilizada en la provincia de Chiriqui. En la ciudad de Panama (sobretodo) ofi.')
    conexion.hset("slam", str(numerador()) + '- Millo :',
                  ' Palomitas de maiz. Millo viene de la lengua gallega y quiere decir maiz. En Galicia se le llama a las palomitas de maiz, flocos de millo.')
    conexion.hset("slam", str(numerador()) + '- Mococoa :',
                  ' liquido producido por los miembros nasales, regularmente de color verde, esta se bebe en grandes cantidades usualmente luego de que a uno lo han traicionado (ver quemado) en una relacion se creia seria.')
    conexion.hset("slam", str(numerador()) + '- Montado :',
                  ' Que tiene buena situacion economica. (normalmente se dice montao/a)')
    conexion.hset("slam", str(numerador()) + '- Ñameria :', ' Locura.')
    conexion.hset("slam", str(numerador()) + '- Ñampearse :', ' volverse loco/a.')
    conexion.hset("slam", str(numerador()) + '- Ñangara :',
                  ' forma despectiva de definir a los comunistas o miembros de partido de izquierda o extrema izquierda.')
    conexion.hset("slam", str(numerador()) + '- Ñangotado :', ' Persona que camina en cuclillas')
    conexion.hset("slam", str(numerador()) + '- Añingotado :', ' Persona que camina en cuclillas')
    conexion.hset("slam", str(numerador()) + '- Ñapa :',
                  ' Un regalo que dan cuando se compra algo en un tienda o abarroterria (introducido por los chinos para captar clientes frecuentes).')
    conexion.hset("slam", str(numerador()) + '- Ñecks :',
                  ' Version decente de mierda.[Ejm. Te wa (voy a) saca la ñecks!!!]')
    conexion.hset("slam", str(numerador()) + '- Nevera :',
                  ' refrigeradora; autobus con aire acondicionado (dicese de los trans-provinciales [ejm: Panama-David] porque normalmente van a temperaturas muy frias); mujer cuadrada.')
    conexion.hset("slam", str(numerador()) + '- No me parece :',
                  ' Frase popularmente utilizada para demostrar descontento por algo.')
    conexion.hset("slam", str(numerador()) + '- Ñorro  :', ' Homosexual/ Ese man es ñorro.')
    conexion.hset("slam", str(numerador()) + '- Ofi :',
                  ' entendido, OK (acortacion de oficial, utilizado para aprobar o recibir aprobacion).')
    conexion.hset("slam", str(numerador()) + '- Palante :', ' reduccion derivada depara adelante')
    conexion.hset("slam", str(numerador()) + '- Paciero(s) :',
                  ' Amigo, generalmente amigos con quienes se comparte parrandas.')
    conexion.hset("slam", str(numerador()) + '- Paja :', ' masturbarse')
    conexion.hset("slam", str(numerador()) + '- Volar Cometa :', ' masturbarse')
    conexion.hset("slam", str(numerador()) + '- Pajizo :',
                  ' persona que se masturba constantemente; persona que muestra debilidad ante una actividad fisica.[Ejm. Jo! no puedes ni levantar eso... tas pajizo!!!].')
    conexion.hset("slam", str(numerador()) + '- Pajiza :',
                  ' persona que se masturba constantemente; persona que muestra debilidad ante una actividad fisica.[Ejm. Jo! no puedes ni levantar eso... tas pajizo!!!].')
    conexion.hset("slam", str(numerador()) + '- Paka :',
                  ' Cargamento de droga; persona que tiene fardos/mochilas/ bultos [del ingles packs]; referente a cartuchos de balas; delincuente.')
    conexion.hset("slam", str(numerador()) + '- Paracaidas :',
                  ' persona que acude a una reunion o fiesta sin invitacion.')
    conexion.hset("slam", str(numerador()) + '- Parapapeo :',
                  ' Palabra que describe el baile de las reinas de carnaval. Verbo: parapapear; ejm: esta parapapeando. El termino se deriva del sonido de las trompetas de una murga: Para pa pa')
    conexion.hset("slam", str(numerador()) + '- Parkin :', ' Fiesta o reunion entre amigos.')
    conexion.hset("slam", str(numerador()) + '- Parquearr :',
                  ' Salir con alguien a pasar el rato: parquear con mis amigos; poner a alguien en su sitio Quiso insultarme y lo parquee. Normalmente la gente dice parquiar.')
    conexion.hset("slam", str(numerador()) + '- Patacon :',
                  ' Popular acompañamiento de comida, el cual consiste en rodajas deplatanoaplastadas y luego fritas.')
    conexion.hset("slam", str(numerador()) + '- Pataconcito :',
                  ' Pequeña acumulacion de basura, viene del relleno sanitario de la ciudad de Panama (Cerro Patacon).')
    conexion.hset("slam", str(numerador()) + '- Patatus :', ' Desmayo, ataque cardiaco')
    conexion.hset("slam", str(numerador()) + '- Pati-amarillo :',
                  ' Cigarrillo con el filtro de color amarillo o anaranjado.')
    conexion.hset("slam", str(numerador()) + '- Pato  :', ' ver sacalodo, tutifruti, punky-punch ...i.e. homosexual')
    conexion.hset("slam", str(numerador()) + '- ñorro :', ' ver sacalodo, tutifruti, punky-punch ...i.e. homosexual')
    conexion.hset("slam", str(numerador()) + '-  ñaño :', ' ver sacalodo, tutifruti, punky-punch ...i.e. homosexual')
    conexion.hset("slam", str(numerador()) + '- Pebre :', ' comida')
    conexion.hset("slam", str(numerador()) + '- refine :', ' comida')
    conexion.hset("slam", str(numerador()) + '- Pelo pelo :', ' Baile erotico')
    conexion.hset("slam", str(numerador()) + '- Pelonera :',
                  ' Golpiza propiciada entre varios sin ser fuerte, comunmente en la cebeza y en la secundaria.')
    conexion.hset("slam", str(numerador()) + '- Perro :',
                  ' Despectivo utilizado como sinonimo de mujeriego; usado como insulto.')
    conexion.hset("slam", str(numerador()) + '- Perron :',
                  ' Persona de poca capacidad. Dicese de una persona que no es muy popular dentro de un circulo')
    conexion.hset("slam", str(numerador()) + '- Perron :',
                  ' Persona que no desempeña bien una funcion referenciada o exageracion de perro.')
    conexion.hset("slam", str(numerador()) + '- Pescuezona :', ' cerveza de botella tamaño grande.')
    conexion.hset("slam", str(numerador()) + '- Peso :',
                  ' Moneda de 50 centavos, viene del periodo de la separacion de Panama de Colombia donde equivalia el peso colombiano a 50 centavos de dolar; usado comunmente en las peleas de gallos para cuantificar las apuestas.')
    conexion.hset("slam", str(numerador()) + '- Picando :',
                  ' algo que esta de moda.(Su uso se debe al famoso baile del pique, en Panama.)')
    conexion.hset("slam", str(numerador()) + '- Pichi :', ' Droga, dicese comunmente a la cocaina')
    conexion.hset("slam", str(numerador()) + '- Piedra :', ' crack (droga).')
    conexion.hset("slam", str(numerador()) + '- Piedrero :',
                  ' persona drogadicta que ha llegado a la indigencia por ser drogadicto.')
    conexion.hset("slam", str(numerador()) + '- Piedrera :',
                  ' persona drogadicta que ha llegado a la indigencia por ser drogadicto.')
    conexion.hset("slam", str(numerador()) + '- Pilar :',
                  ' estudiar con afon; pilon(a) es alguien muy estudiso o sabelotodo.')
    conexion.hset("slam", str(numerador()) + '- Pilinqui :', ' Persona mezquina.')
    conexion.hset("slam", str(numerador()) + '- Pillar :',
                  ' Synonimo de tomar/coger/Agarrar, ejm: pilla la pluma...; encontrar a hurtadillas una situacion o ver algo en especial.')
    conexion.hset("slam", str(numerador()) + '- Pinta :', ' cerveza')
    conexion.hset("slam", str(numerador()) + '- Fria :', ' cerveza')
    conexion.hset("slam", str(numerador()) + '- Pipi :', ' pene, miembro viril; orine.')
    conexion.hset("slam", str(numerador()) + '- Plena :',
                  ' Usado para canciones/ritmos dereggaepero tambien usada para otros generos cuando la cancion es buena.')
    conexion.hset("slam", str(numerador()) + '- Ponchar :',
                  ' desinflar; tener sexo; sacar a un bateador por out en beisbol.')
    conexion.hset("slam", str(numerador()) + '- Ponchera :', ' Desorden, algarabia.')
    conexion.hset("slam", str(numerador()) + '- Porcon :', ' Entiendase popcon o palomitas de mais')
    conexion.hset("slam", str(numerador()) + '- Millo :', ' Entiendase popcon o palomitas de mais')
    conexion.hset("slam", str(numerador()) + '- Praka praka :', ' Derivacion de Rakataca.')
    conexion.hset("slam", str(numerador()) + '- Puesto Quemado :', ' Puesto reservado')
    conexion.hset("slam", str(numerador()) + '- que Bate :',
                  ' usado como descripcion de algo ficticio, asombroso o espectacular')
    conexion.hset("slam", str(numerador()) + '- que es lo que es :',
                  ' que hay de nuevo. (pronunciado que lo que e o queloque)')
    conexion.hset("slam", str(numerador()) + '- Que xopa :', 'traspalante, derivado de¿que paso?')
    conexion.hset("slam", str(numerador()) + '- Quemado :',
                  ' Persona a la cual su novio/novia esposo/esposa lo ha traicionado con otra/o.')
    conexion.hset("slam", str(numerador()) + '- Queso :', ' Cierta atraccion meramente fisica y sexual.')
    conexion.hset("slam", str(numerador()) + '- Rakataca :',
                  ' hombe o mujer sin clase, comunmente utiliza mayormente la jerga panameña autoctona. Derivado del sonido de las metralletas al disparar rakatakatakatakataka popularizado durante una cancion del grupo Jam & Suppose en 1992: Camion lleno de gun.')
    conexion.hset("slam", str(numerador()) + '- Rambulero :',
                  ' Persona usualmente de los barrios populares que gusta de las peleas, intrigas, chismes, baile y otras manifestaciones de comunicacion sin clase.')
    conexion.hset("slam", str(numerador()) + '- Rangalido :', ' de mal aspecto, flaco')
    conexion.hset("slam", str(numerador()) + '- Rantan :', ' Mucho.')
    conexion.hset("slam", str(numerador()) + '- Real :',
                  ' Moneda de 5 centesimos de balboa. La palabra viene de la epoca de la colonia en la cual se le denominaba Real a las monedas acuñadas en Potosi, Lima y en algunos otros lugares. En Taboga, Panama, por ejemplo una familia llego a encontrar una cantidad de monedas de denominacion de pesos de 8 reales, mientras construian su casa.')
    conexion.hset("slam", str(numerador()) + '- Pau Pau :',
                  ' Castigo a los hijos, ya sea darles con la correa (rejera) o con nalgadas (pau pau).')
    conexion.hset("slam", str(numerador()) + '- Rejera :',
                  ' Castigo a los hijos, ya sea darles con la correa (rejera) o con nalgadas (pau pau).')
    conexion.hset("slam", str(numerador()) + '- Rejeros :',
                  ' Grupos de hombres (amigos entre si) que van a una discoteca, clubes nocturnos o fiesta a ligarse con mujeres o que simplemente se reunen para pasarla bien. Tambien se reunen en un casa para libar licor y echar historias u apspectos personales que le han pasado. El programa de Humor de la Cascara hizo una parodia de esto.')
    conexion.hset("slam", str(numerador()) + '- Rejo :', ' azote, pene.')
    conexion.hset("slam", str(numerador()) + '- Reventar :', ' vacilar, tomar el tiempo.')
    conexion.hset("slam", str(numerador()) + '- Detonar :', ' vacilar, tomar el tiempo.')
    conexion.hset("slam", str(numerador()) + '- Romper :', ' vacilar, tomar el tiempo.')
    conexion.hset("slam", str(numerador()) + '- Rompe pecho :', ' una Botella de cerveza muy grande.')
    conexion.hset("slam", str(numerador()) + '- Manga larga :', ' una Botella de cerveza muy grande.')
    conexion.hset("slam", str(numerador()) + '- Roncabalao :', 'Golpe exagerado capaz de matar a una persona.')
    conexion.hset("slam", str(numerador()) + '- Sabroson :',
                  ' Algo o alguien que se encuentre en excelentes condiciones o algun evento agradable.')
    conexion.hset("slam", str(numerador()) + '- Sacalodo :', ' ver cuecon')
    conexion.hset("slam", str(numerador()) + '- tutifruti :', ' ver cuecon')
    conexion.hset("slam", str(numerador()) + '- punkypunch :', ' ver cuecon')
    conexion.hset("slam", str(numerador()) + '- Salao :',
                  ' Persona que tiene mala suerte. Ejm.Mario tuestas saladoen la loteria.')
    conexion.hset("slam", str(numerador()) + '- Sarao :',
                  ' Fiesta o baile organizada generalmente por el segundo ciclo de secundaria. Tipicamente se realiza en horas de la tarde, en el gimnasio de la escuela. Dicese de cualquier fiesta en que el objetivo principal es bailar.')
    conexion.hset("slam", str(numerador()) + '- Solido :', 'Significaexcelente. Tambien chevere.')
    conexion.hset("slam", str(numerador()) + '- Tallao :', 'Bien vestido.')
    conexion.hset("slam", str(numerador()) + '- Tarrantan :', 'Mas que rantan. Muchisimo.')
    conexion.hset("slam", str(numerador()) + '- Tatai :',
                  'Bye, hasta luego, nos vemos.*Ta bien (viene de: esta bien; se le da significado segun la diccion, pronunciacion y el tono de la voz usada por la persona) Algo sorprendente; falso; exagerado; emocionante; todos los significados anteriores a la vez.')
    conexion.hset("slam", str(numerador()) + '- Tella :', 'Botella (generalmente de licor).')
    conexion.hset("slam", str(numerador()) + '- Totuma:  :',
                  'Es un plato que se fabrica partiendo a la mitad unos frutos redondos y duros que crecen en el monte (calabazo).')
    conexion.hset("slam", str(numerador()) + '- Tongo :', ' Policia de bajo rango')
    conexion.hset("slam", str(numerador()) + '- Tonton :', ' Vagina')
    conexion.hset("slam", str(numerador()) + '- Micha :', ' Vagina')
    conexion.hset("slam", str(numerador()) + '- Mota :', ' Vagina')
    conexion.hset("slam", str(numerador()) + '- Trozo :', ' Vagina')
    conexion.hset("slam", str(numerador()) + '- Tortillera :', 'lesbiana')
    conexion.hset("slam", str(numerador()) + '- Trepaquesube/verguero/chuchamadre/zaperoco :',
                  ' gran problema, disturbio, desorden, conflicto')
    conexion.hset("slam", str(numerador()) + '- Verguero :', ' gran problema, disturbio, desorden, conflicto')
    conexion.hset("slam", str(numerador()) + '- Chuchamadre :', ' gran problema, disturbio, desorden, conflicto')
    conexion.hset("slam", str(numerador()) + '- Zaperoco :', ' gran problema, disturbio, desorden, conflicto')
    conexion.hset("slam", str(numerador()) + '- Trueno :', ' Arma de fuego')
    conexion.hset("slam", str(numerador()) + '- Vaca :',
                  ' Colecta de dinero entre varias personas para comprar algo. Hey hagan una vaca pala Carmen ahi...')
    conexion.hset("slam", str(numerador()) + '- Vaina :',
                  ' Utilizado como comodin en conversaciones, usado porcosa(tambien usado en otros paises con el mismo significado).')
    conexion.hset("slam", str(numerador()) + '- Vale cebo :', ' Dicese de una situacion injusta o estupida.')
    conexion.hset("slam", str(numerador()) + '- Vampira :',
                  ' Mujeres de alto mantenimiento, sumamente ignorantes en todo menos en el arte de hacer el amor.')
    conexion.hset("slam", str(numerador()) + '- Chupasangre :',
                  ' Mujeres de alto mantenimiento, sumamente ignorantes en todo menos en el arte de hacer el amor.')
    conexion.hset("slam", str(numerador()) + '- Verguero :',
                  ' Problema, debate discusion acalorada llegando al punto cercano a formarse una trifulca.')
    conexion.hset("slam", str(numerador()) + '- Vidajenear :', ' Husmear, espiar, y entrometerse en la vida ajena.')
    conexion.hset("slam", str(numerador()) + '- Violinista :',
                  ' Persona que acopaña a una pareja pero no debe estar presente pues la pareja quiere arropar. (vease arropar).')
    conexion.hset("slam", str(numerador()) + '- Yapla :',
                  ' playa. sale del reverso de playa, yaspla, y quitandole pla.')
    conexion.hset("slam", str(numerador()) + '- Yeye :',
                  ' Persona adinerada que presume de su condicion, comunmente usa anglicismos en su habla.')
    conexion.hset("slam", str(numerador()) + '- Rabiblanco :',
                  ' Persona adinerada que presume de su condicion, comunmente usa anglicismos en su habla.')
    conexion.hset("slam", str(numerador()) + '- Zambito(a) :',
                  ' expresion de las provincias de Herrera y Los Santos, significaniño o niña.')

    #    print(conexion.get("secuencia"))
    #print(conexion.hgetall("slam"))
    #    print(numerador())







    # MUESTRA VALORES

#print(conexion.hget("slam", "3"))
#print(conexion.hkeys("slam"))
#print(conexion.hvals("slam"))
#print(conexion.hgetall("slam"))

#ELIMINA VALORES
#conexion.hdel("slam", 3)
#print(conexion.hgetall("slam"))

#PARA ACTUALIZACION BORRAMOS LA LLAVE E INSERTAMOS UNA NUEVA
