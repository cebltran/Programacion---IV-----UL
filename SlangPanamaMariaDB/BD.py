import sqlalchemy
from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine('mysql+pymysql://root:Sebasdiances2021@localhost:3307/slam')
base = declarative_base()

class Slam(base):
    __tablename__ = 'slam'

    id = Column(Integer(), primary_key=True)
    EXPRESION = Column(String(150), nullable =False, )
    SIGNIFICADO = Column(String(350), nullable =False,)

    def __str__(self):
            return self.id

Session = sessionmaker(bind=engine)
session = Session()

def Insertadato(palabra , significado):
    slam1 = Slam(EXPRESION=palabra, SIGNIFICADO=significado)
    session.add(slam1)
    session.commit()
    print("")
    print("                                 -->Registro Insertado Con exito")
    print("")
    p=input("Presione una <Enter> para continuar")

def Editadato(palabra , significado, idpalabra):

    session.query(Slam).filter(
        Slam.id == idpalabra
    ).update(
        {
        Slam.EXPRESION: palabra,
        Slam.SIGNIFICADO: significado
        }
    )

    session.commit()



    print("                                 --> Registro Actualizado con Exito")
    print("")
    p = input("Presione una <Enter> para continuar")

def Borradato(idpalabra):
    session.query(Slam).filter(
        Slam.id == idpalabra
    ).delete()

    session.commit()

    print("                                 --> Registro Eliminado con Exito")
    print("")
    p = input("Presione una <Enter> para continuar")

def BuscaDato(palabra, muestra):
    palabra = '%' + palabra + '%'
    slams = session.query(Slam).filter(
        Slam.EXPRESION.like(palabra)
    )
    for slam in slams:
        print(str(slam.id) + '-' + slam.EXPRESION + ' : ' + slam.SIGNIFICADO)
    if muestra == 1:
        print("                                 --> Registros encontrados")
        print("")
        p=input("Presione una <Enter> para continuar")

def CreaBD():
    base.metadata.drop_all(engine)
    base.metadata.create_all(engine)

    slam1 = Slam(EXPRESION='A guanchinche', SIGNIFICADO=' a caballito, cargando a espaldas')
    slam2 = Slam(EXPRESION='A monchinche', SIGNIFICADO=' a caballito, cargando a espaldas')
    slam3 = Slam(EXPRESION='Abuelazón',
                 SIGNIFICADO=' Dícese de la conducta de entusiasmo excesivo que los abuelos sienten por los nietos; actitud típica de personas ancianas.')
    slam4 = Slam(EXPRESION='Agarrar los mangos bajitos', SIGNIFICADO='hacer algo de la forma más facil.')
    slam5 = Slam(EXPRESION='Ahuevado', SIGNIFICADO=' sinónimo de huevón, lento, imbécil')
    slam6 = Slam(EXPRESION='ahuevao', SIGNIFICADO=' sinónimo de huevón, lento, imbécil')
    slam7 = Slam(EXPRESION='Ahuevazón',
                 SIGNIFICADO=' Situacion calificada de ahuevada (situación causada pur una tontera/por un tonto).')
    slam8 = Slam(EXPRESION='Allá adonde uno ', SIGNIFICADO=' El interior.(normalmente pronunciado alla onde uno)')
    slam9 = Slam(EXPRESION='Arrabalero', SIGNIFICADO=' Buscapleitos')
    slam10 = Slam(EXPRESION='Arrabalera', SIGNIFICADO=' Buscapleitos')
    slam11 = Slam(EXPRESION='Arranque', SIGNIFICADO=' Parranda.((de arrancarse [irse de fiesta/a parrandear]))')
    slam12 = Slam(EXPRESION='Arrebatiña, pata y puñete',
                  SIGNIFICADO=' lo que pasa despues que alguien rompe la piñata.')
    slam13 = Slam(EXPRESION='Arrecho',
                  SIGNIFICADO=' persona que esta excitada sexualmente. Persona que puede realizar cualquier trabajo o hazaña(termino utilizado con mayor frecuencia en el interior del país).')
    slam14 = Slam(EXPRESION='Arrecha',
                  SIGNIFICADO=' persona que esta excitada sexualmente. Persona que puede realizar cualquier trabajo o hazaña(termino utilizado con mayor frecuencia en el interior del país).')
    slam15 = Slam(EXPRESION='Arrepinchoso', SIGNIFICADO=' Persona que le gusta el arranque')
    slam16 = Slam(EXPRESION='Arrepinchosa', SIGNIFICADO=' Persona que le gusta el arranque')
    slam17 = Slam(EXPRESION='Arropar',
                  SIGNIFICADO=' hacer el amor con la ropa, comúnmente visto en saraos o en lugares con poca intimidad.')
    slam18 = Slam(EXPRESION='Arroz con Mango', SIGNIFICADO=' Grandes problemas')
    slam19 = Slam(EXPRESION='Trepa que sube', SIGNIFICADO=' Grandes problemas')
    slam20 = Slam(EXPRESION='pandemonio', SIGNIFICADO=' Grandes problemas')
    slam21 = Slam(EXPRESION='Ayala',
                  SIGNIFICADO=' interjección de sorpresa o enojo. Adaptado de Vaya la. Usualmente utilizado con palabras curiosas y soeces. Ejm: Ayala Peste, áyala máquina, áyala vida. (pronunciado también áshala)')
    slam22 = Slam(EXPRESION='Bagre', SIGNIFICADO=' Mujer horrible o poco agraciada físicamente')
    slam23 = Slam(EXPRESION='Cangreja', SIGNIFICADO=' Mujer horrible o poco agraciada físicamente')
    slam24 = Slam(EXPRESION='Gárgola', SIGNIFICADO=' Mujer horrible o poco agraciada físicamente')
    slam25 = Slam(EXPRESION='Cocobola', SIGNIFICADO=' Mujer horrible o poco agraciada físicamente')
    slam26 = Slam(EXPRESION='Baño de pueblo',
                  SIGNIFICADO=' participar de alguna actividad normalmente de tipo folklorica para renovar el espiritu Panameno... irse a un pindin, cantaderas, comer frituras, baile tipico, etc.')
    slam27 = Slam(EXPRESION='Barriada Bruja', SIGNIFICADO='Asentamiento HumanoInformal/ Villa mísera o Favela.')
    slam28 = Slam(EXPRESION='Barrio Brujo', SIGNIFICADO='Asentamiento HumanoInformal/ Villa mísera o Favela.')
    slam29 = Slam(EXPRESION='Bate',
                  SIGNIFICADO='Excusa difícil de creer, o golpe de suerte. Ejm:James Bond es un batoso, me metió un bate; cigarro de Marihuana de gran tamaño')
    slam30 = Slam(EXPRESION='Batería', SIGNIFICADO=' papel con respuestas de un examen')
    slam31 = Slam(EXPRESION='Berraco', SIGNIFICADO=' (sust) persona diestra, hábil; (adj) furioso; (adj) díficil.')
    slam32 = Slam(EXPRESION='Berraca', SIGNIFICADO=' (sust) persona diestra, hábil; (adj) furioso; (adj) díficil.')
    slam33 = Slam(EXPRESION='Berrinche',
                  SIGNIFICADO=' Armar un escándalo o necedad[Ejm. Ese niño tiene un berrinche]. Olor fuerte a orine[Ejm. Este baño huele a berrinche].')
    slam34 = Slam(EXPRESION='Biencuidao',
                  SIGNIFICADO=' Individuo que se gana la vida cuidando autos y consiguiendo estacionamientos en lugares como centros comerciales, discotecas, cines, almacenes.')
    slam35 = Slam(EXPRESION='Birria',
                  SIGNIFICADO=' Juego muy repetitivo sin espiritu de competencia o finalidad alguna, comunmente usado para los videojuegos, futbol o baloncesto.')
    slam36 = Slam(EXPRESION='Blanco', SIGNIFICADO=' cigarrillo')
    slam37 = Slam(EXPRESION='Blazear',
                  SIGNIFICADO=' Ofender.(se utiliza como verbo en infinitivo-gerundio, ej: Juan me estaba blazeando.)')
    slam38 = Slam(EXPRESION='Bochinche', SIGNIFICADO=' chisme.')
    slam39 = Slam(EXPRESION='Borrador', SIGNIFICADO=' Un gran Autobús o Camion.')
    slam40 = Slam(EXPRESION='Bote',
                  SIGNIFICADO=' Pedir que te lleven o te den un aventon a algun lugar (Hey un bote pue).')
    slam41 = Slam(EXPRESION='Botella',
                  SIGNIFICADO=' Persona que cobra pero no trabaja; se da mucho esta situación en sector público panameño.')
    slam42 = Slam(EXPRESION='Bravos de Boston',
                  SIGNIFICADO=' El mejor de una profesión. dedicado a los bravos de boston de 1914.[1]')
    slam43 = Slam(EXPRESION='Brujo', SIGNIFICADO=' barato, de poca calidad.')
    slam44 = Slam(EXPRESION='Gallo', SIGNIFICADO=' barato, de poca calidad.')
    slam45 = Slam(EXPRESION='Buco', SIGNIFICADO=' mucho (galicismo; derivado de beaucoup).')
    slam46 = Slam(EXPRESION='Bueno',
                  SIGNIFICADO=' que esta muy bonita o bonita y tiene buen fisico,[ejm. Mami tas wena]; también pay (como en es un pay).')
    slam47 = Slam(EXPRESION='Buena',
                  SIGNIFICADO=' que esta muy bonita o bonita y tiene buen fisico,[ejm. Mami tas wena]; también pay (como en es un pay).')
    slam48 = Slam(EXPRESION='Bulto',
                  SIGNIFICADO=' Persona que no tiene un buen desempeño de sus funciones, viene de ocupar un espacio determinado siendo irrelevante para la situacion.')
    slam49 = Slam(EXPRESION='Burundanga',
                  SIGNIFICADO='alimento de poco valor nutritivo. Ejm: caramelos, chocolates, chicles, etc...')
    slam50 = Slam(EXPRESION='Cafá', SIGNIFICADO=' Una Palmada fuerte átras en la cabeza.')
    slam51 = Slam(EXPRESION='Camarón',
                  SIGNIFICADO=' actividad extracurricular que permite a un individuo ganar dinero extra. Su origen se remonta a los tiempos en que los gringos le decían a los localesCome around...(pásate por aquí).[Ejm. Voy a hacer un camarón]')
    slam52 = Slam(EXPRESION='Cangreja',
                  SIGNIFICADO=' Mujer de baja categoria que usalmente sale por las noches y no puede caminar normalmente de tanta profesion... baja la marea y suben las cangrejas expresion que se usa cuando cae la noche en Panama.')
    slam53 = Slam(EXPRESION='Chachai', SIGNIFICADO=' Vestido de niña.')
    slam54 = Slam(EXPRESION='Chambón', SIGNIFICADO=' Torpe')
    slam55 = Slam(EXPRESION='Chantin', SIGNIFICADO=' casa, hogar.')
    slam56 = Slam(EXPRESION='Chen chen', SIGNIFICADO=' Dinero')
    slam57 = Slam(EXPRESION='Chequear', SIGNIFICADO=' revisar')
    slam58 = Slam(EXPRESION='Chicha',
                  SIGNIFICADO=' Refresco o bebida fermentada. (Esta palabra, recogida por laRAEy de etimología panameña es usada en Centroamérica, Chile y Perú, con ciertas variaciones)')
    slam59 = Slam(EXPRESION='Chichí',
                  SIGNIFICADO=' 1)Forma cariñosa de decir Bebe; Forma cariñosa de deicirle a novia o novio')
    slam60 = Slam(EXPRESION='Chifear', SIGNIFICADO=' No invitar/ignorar a alguna persona.')
    slam61 = Slam(EXPRESION='Chilin',
                  SIGNIFICADO=' del ingles Chilling estar tranquilo; parkear cool; ejm: estaba parkeando chillin en la chantin.')
    slam62 = Slam(EXPRESION='Chinguear', SIGNIFICADO=' apostar')
    slam63 = Slam(EXPRESION='Chino o Chinito',
                  SIGNIFICADO=' bodega / tienda de abarrotes (dícese porque generalmente están administradas por chinos)')
    slam64 = Slam(EXPRESION='Chiquishow',
                  SIGNIFICADO='Dicese de un espectáculo púgil no programado en el que los combatientes por lo general no saben pelear de forma vistosa. También utilizado para indicar cuando a alguien le hacen un espectaculo frente a otras personas, regularmente realizado por el sexo femenino.')
    slam65 = Slam(EXPRESION='Chirrisco',
                  SIGNIFICADO=' Bebida hecha en casa proveniente comúnmente de la fermentacion y destilacion del maiz o la caña.')
    slam66 = Slam(EXPRESION='Chiva', SIGNIFICADO=' Transporte colectivo de capacidad media')
    slam67 = Slam(EXPRESION='Choborro',
                  SIGNIFICADO=' persona brusca y de poca capacidad para desarrollar una actividad.')
    slam68 = Slam(EXPRESION='Choborra',
                  SIGNIFICADO=' persona brusca y de poca capacidad para desarrollar una actividad.')
    slam69 = Slam(EXPRESION='Cholipay', SIGNIFICADO=' mujer mestiza/indígena atractiva físicamente')
    slam70 = Slam(EXPRESION='Cholo',
                  SIGNIFICADO=' En zonas del interior haciendo referencia a amigo, en la ciudad hace referencia a personas del interior.')
    slam71 = Slam(EXPRESION='Cholometal',
                  SIGNIFICADO=' cholo o indigena que sigue modismos de roqueros, punks y/o heavymetals.')
    slam72 = Slam(EXPRESION='CholoPop',
                  SIGNIFICADO=' un compa que acaba de llegar a la capital vestido como en los 70s, con el pecho afuero y usando essencia de pacholi como perfume.')
    slam73 = Slam(EXPRESION='Cholywood',
                  SIGNIFICADO=' Forma graciosa, despectiva o una manera para definir la farándula panameña.')
    slam74 = Slam(EXPRESION='Chombo', SIGNIFICADO=' persona de raza negra.')
    slam75 = Slam(EXPRESION='Chomba', SIGNIFICADO=' persona de raza negra.')
    slam76 = Slam(EXPRESION='Chonta', SIGNIFICADO=' cabeza')
    slam77 = Slam(EXPRESION='Chota', SIGNIFICADO=' minivan de la policía. También utilizada para referirse a joder.')
    slam78 = Slam(EXPRESION='Chota', SIGNIFICADO=' Policia.')
    slam79 = Slam(EXPRESION='Tongo', SIGNIFICADO=' Policia.')
    slam80 = Slam(EXPRESION='Chuain',
                  SIGNIFICADO=' (de pronunciación rápida) Esta es un sinónimo de Yeye y es una persona acomodada, alta alcurnia, delicada o adinerada.')
    slam81 = Slam(EXPRESION='Chucha',
                  SIGNIFICADO=' Vulva; también usado como interjección (Ejemplo:¡Chucha!, Que chucha me importa!)')
    slam82 = Slam(EXPRESION='Chuchita', SIGNIFICADO=' véaseCongo.[Ejm. Te tan (están) cogiendo de congo!!!]')
    slam83 = Slam(EXPRESION='Chuleta', SIGNIFICADO=' Exclamacion de sorpresa o admiracion')
    slam84 = Slam(EXPRESION='Chupar', SIGNIFICADO=' Ingerir bebidas alcoholicas')
    slam85 = Slam(EXPRESION='Chuzo', SIGNIFICADO=' Ver Chuleta')
    slam86 = Slam(EXPRESION='Cocho',
                  SIGNIFICADO=' Golpe en la cabeza propinado con los nudillos de la mano. ejemplo Te voy a dar un cocho!')
    slam87 = Slam(EXPRESION='Cocoa',
                  SIGNIFICADO=' Cuento o historia relacionada a un suceso o evento, normalmente un bochinche o chisme.')
    slam88 = Slam(EXPRESION='Cinta',
                  SIGNIFICADO=' Cuento o historia relacionada a un suceso o evento, normalmente un bochinche o chisme.')
    slam89 = Slam(EXPRESION='Compa',
                  SIGNIFICADO=' frase cariñosa refiriendose a un campesino o a un compadre... buen amigo.')
    slam90 = Slam(EXPRESION='Conflei',
                  SIGNIFICADO=' Cualquier cereal de cualquier marca que se come en el desayuno, del inglés Corn Flakes')
    slam91 = Slam(EXPRESION='Coscorrón',
                  SIGNIFICADO=' insecto redondo y cafe, golpe dado con los nudillos (vease cocho).(normalmente cocorrón) ')
    slam92 = Slam(EXPRESION='Cuatrera', SIGNIFICADO=' Mujer la cual esta en busca o acecho de algun hombre cazado.')
    slam93 = Slam(EXPRESION='Cueco', SIGNIFICADO='homosexualolesbiana')
    slam94 = Slam(EXPRESION='Cueca', SIGNIFICADO='homosexualolesbiana')
    slam95 = Slam(EXPRESION='Culantro',
                  SIGNIFICADO=' Una bella dama. Proveniente del Segmento Doble Vida del programa televisivo Parecen Noticias. Tambien es una un planta que se utiliza para sazonar la sopa y otros alimentos.')
    slam96 = Slam(EXPRESION='Culear',
                  SIGNIFICADO=' manera vulgar de decir tener relaciones sexuales osexocon una persona .')
    slam97 = Slam(EXPRESION='Culillo', SIGNIFICADO=' miedo, terror o temor a una cosa')
    slam98 = Slam(EXPRESION='ñáñara', SIGNIFICADO=' miedo, terror o temor a una cosa')
    slam99 = Slam(EXPRESION='Culito', SIGNIFICADO=' Ver Pay')
    slam100 = Slam(EXPRESION='Culo', SIGNIFICADO=' Nalgas')
    slam101 = Slam(EXPRESION='Datien', SIGNIFICADO=' traspalante de tienda')
    slam102 = Slam(EXPRESION='De a vaina', SIGNIFICADO=' ganar algo por pura buena suerte en el ultimo momento.')
    slam103 = Slam(EXPRESION='De a vainilla', SIGNIFICADO=' ganar algo por pura buena suerte en el ultimo momento.')
    slam104 = Slam(EXPRESION='por un pelito', SIGNIFICADO=' ganar algo por pura buena suerte en el ultimo momento.')
    slam105 = Slam(EXPRESION='por un cocoazo', SIGNIFICADO=' ganar algo por pura buena suerte en el ultimo momento.')
    slam106 = Slam(EXPRESION='por pura leche', SIGNIFICADO=' ganar algo por pura buena suerte en el ultimo momento.')
    slam107 = Slam(EXPRESION='De agencia ', SIGNIFICADO='nítido, bonito, nuevo')
    slam108 = Slam(EXPRESION='De vez', SIGNIFICADO=' de una vez, en el acto')
    slam109 = Slam(EXPRESION='Diablo rojo',
                   SIGNIFICADO=' Autobus generalmente pintado de varios colores procedente de las escuelas estadounidenses que comúnmente se les llama borradores por el efecto que produce durante una colision.')
    slam110 = Slam(EXPRESION='En tuco',
                   SIGNIFICADO=' Sinonimo quiebra de no tener dinero, hace referencia a cuando un automovil esta montado sobre pedazos de madera, generalmente sin llantas o en reparacion.')
    slam111 = Slam(EXPRESION='En verga',
                   SIGNIFICADO=' Algo de mala calidad, no complaciente al gusto de nadie ese show esta en verga')
    slam112 = Slam(EXPRESION='Falta de todo',
                   SIGNIFICADO=' Versión moderna de la famosa frase venezolana popularizada en los 80 falta de glamour. Significa falta de respeto, falta de ética, falta de elegancia, falta de clase, falta de consideración, falta de... todo.')
    slam113 = Slam(EXPRESION='Ficha', SIGNIFICADO=' persona importante')
    slam114 = Slam(EXPRESION='Filo', SIGNIFICADO=' Arma punzocortante')
    slam115 = Slam(EXPRESION='Flintin',
                   SIGNIFICADO=' Proveniente de el Patois( ver Guari-Guari), referente a una pareja peleando, donde la mujer le tira cosas al hombre, en ingles Jamaiquino(patois) flying things , usado para describir un problema, conflicto o pelea. Yo no quiero flintin con ese man.')
    slam116 = Slam(EXPRESION='Fulo', SIGNIFICADO=' Rubio/a.')
    slam117 = Slam(EXPRESION='Fula', SIGNIFICADO=' Rubio/a.')
    slam118 = Slam(EXPRESION='Fundillo', SIGNIFICADO=' especificamente el orificio anal.')
    slam119 = Slam(EXPRESION='Fuste', SIGNIFICADO=' Nalgas, Trasero.')
    slam120 = Slam(EXPRESION='Gadaca', SIGNIFICADO=' traspalante de. cagada(algo que sale mal de momento)')
    slam121 = Slam(EXPRESION='Gallinero',
                   SIGNIFICADO='la entreda general o area popular de algun evento cultural (concierto) o evento deportivo.')
    slam122 = Slam(EXPRESION='Gallo', SIGNIFICADO=' Barato, de poca calidad; persona sin gracia.')
    slam123 = Slam(EXPRESION='Galla', SIGNIFICADO=' Barato, de poca calidad; persona sin gracia.')
    slam124 = Slam(EXPRESION='Gandoca', SIGNIFICADO=' traspalante de cagando(defecar)')
    slam125 = Slam(EXPRESION='Garnatón', SIGNIFICADO=' Bofetón. *Garnatada normalmente se dice garnatá.')
    slam126 = Slam(EXPRESION='Garnatada', SIGNIFICADO=' Bofetón. *Garnatada normalmente se dice garnatá.')
    slam127 = Slam(EXPRESION='Globito',
                   SIGNIFICADO=' Condon, preservativo; *forrito ha sido popularizado por el homónimo personaje condón del popular programa La Cáscara.')
    slam128 = Slam(EXPRESION='Forrito',
                   SIGNIFICADO=' Condon, preservativo; *forrito ha sido popularizado por el homónimo personaje condón del popular programa La Cáscara.')
    slam129 = Slam(EXPRESION='Golpe de ala',
                   SIGNIFICADO=' aroma intolerable que procede de las exilas... vulg. ver Grajo')
    slam130 = Slam(EXPRESION='Grajo', SIGNIFICADO=' sudor de las exilas sumamente apestoso')
    slam131 = Slam(EXPRESION='Grubeo',
                   SIGNIFICADO=' Estar con una persona por un tiempo o por una noche para pasarla bien y para nada serio o formal.')
    slam132 = Slam(EXPRESION='Grubear',
                   SIGNIFICADO=' Estar con una persona por un tiempo o por una noche para pasarla bien y para nada serio o formal.')
    slam133 = Slam(EXPRESION='Guabazo', SIGNIFICADO=' Gran golpe, usualmente seguido de hematoma de alguna clase.')
    slam134 = Slam(EXPRESION='Guabanazo', SIGNIFICADO=' Gran golpe, usualmente seguido de hematoma de alguna clase.')
    slam135 = Slam(EXPRESION='Guacho',
                   SIGNIFICADO='es una sopa espesa que lleva ñame, yuca, culantro, arroz, verduras y alguna carne, que puede ser res, rabito de puerco o chicharrón. El guacho se sirve tradicionalmente en una totuma, plato que se fabrica partiendo a la mitad unos frutos redondos y duros que crecen en el monte. Tambien siginfica la combinacion de varias cosas.')
    slam136 = Slam(EXPRESION='Guagua', SIGNIFICADO=' se dice de un automóvil muy viejo o en mal estado.')
    slam137 = Slam(EXPRESION='Guapin',
                   SIGNIFICADO=' Saludo que indica que pasa. Del inglésWhat happened? / What is happening?.')
    slam138 = Slam(EXPRESION='Juatapin',
                   SIGNIFICADO=' Saludo que indica que pasa. Del inglésWhat happened? / What is happening?.')
    slam139 = Slam(EXPRESION='Guapote',
                   SIGNIFICADO=' individuo usualmente con poca autoestima que hace mucha fisicultura pero que al final siempre sigue siendo bien FEO')
    slam140 = Slam(EXPRESION='Guari-guari',
                   SIGNIFICADO=' Dialecto de la Provincia de Bocas del Toro, es una mezcla de Español, Francés, Inglés y lenguas indígenas.')
    slam141 = Slam(EXPRESION='Guaro', SIGNIFICADO=' Alcohol; bebiba alcohólica; licor.')
    slam142 = Slam(EXPRESION='Guillado',
                   SIGNIFICADO=' 1.influenciado por alucinógenos 2.emocionado, inspirado. (normalmente se dice guillao) ')
    slam143 = Slam(EXPRESION='Huevear',
                   SIGNIFICADO=' Perder el tiempo de la peor forma.[Ejm. Pónte a trabajá y deja de ta webiando!!!]')
    slam144 = Slam(EXPRESION='Ir al choque', SIGNIFICADO=' ir de frente ante cualquier adversidad.')
    slam145 = Slam(EXPRESION='Joder', SIGNIFICADO=' Bromear, molestar, irritar. Ejm: No jodas!')
    slam146 = Slam(EXPRESION='Juega vivo', SIGNIFICADO=' con astucia, generalmente sin moral, oportunista.')
    slam147 = Slam(EXPRESION='Jugo-e-Policia', SIGNIFICADO=' agua')
    slam148 = Slam(EXPRESION='Kenke', SIGNIFICADO=' Bate de marihuana')
    slam149 = Slam(EXPRESION='la Kenton',
                   SIGNIFICADO=' llave en lucha libre que se usa para amarrar al adversario, usando las piernas, mientras lo repletan de roncabalaos... usalmente esta llave se usa por mujeres que quieren tener hijos obligando al novio a ejacular dentro del vientre... por eso se dice cuidao y te hace la kenton.')
    slam150 = Slam(EXPRESION='Labia',
                   SIGNIFICADO=' Adulación, normalmente para convencer a la persona de cual es la mejor alternativa en una situación dada o para conseguir apoyo de la misma; muy comun en el ambito de la politica.')
    slam151 = Slam(EXPRESION='Láiter', SIGNIFICADO=' Encendedor, anglicismo [de lighter].')
    slam152 = Slam(EXPRESION='Laopé', SIGNIFICADO=' traspalante de pelao (muchacho)')
    slam153 = Slam(EXPRESION='Levante', SIGNIFICADO='Novio/a, quiénes se gustan y tienen química entre ellos.')
    slam154 = Slam(EXPRESION='Limado',
                   SIGNIFICADO=' Dicese de la persona que se encuentra muy cansada luego de trabajar o beber mucho.')
    slam155 = Slam(EXPRESION='Limpio (a)', SIGNIFICADO=' Sin dinero.')
    slam156 = Slam(EXPRESION='Lleca', SIGNIFICADO='traspalantederivado de Calle')
    slam157 = Slam(EXPRESION='Loco',
                   SIGNIFICADO=' Es como se llaman los amigos de cariño. Muy comun entre oriundos de Panamá.')
    slam158 = Slam(EXPRESION='Machiua', SIGNIFICADO=' Mas cholo que un Cholo Pop... usualmente un indigena.')
    slam159 = Slam(EXPRESION='Machigua', SIGNIFICADO=' Mas cholo que un Cholo Pop... usualmente un indigena.')
    slam160 = Slam(EXPRESION='Machihua', SIGNIFICADO=' Mas cholo que un Cholo Pop... usualmente un indigena.')
    slam161 = Slam(EXPRESION='Machoemonte', SIGNIFICADO=' Tipo mas tof que Rambo')
    slam162 = Slam(EXPRESION='Mafá',
                   SIGNIFICADO=' abrebocas de harina (fritura) en forma de trenza; dícese de un enredo, asunto complicado, o personas abrazadas de forma muy afectiva (como mafá).')
    slam163 = Slam(EXPRESION='Maleante', SIGNIFICADO=' Delincuente o persona que quiere ser como los delincuentes.')
    slam164 = Slam(EXPRESION='Manacho',
                   SIGNIFICADO=' Hombre joven de clase obrera, cuerpo atlético y aspecto un poco rudo y muy masculino. Manacha: Lesbiana.')
    slam165 = Slam(EXPRESION='Manzanillo',
                   SIGNIFICADO=' sin personalidad, influenciable con facilidad, también se dice así a los vividores.')
    slam166 = Slam(EXPRESION='Matapuerco o Soplamoco',
                   SIGNIFICADO=' Golpe exagerado y certero, que duele mucho. Nótese que soplamoco es ehn la mejilla.')
    slam167 = Slam(EXPRESION='Me vale verga',
                   SIGNIFICADO=' Situación que no genera ninguna clase de reacción ni de interés en la persona.(vulgar)/un pepino/un comino')
    slam168 = Slam(EXPRESION='Meña',
                   SIGNIFICADO=' jóvenes de la calle de mal hablar y vestir. Denota las últimas 4 letras de la nacionalidad Panameña. También traspalante del tubérculo ñame)')
    slam169 = Slam(EXPRESION='Meto',
                   SIGNIFICADO=' una expresión que denota una frase de admiración y afirmación muy utilizada en la provincia de Chiriquí. En la ciudad de Panamá (sobretodo) ofi.')
    slam170 = Slam(EXPRESION='Millo',
                   SIGNIFICADO=' Palomitas de maíz. Millo viene de la lengua gallega y quiere decir maíz. En Galicia se le llama a las palomitas de maíz, flocos de millo.')
    slam171 = Slam(EXPRESION='Mococoa',
                   SIGNIFICADO=' liquido producido por los miembros nasales, regularmente de color verde, esta se bebe en grandes cantidades usualmente luego de que a uno lo han traicionado (ver quemado) en una relacion se creia seria.')
    slam172 = Slam(EXPRESION='Montado',
                   SIGNIFICADO=' Que tiene buena situación económica. (normalmente se dice montao/a)')
    slam173 = Slam(EXPRESION='Ñamería', SIGNIFICADO=' Locura.')
    slam174 = Slam(EXPRESION='Ñampearse', SIGNIFICADO=' volverse loco/a.')
    slam175 = Slam(EXPRESION='Ñángara',
                   SIGNIFICADO=' forma despectiva de definir a los comunistas o miembros de partido de izquierda o extrema izquierda.')
    slam176 = Slam(EXPRESION='Ñangotado', SIGNIFICADO=' Persona que camina en cuclillas')
    slam177 = Slam(EXPRESION='Añingotado', SIGNIFICADO=' Persona que camina en cuclillas')
    slam178 = Slam(EXPRESION='Ñapa',
                   SIGNIFICADO=' Un regalo que dan cuando se compra algo en un tienda o abarroterria (introducido por los chinos para captar clientes frecuentes).')
    slam179 = Slam(EXPRESION='Ñecks', SIGNIFICADO=' Versión decente de mierda.[Ejm. Te wa (voy a) sacá la ñecks!!!]')
    slam180 = Slam(EXPRESION='Nevera',
                   SIGNIFICADO=' refrigeradora; autobús con aire acondicionado (dícese de los trans-provinciales [ejm: Panamá-David] porque normalmente van a temperaturas muy frías); mujer cuadrada.')
    slam181 = Slam(EXPRESION='No me parece',
                   SIGNIFICADO=' Frase popularmente utilizada para demostrar descontento por algo.')
    slam182 = Slam(EXPRESION='Ñorro ', SIGNIFICADO=' Homosexual/ Ese man es ñorro.')
    slam183 = Slam(EXPRESION='Ofi',
                   SIGNIFICADO=' entendido, OK (acortación de oficial, utilizado para aprobar o recibir aprobación).')
    slam184 = Slam(EXPRESION='Palante', SIGNIFICADO=' reducción derivada depara adelante')
    slam185 = Slam(EXPRESION='Paciero(s)', SIGNIFICADO=' Amigo, generalmente amigos con quienes se comparte parrandas.')
    slam186 = Slam(EXPRESION='Paja', SIGNIFICADO=' masturbarse')
    slam187 = Slam(EXPRESION='Volar Cometa', SIGNIFICADO=' masturbarse')
    slam188 = Slam(EXPRESION='Pajizo',
                   SIGNIFICADO=' persona que se masturba constantemente; persona que muestra debilidad ante una actividad física.[Ejm. Jo! no puedes ni levantar eso... tas pajizo!!!].')
    slam189 = Slam(EXPRESION='Pajiza',
                   SIGNIFICADO=' persona que se masturba constantemente; persona que muestra debilidad ante una actividad física.[Ejm. Jo! no puedes ni levantar eso... tas pajizo!!!].')
    slam190 = Slam(EXPRESION='Paka',
                   SIGNIFICADO=' Cargamento de droga; persona que tiene fardos/mochilas/ bultos [del inglés packs]; referente a cartuchos de balas; delincuente.')
    slam191 = Slam(EXPRESION='Paracaídas', SIGNIFICADO=' persona que acude a una reunión o fiesta sin invitación.')
    slam192 = Slam(EXPRESION='Parapapeo',
                   SIGNIFICADO=' Palabra que describe el baile de las reinas de carnaval. Verbo: parapapear; ejm: está parapapeando. El término se deriva del sonido de las trompetas de una murga: Para pa pá')
    slam193 = Slam(EXPRESION='Parkin', SIGNIFICADO=' Fiesta o reunión entre amigos.')
    slam194 = Slam(EXPRESION='Parquearr',
                   SIGNIFICADO=' Salir con alguien a pasar el rato: parquear con mis amigos; poner a alguien en su sitio Quiso insultarme y lo parqueé. Normalmente la gente dice parquiar.')
    slam195 = Slam(EXPRESION='Patacón',
                   SIGNIFICADO=' Popular acompañamiento de comida, el cual consiste en rodajas deplátanoaplastadas y luego fritas.')
    slam196 = Slam(EXPRESION='Pataconcito',
                   SIGNIFICADO=' Pequeña acumulación de basura, viene del relleno sanitario de la ciudad de Panamá (Cerro Patacón).')
    slam197 = Slam(EXPRESION='Patatús', SIGNIFICADO=' Desmayo, ataque cardíaco')
    slam198 = Slam(EXPRESION='Pati-amarillo', SIGNIFICADO=' Cigarrillo con el filtro de color amarillo o anaranjado.')
    slam199 = Slam(EXPRESION='Pato ', SIGNIFICADO=' ver sacalodo, tutifruti, punky-punch ...i.e. homosexual')
    slam200 = Slam(EXPRESION='ñorro', SIGNIFICADO=' ver sacalodo, tutifruti, punky-punch ...i.e. homosexual')
    slam201 = Slam(EXPRESION=' ñaño', SIGNIFICADO=' ver sacalodo, tutifruti, punky-punch ...i.e. homosexual')
    slam202 = Slam(EXPRESION='Pebre', SIGNIFICADO=' comida')
    slam203 = Slam(EXPRESION='refine', SIGNIFICADO=' comida')
    slam204 = Slam(EXPRESION='Pelo pelo', SIGNIFICADO=' Baile erótico')
    slam205 = Slam(EXPRESION='Pelonera',
                   SIGNIFICADO=' Golpiza propiciada entre varios sin ser fuerte, comúnmente en la cebeza y en la secundaria.')
    slam206 = Slam(EXPRESION='Perro',
                   SIGNIFICADO=' Despectivo utilizado como sinónimo de mujeriego; usado como insulto.')
    slam207 = Slam(EXPRESION='Perron',
                   SIGNIFICADO=' Persona de poca capacidad. Dicese de una persona que no es muy popular dentro de un circulo')
    slam208 = Slam(EXPRESION='Perrón',
                   SIGNIFICADO=' Persona que no desempeña bien una funcion referenciada o exageracion de perro.')
    slam209 = Slam(EXPRESION='Pescuezona', SIGNIFICADO=' cerveza de botella tamaño grande.')
    slam210 = Slam(EXPRESION='Peso',
                   SIGNIFICADO=' Moneda de 50 centavos, viene del periodo de la separación de Panama de Colombia donde equivalía el peso colombiano a 50 centavos de dólar; usado comúnmente en las peleas de gallos para cuantificar las apuestas.')
    slam211 = Slam(EXPRESION='Picando',
                   SIGNIFICADO=' algo que está de moda.(Su uso se debe al famoso baile del pique, en Panamá.)')
    slam212 = Slam(EXPRESION='Pichi', SIGNIFICADO=' Droga, dícese comúnmente a la cocaina')
    slam213 = Slam(EXPRESION='Piedra', SIGNIFICADO=' crack (droga).')
    slam214 = Slam(EXPRESION='Piedrero',
                   SIGNIFICADO=' persona drogadicta que ha llegado a la indigencia por ser drogadicto.')
    slam215 = Slam(EXPRESION='Piedrera',
                   SIGNIFICADO=' persona drogadicta que ha llegado a la indigencia por ser drogadicto.')
    slam216 = Slam(EXPRESION='Pilar', SIGNIFICADO=' estudiar con afón; pilón(a) es alguien muy estudiso o sabelotodo.')
    slam217 = Slam(EXPRESION='Pilinqui', SIGNIFICADO=' Persona mezquina.')
    slam218 = Slam(EXPRESION='Pillar',
                   SIGNIFICADO=' Synonimo de tomar/coger/Agarrar, ejm: pilla la pluma...; encontrar a hurtadillas una situacion o ver algo en especial.')
    slam219 = Slam(EXPRESION='Pinta', SIGNIFICADO=' cerveza')
    slam220 = Slam(EXPRESION='Fría', SIGNIFICADO=' cerveza')
    slam221 = Slam(EXPRESION='Pipí', SIGNIFICADO=' pene, miembro viril; orine.')
    slam222 = Slam(EXPRESION='Plena',
                   SIGNIFICADO=' Usado para canciones/ritmos dereggaepero también usada para otros géneros cuando la cancion es buena.')
    slam223 = Slam(EXPRESION='Ponchar', SIGNIFICADO=' desinflar; tener sexo; sacar a un bateador por out en béisbol.')
    slam224 = Slam(EXPRESION='Ponchera', SIGNIFICADO=' Desorden, algarabía.')
    slam225 = Slam(EXPRESION='Porcón', SIGNIFICADO=' Entiéndase popcon o palomitas de mais')
    slam226 = Slam(EXPRESION='Millo', SIGNIFICADO=' Entiéndase popcon o palomitas de mais')
    slam227 = Slam(EXPRESION='Praka praka', SIGNIFICADO=' Derivacion de Rakataca.')
    slam228 = Slam(EXPRESION='Puesto Quemado', SIGNIFICADO=' Puesto reservado')
    slam229 = Slam(EXPRESION='qué Bate',
                   SIGNIFICADO=' usado como descripción de algo ficticio, asombroso o espectacular')
    slam230 = Slam(EXPRESION='que es lo que es', SIGNIFICADO=' que hay de nuevo. (pronunciado que lo que é o queloqué)')
    slam231 = Slam(EXPRESION='Qué xopá', SIGNIFICADO='traspalante, derivado de¿qué paso?')
    slam232 = Slam(EXPRESION='Quemado',
                   SIGNIFICADO=' Persona a la cual su novio/novia esposo/esposa lo ha traicionado con otra/o.')
    slam233 = Slam(EXPRESION='Queso', SIGNIFICADO=' Cierta atracción meramente física y sexual.')
    slam234 = Slam(EXPRESION='Rakataca',
                   SIGNIFICADO=' hombe o mujer sin clase, comunmente utiliza mayormente la jerga panameña autoctona. Derivado del sonido de las metralletas al disparar rakatakatakatakataka popularizado durante una canción del grupo Jam & Suppose en 1992: Camión lleno de gun.')
    slam235 = Slam(EXPRESION='Rambulero',
                   SIGNIFICADO=' Persona usualmente de los barrios populares que gusta de las peleas, intrigas, chismes, baile y otras manifestaciones de comunicación sin clase.')
    slam236 = Slam(EXPRESION='Rangálido', SIGNIFICADO=' de mal aspecto, flaco')
    slam237 = Slam(EXPRESION='Rantan', SIGNIFICADO=' Mucho.')
    slam238 = Slam(EXPRESION='Real',
                   SIGNIFICADO=' Moneda de 5 centésimos de balboa. La palabra viene de la época de la colonia en la cual se le denominaba Real a las monedas acuñadas en Potosí, Lima y en algunos otros lugares. En Taboga, Panamá, por ejemplo una familia llegó a encontrar una cantidad de monedas de denominación de pesos de 8 reales, mientras construían su casa.')
    slam239 = Slam(EXPRESION='Pau Pau',
                   SIGNIFICADO=' Castigo a los hijos, ya sea darles con la correa (rejera) o con nalgadas (pau pau).')
    slam240 = Slam(EXPRESION='Rejera',
                   SIGNIFICADO=' Castigo a los hijos, ya sea darles con la correa (rejera) o con nalgadas (pau pau).')
    slam241 = Slam(EXPRESION='Rejeros',
                   SIGNIFICADO=' Grupos de hombres (amigos entre sí) que van a una discoteca, clubes nocturnos o fiesta a ligarse con mujeres o que simplemente se reúnen para pasarla bien. También se reúnen en un casa para libar licor y echar historias u apspectos personales que le han pasado. El programa de Humor de la Cascara hizo una parodia de esto.')
    slam242 = Slam(EXPRESION='Rejo', SIGNIFICADO=' azote, pene.')
    slam243 = Slam(EXPRESION='Reventar', SIGNIFICADO=' vacilar, tomar el tiempo.')
    slam244 = Slam(EXPRESION='Detonar', SIGNIFICADO=' vacilar, tomar el tiempo.')
    slam245 = Slam(EXPRESION='Romper', SIGNIFICADO=' vacilar, tomar el tiempo.')
    slam246 = Slam(EXPRESION='Rompe pecho', SIGNIFICADO=' una Botella de cerveza muy grande.')
    slam247 = Slam(EXPRESION='Manga larga', SIGNIFICADO=' una Botella de cerveza muy grande.')
    slam248 = Slam(EXPRESION='Roncabalao', SIGNIFICADO='Golpe exagerado capaz de matar a una persona.')
    slam249 = Slam(EXPRESION='Sabrosón',
                   SIGNIFICADO=' Algo o alguien que se encuentre en excelentes condiciones o algún evento agradable.')
    slam250 = Slam(EXPRESION='Sacalodo', SIGNIFICADO=' ver cuecon')
    slam251 = Slam(EXPRESION='tutifruti', SIGNIFICADO=' ver cuecon')
    slam252 = Slam(EXPRESION='punkypunch', SIGNIFICADO=' ver cuecon')
    slam253 = Slam(EXPRESION='Salao',
                   SIGNIFICADO=' Persona que tiene mala suerte. Ejm.Mario tuestás saladoen la lotería.')
    slam254 = Slam(EXPRESION='Sarao',
                   SIGNIFICADO=' Fiesta o baile organizada generalmente por el segundo ciclo de secundaria. Típicamente se realiza en horas de la tarde, en el gimnasio de la escuela. Dícese de cualquier fiesta en que el objetivo principal es bailar.')
    slam255 = Slam(EXPRESION='Sólido', SIGNIFICADO='Significaexcelente. También chévere.')
    slam256 = Slam(EXPRESION='Tallao', SIGNIFICADO='Bien vestido.')
    slam257 = Slam(EXPRESION='Tarrantan', SIGNIFICADO='Más que rantan. Muchísimo.')
    slam258 = Slam(EXPRESION='Tatai',
                   SIGNIFICADO='Bye, hasta luego, nos vemos.*Tá bien (viene de: está bien; se le da significado según la dicción, pronunciación y el tono de la voz usada por la persona) Algo sorprendente; falso; exagerado; emocionante; todos los significados anteriores a la vez.')
    slam259 = Slam(EXPRESION='Tella', SIGNIFICADO='Botella (generalmente de licor).')
    slam260 = Slam(EXPRESION='Totuma: ',
                   SIGNIFICADO='Es un plato que se fabrica partiendo a la mitad unos frutos redondos y duros que crecen en el monte (calabazo).')
    slam261 = Slam(EXPRESION='Tongo', SIGNIFICADO=' Policia de bajo rango')
    slam262 = Slam(EXPRESION='Tontón', SIGNIFICADO=' Vagina')
    slam263 = Slam(EXPRESION='Micha', SIGNIFICADO=' Vagina')
    slam264 = Slam(EXPRESION='Mota', SIGNIFICADO=' Vagina')
    slam265 = Slam(EXPRESION='Trozo', SIGNIFICADO=' Vagina')
    slam266 = Slam(EXPRESION='Tortillera', SIGNIFICADO='lesbiana')
    slam267 = Slam(EXPRESION='Trepaquesube/verguero/chuchamadre/zaperoco',
                   SIGNIFICADO=' gran problema, disturbio, desorden, conflicto')
    slam268 = Slam(EXPRESION='Verguero', SIGNIFICADO=' gran problema, disturbio, desorden, conflicto')
    slam269 = Slam(EXPRESION='Chuchamadre', SIGNIFICADO=' gran problema, disturbio, desorden, conflicto')
    slam270 = Slam(EXPRESION='Zaperoco', SIGNIFICADO=' gran problema, disturbio, desorden, conflicto')
    slam271 = Slam(EXPRESION='Trueno', SIGNIFICADO=' Arma de fuego')
    slam272 = Slam(EXPRESION='Vaca',
                   SIGNIFICADO=' Colecta de dinero entre varias personas para comprar algo. Hey hagan una vaca pala Carmen ahí...')
    slam273 = Slam(EXPRESION='Vaina',
                   SIGNIFICADO=' Utilizado como comodín en conversaciones, usado porcosa(también usado en otros países con el mismo significado).')
    slam274 = Slam(EXPRESION='Vale cebo', SIGNIFICADO=' Dícese de una situación injusta o estúpida.')
    slam275 = Slam(EXPRESION='Vampira',
                   SIGNIFICADO=' Mujeres de alto mantenimiento, sumamente ignorantes en todo menos en el arte de hacer el amor.')
    slam276 = Slam(EXPRESION='Chupasangre',
                   SIGNIFICADO=' Mujeres de alto mantenimiento, sumamente ignorantes en todo menos en el arte de hacer el amor.')
    slam277 = Slam(EXPRESION='Vergüero',
                   SIGNIFICADO=' Problema, debate discusion acalorada llegando al punto cercano a formarse una trifulca.')
    slam278 = Slam(EXPRESION='Vidajenear', SIGNIFICADO=' Husmear, espiar, y entrometerse en la vida ajena.')
    slam279 = Slam(EXPRESION='Violinista',
                   SIGNIFICADO=' Persona que acopaña a una pareja pero no debe estar presente pues la pareja quiere arropar. (veáse arropar).')
    slam280 = Slam(EXPRESION='Yapla', SIGNIFICADO=' playa. sale del reverso de playa, yaspla, y quitándole pla.')
    slam281 = Slam(EXPRESION='Yeye',
                   SIGNIFICADO=' Persona adinerada que presume de su condición, comúnmente usa anglicismos en su habla.')
    slam282 = Slam(EXPRESION='Rabiblanco',
                   SIGNIFICADO=' Persona adinerada que presume de su condición, comúnmente usa anglicismos en su habla.')
    slam283 = Slam(EXPRESION='Zambito(a)',
                   SIGNIFICADO=' expresión de las provincias de Herrera y Los Santos, significaniño o niña.')

    session.add(slam1)
    session.add(slam2)
    session.add(slam3)
    session.add(slam4)
    session.add(slam5)
    session.add(slam6)
    session.add(slam7)
    session.add(slam8)
    session.add(slam9)
    session.add(slam10)
    session.add(slam11)
    session.add(slam12)
    session.add(slam13)
    session.add(slam14)
    session.add(slam15)
    session.add(slam16)
    session.add(slam17)
    session.add(slam18)
    session.add(slam19)
    session.add(slam20)
    session.add(slam21)
    session.add(slam22)
    session.add(slam23)
    session.add(slam24)
    session.add(slam25)
    session.add(slam26)
    session.add(slam27)
    session.add(slam28)
    session.add(slam29)
    session.add(slam30)
    session.add(slam31)
    session.add(slam32)
    session.add(slam33)
    session.add(slam34)
    session.add(slam35)
    session.add(slam36)
    session.add(slam37)
    session.add(slam38)
    session.add(slam39)
    session.add(slam40)
    session.add(slam41)
    session.add(slam42)
    session.add(slam43)
    session.add(slam44)
    session.add(slam45)
    session.add(slam46)
    session.add(slam47)
    session.add(slam48)
    session.add(slam49)
    session.add(slam50)
    session.add(slam51)
    session.add(slam52)
    session.add(slam53)
    session.add(slam54)
    session.add(slam55)
    session.add(slam56)
    session.add(slam57)
    session.add(slam58)
    session.add(slam59)
    session.add(slam60)
    session.add(slam61)
    session.add(slam62)
    session.add(slam63)
    session.add(slam64)
    session.add(slam65)
    session.add(slam66)
    session.add(slam67)
    session.add(slam68)
    session.add(slam69)
    session.add(slam70)
    session.add(slam71)
    session.add(slam72)
    session.add(slam73)
    session.add(slam74)
    session.add(slam75)
    session.add(slam76)
    session.add(slam77)
    session.add(slam78)
    session.add(slam79)
    session.add(slam80)
    session.add(slam81)
    session.add(slam82)
    session.add(slam83)
    session.add(slam84)
    session.add(slam85)
    session.add(slam86)
    session.add(slam87)
    session.add(slam88)
    session.add(slam89)
    session.add(slam90)
    session.add(slam91)
    session.add(slam92)
    session.add(slam93)
    session.add(slam94)
    session.add(slam95)
    session.add(slam96)
    session.add(slam97)
    session.add(slam98)
    session.add(slam99)
    session.add(slam100)
    session.add(slam101)
    session.add(slam102)
    session.add(slam103)
    session.add(slam104)
    session.add(slam105)
    session.add(slam106)
    session.add(slam107)
    session.add(slam108)
    session.add(slam109)
    session.add(slam110)
    session.add(slam111)
    session.add(slam112)
    session.add(slam113)
    session.add(slam114)
    session.add(slam115)
    session.add(slam116)
    session.add(slam117)
    session.add(slam118)
    session.add(slam119)
    session.add(slam120)
    session.add(slam121)
    session.add(slam122)
    session.add(slam123)
    session.add(slam124)
    session.add(slam125)
    session.add(slam126)
    session.add(slam127)
    session.add(slam128)
    session.add(slam129)
    session.add(slam130)
    session.add(slam131)
    session.add(slam132)
    session.add(slam133)
    session.add(slam134)
    session.add(slam135)
    session.add(slam136)
    session.add(slam137)
    session.add(slam138)
    session.add(slam139)
    session.add(slam140)
    session.add(slam141)
    session.add(slam142)
    session.add(slam143)
    session.add(slam144)
    session.add(slam145)
    session.add(slam146)
    session.add(slam147)
    session.add(slam148)
    session.add(slam149)
    session.add(slam150)
    session.add(slam151)
    session.add(slam152)
    session.add(slam153)
    session.add(slam154)
    session.add(slam155)
    session.add(slam156)
    session.add(slam157)
    session.add(slam158)
    session.add(slam159)
    session.add(slam160)
    session.add(slam161)
    session.add(slam162)
    session.add(slam163)
    session.add(slam164)
    session.add(slam165)
    session.add(slam166)
    session.add(slam167)
    session.add(slam168)
    session.add(slam169)
    session.add(slam170)
    session.add(slam171)
    session.add(slam172)
    session.add(slam173)
    session.add(slam174)
    session.add(slam175)
    session.add(slam176)
    session.add(slam177)
    session.add(slam178)
    session.add(slam179)
    session.add(slam180)
    session.add(slam181)
    session.add(slam182)
    session.add(slam183)
    session.add(slam184)
    session.add(slam185)
    session.add(slam186)
    session.add(slam187)
    session.add(slam188)
    session.add(slam189)
    session.add(slam190)
    session.add(slam191)
    session.add(slam192)
    session.add(slam193)
    session.add(slam194)
    session.add(slam195)
    session.add(slam196)
    session.add(slam197)
    session.add(slam198)
    session.add(slam199)
    session.add(slam200)
    session.add(slam201)
    session.add(slam202)
    session.add(slam203)
    session.add(slam204)
    session.add(slam205)
    session.add(slam206)
    session.add(slam207)
    session.add(slam208)
    session.add(slam209)
    session.add(slam210)
    session.add(slam211)
    session.add(slam212)
    session.add(slam213)
    session.add(slam214)
    session.add(slam215)
    session.add(slam216)
    session.add(slam217)
    session.add(slam218)
    session.add(slam219)
    session.add(slam220)
    session.add(slam221)
    session.add(slam222)
    session.add(slam223)
    session.add(slam224)
    session.add(slam225)
    session.add(slam226)
    session.add(slam227)
    session.add(slam228)
    session.add(slam229)
    session.add(slam230)
    session.add(slam231)
    session.add(slam232)
    session.add(slam233)
    session.add(slam234)
    session.add(slam235)
    session.add(slam236)
    session.add(slam237)
    session.add(slam238)
    session.add(slam239)
    session.add(slam240)
    session.add(slam241)
    session.add(slam242)
    session.add(slam243)
    session.add(slam244)
    session.add(slam245)
    session.add(slam246)
    session.add(slam247)
    session.add(slam248)
    session.add(slam249)
    session.add(slam250)
    session.add(slam251)
    session.add(slam252)
    session.add(slam253)
    session.add(slam254)
    session.add(slam255)
    session.add(slam256)
    session.add(slam257)
    session.add(slam258)
    session.add(slam259)
    session.add(slam260)
    session.add(slam261)
    session.add(slam262)
    session.add(slam263)
    session.add(slam264)
    session.add(slam265)
    session.add(slam266)
    session.add(slam267)
    session.add(slam268)
    session.add(slam269)
    session.add(slam270)
    session.add(slam271)
    session.add(slam272)
    session.add(slam273)
    session.add(slam274)
    session.add(slam275)
    session.add(slam276)
    session.add(slam277)
    session.add(slam278)
    session.add(slam279)
    session.add(slam280)
    session.add(slam281)
    session.add(slam282)
    session.add(slam283)

    session.commit()
    print("")
    print("                                 -->Base de datos Creada y se insertaron los registros de inicio")
    print("")
    p=input("Presione una <Enter> para continuar")




