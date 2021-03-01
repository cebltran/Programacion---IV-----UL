import sqlite3


def Insertadato(palabra , significado):
    conn = sqlite3.connect('slam.db')
    strsql = "insert into SLAM (id, expresion, significado) values (null,'" + palabra + "','" + significado + "')"

    conn.execute(strsql)
    conn.commit()
    print("")
    print("                                 -->Registro Insertado Con exito")
    print("")
    p=input("Presione una <Enter> para continuar")
    conn.close()

def Editadato(palabra , significado, idpalabra):
    conn = sqlite3.connect('slam.db')
    strsql = "update SLAM set expresion = '" + palabra + "', significado = '" + significado + "' where id = " + str(idpalabra)
    conn.execute(strsql)
    conn.commit()
    print("                                 --> Registro Actualizado con Exito")
    print("")
    p = input("Presione una <Enter> para continuar")
    conn.close()

def Borradato(idpalabra):
    conn = sqlite3.connect('slam.db')
    strsql = "delete from  SLAM where id = " + str(idpalabra)
    conn.execute(strsql)
    conn.commit()
    print("                                 --> Registro Eliminado con Exito")
    print("")
    p = input("Presione una <Enter> para continuar")
    conn.close()

def BuscaDato(palabra, muestra):
    conn = sqlite3.connect('slam.db')
    cursor = conn.cursor()
    strsql = "SELECT ID,Expresion, significado FROM SLAM where EXPRESION like '%" + palabra + "%'"
    cursor.execute(strsql)
    datos = cursor.fetchall()
    print("")
    for dato in datos:
            print (dato)
    if muestra == 1:
        print("                                 --> Registros encontrados")
        print("")
        p=input("Presione una <Enter> para continuar")

    conn.close()

def CreaBD():
    conn = sqlite3.connect('slam.db')
    consulta = conn.execute("select coalesce(1,0) existe from sqlite_master where name = 'SLAM'")
    for c in consulta:
        if c[0] == 1:
            conn.execute('''DROP TABLE SLAM''')

    conn.execute('''CREATE TABLE SLAM
            (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            EXPRESION TEXT NOT NULL,
            SIGNIFICADO TEXT NOT NULL)''')

    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'A GUANCHINCHE',' A CABALLITO, CARGANDO A ESPALDAS')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'A MONCHINCHE',' A CABALLITO, CARGANDO A ESPALDAS')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ABUELAZÓN ',' DÍCESE DE LA CONDUCTA DE ENTUSIASMO EXCESIVO QUE LOS ABUELOS SIENTEN POR LOS NIETOS; ACTITUD TÍPICA DE PERSONAS ANCIANAS.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'AGARRAR LOS MANGOS BAJITOS',' HACER ALGO DE LA FORMA MÁS FACIL.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'AHUEVADO',' SINÓNIMO DE HUEVÓN, LENTO, IMBÉCIL')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'AHUEVAO',' SINÓNIMO DE HUEVÓN, LENTO, IMBÉCIL')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'AHUEVAZÓN',' SITUACION CALIFICADA DE AHUEVADA (SITUACIÓN CAUSADA PUR UNA TONTERA/POR UN TONTO).')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ALLÁ ADONDE UNO ',' EL INTERIOR.(NORMALMENTE PRONUNCIADO ALLA ONDE UNO) ')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ARRABALERO',' BUSCAPLEITOS')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ARRABALERA',' BUSCAPLEITOS')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ARRANQUE',' PARRANDA.((DE ARRANCARSE [IRSE DE FIESTA/A PARRANDEAR]) )')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ARREBATIÑA, PATA Y PUÑETE ',' LO QUE PASA DESPUES QUE ALGUIEN ROMPE LA PIÑATA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ARRECHO',' PERSONA QUE ESTA EXCITADA SEXUALMENTE. PERSONA QUE PUEDE REALIZAR CUALQUIER TRABAJO O HAZAÑA(TERMINO UTILIZADO CON MAYOR FRECUENCIA EN EL INTERIOR DEL PAÍS).')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ARRECHA ',' PERSONA QUE ESTA EXCITADA SEXUALMENTE. PERSONA QUE PUEDE REALIZAR CUALQUIER TRABAJO O HAZAÑA(TERMINO UTILIZADO CON MAYOR FRECUENCIA EN EL INTERIOR DEL PAÍS).')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ARREPINCHOSO ',' PERSONA QUE LE GUSTA EL ARRANQUE')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ARREPINCHOSA ',' PERSONA QUE LE GUSTA EL ARRANQUE')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ARROPAR',' HACER EL AMOR CON LA ROPA, COMÚNMENTE VISTO EN SARAOS O EN LUGARES CON POCA INTIMIDAD.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ARROZ CON MANGO',' GRANDES PROBLEMAS')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'TREPA QUE SUBE',' GRANDES PROBLEMAS')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PANDEMONIO',' GRANDES PROBLEMAS')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'AYALA ',' INTERJECCIÓN DE SORPRESA O ENOJO. ADAPTADO DE VAYA LA. USUALMENTE UTILIZADO CON PALABRAS CURIOSAS Y SOECES. EJM: AYALA PESTE, ÁYALA MÁQUINA, ÁYALA VIDA. (PRONUNCIADO TAMBIÉN ÁSHALA)')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BAGRE',' MUJER HORRIBLE O POCO AGRACIADA FÍSICAMENTE')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CANGREJA',' MUJER HORRIBLE O POCO AGRACIADA FÍSICAMENTE')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GÁRGOLA',' MUJER HORRIBLE O POCO AGRACIADA FÍSICAMENTE')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'COCOBOLA',' MUJER HORRIBLE O POCO AGRACIADA FÍSICAMENTE')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BAÑO DE PUEBLO ',' PARTICIPAR DE ALGUNA ACTIVIDAD NORMALMENTE DE TIPO FOLKLORICA PARA RENOVAR EL ESPIRITU PANAMENO... IRSE A UN PINDIN, CANTADERAS, COMER FRITURAS, BAILE TIPICO, ETC.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BARRIADA BRUJA',' ASENTAMIENTO HUMANO INFORMAL/ VILLA MÍSERA O FAVELA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BARRIO BRUJO ',' ASENTAMIENTO HUMANO INFORMAL/ VILLA MÍSERA O FAVELA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BATE','EXCUSA DIFÍCIL DE CREER, O GOLPE DE SUERTE. EJM:JAMES BOND ES UN BATOSO, ME METIÓ UN BATE; CIGARRO DE MARIHUANA DE GRAN TAMAÑO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BATERÍA ',' PAPEL CON RESPUESTAS DE UN EXAMEN')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BERRACO',' (SUST) PERSONA DIESTRA, HÁBIL; (ADJ) FURIOSO; (ADJ) DÍFICIL.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BERRACA',' (SUST) PERSONA DIESTRA, HÁBIL; (ADJ) FURIOSO; (ADJ) DÍFICIL.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BERRINCHE ',' ARMAR UN ESCÁNDALO O NECEDAD [EJM. ESE NIÑO TIENE UN BERRINCHE]. OLOR FUERTE A ORINE [EJM. ESTE BAÑO HUELE A BERRINCHE].')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BIENCUIDAO ',' INDIVIDUO QUE SE GANA LA VIDA CUIDANDO AUTOS Y CONSIGUIENDO ESTACIONAMIENTOS EN LUGARES COMO CENTROS COMERCIALES, DISCOTECAS, CINES, ALMACENES.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BIRRIA ',' JUEGO MUY REPETITIVO SIN ESPIRITU DE COMPETENCIA O FINALIDAD ALGUNA, COMUNMENTE USADO PARA LOS VIDEOJUEGOS, FUTBOL O BALONCESTO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BLANCO ',' CIGARRILLO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BLAZEAR',' OFENDER.(SE UTILIZA COMO VERBO EN INFINITIVO-GERUNDIO, EJ: JUAN ME ESTABA BLAZEANDO.)')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BOCHINCHE',' CHISME.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BORRADOR',' UN GRAN AUTOBÚS O CAMION.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BOTE',' PEDIR QUE TE LLEVEN O TE DEN UN AVENTON A ALGUN LUGAR (HEY UN BOTE PUE).')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BOTELLA ',' PERSONA QUE COBRA PERO NO TRABAJA; SE DA MUCHO ESTA SITUACIÓN EN SECTOR PÚBLICO PANAMEÑO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BRAVOS DE BOSTON ',' EL MEJOR DE UNA PROFESIÓN. DEDICADO A LOS BRAVOS DE BOSTON DE 1914. [1]')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BRUJO',' BARATO, DE POCA CALIDAD.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GALLO ',' BARATO, DE POCA CALIDAD.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BUCO ',' MUCHO (GALICISMO; DERIVADO DE BEAUCOUP).')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BUENO',' QUE ESTA MUY BONITA O BONITA Y TIENE BUEN FISICO, [EJM. MAMI TAS WENA]; TAMBIÉN PAY (COMO EN ES UN PAY).')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BUENA',' QUE ESTA MUY BONITA O BONITA Y TIENE BUEN FISICO, [EJM. MAMI TAS WENA]; TAMBIÉN PAY (COMO EN ES UN PAY).')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BULTO',' PERSONA QUE NO TIENE UN BUEN DESEMPEÑO DE SUS FUNCIONES, VIENE DE OCUPAR UN ESPACIO DETERMINADO SIENDO IRRELEVANTE PARA LA SITUACION.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BURUNDANGA','ALIMENTO DE POCO VALOR NUTRITIVO. EJM: CARAMELOS, CHOCOLATES, CHICLES, ETC...')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CAFÁ ',' UNA PALMADA FUERTE ÁTRAS EN LA CABEZA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CAMARÓN',' ACTIVIDAD EXTRACURRICULAR QUE PERMITE A UN INDIVIDUO GANAR DINERO EXTRA. SU ORIGEN SE REMONTA A LOS TIEMPOS EN QUE LOS GRINGOS LE DECÍAN A LOS LOCALES COME AROUND... (PÁSATE POR AQUÍ). [EJM. VOY A HACER UN CAMARÓN]')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CANGREJA ',' MUJER DE BAJA CATEGORIA QUE USALMENTE SALE POR LAS NOCHES Y NO PUEDE CAMINAR NORMALMENTE DE TANTA PROFESION... BAJA LA MAREA Y SUBEN LAS CANGREJAS EXPRESION QUE SE USA CUANDO CAE LA NOCHE EN PANAMA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHACHAI ',' VESTIDO DE NIÑA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHAMBÓN ',' TORPE')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHANTIN ',' CASA, HOGAR.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHEN CHEN ',' DINERO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHEQUEAR',' REVISAR')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHICHA ',' REFRESCO O BEBIDA FERMENTADA. (ESTA PALABRA, RECOGIDA POR LA RAE Y DE ETIMOLOGÍA PANAMEÑA ES USADA EN CENTROAMÉRICA, CHILE Y PERÚ, CON CIERTAS VARIACIONES)')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHICHÍ ',' 1)FORMA CARIÑOSA DE DECIR BEBE; FORMA CARIÑOSA DE DEICIRLE A NOVIA O NOVIO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHIFEAR ',' NO INVITAR/IGNORAR A ALGUNA PERSONA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHILIN ',' DEL INGLES CHILLING ESTAR TRANQUILO; PARKEAR COOL; EJM: ESTABA PARKEANDO CHILLIN EN LA CHANTIN.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHINGUEAR ',' APOSTAR')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHINO O CHINITO ',' BODEGA / TIENDA DE ABARROTES (DÍCESE PORQUE GENERALMENTE ESTÁN ADMINISTRADAS POR CHINOS)')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHIQUISHOW',' DICESE DE UN ESPECTÁCULO PÚGIL NO PROGRAMADO EN EL QUE LOS COMBATIENTES POR LO GENERAL NO SABEN PELEAR DE FORMA VISTOSA. TAMBIÉN UTILIZADO PARA INDICAR CUANDO A ALGUIEN LE HACEN UN ESPECTACULO FRENTE A OTRAS PERSONAS, REGULARMENTE REALIZADO POR EL SEXO FEMENINO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHIRRISCO ',' BEBIDA HECHA EN CASA PROVENIENTE COMÚNMENTE DE LA FERMENTACION Y DESTILACION DEL MAIZ O LA CAÑA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHIVA ',' TRANSPORTE COLECTIVO DE CAPACIDAD MEDIA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHOBORRO',' PERSONA BRUSCA Y DE POCA CAPACIDAD PARA DESARROLLAR UNA ACTIVIDAD.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHOBORRA',' PERSONA BRUSCA Y DE POCA CAPACIDAD PARA DESARROLLAR UNA ACTIVIDAD.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHOLIPAY ',' MUJER MESTIZA/INDÍGENA ATRACTIVA FÍSICAMENTE')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHOLO',' EN ZONAS DEL INTERIOR HACIENDO REFERENCIA A AMIGO, EN LA CIUDAD HACE REFERENCIA A PERSONAS DEL INTERIOR.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHOLOMETAL ',' CHOLO O INDIGENA QUE SIGUE MODISMOS DE ROQUEROS, PUNKS Y/O HEAVYMETALS.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHOLOPOP ',' UN COMPA QUE ACABA DE LLEGAR A LA CAPITAL VESTIDO COMO EN LOS 70S, CON EL PECHO AFUERO Y USANDO ESSENCIA DE PACHOLI COMO PERFUME.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHOLYWOOD',' FORMA GRACIOSA, DESPECTIVA O UNA MANERA PARA DEFINIR LA FARÁNDULA PANAMEÑA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHOMBO',' PERSONA DE RAZA NEGRA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHOMBA',' PERSONA DE RAZA NEGRA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHONTA ',' CABEZA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHOTA ',' MINIVAN DE LA POLICÍA. TAMBIÉN UTILIZADA PARA REFERIRSE A JODER.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHOTA',' POLICIA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'TONGO',' POLICIA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHUAIN ',' (DE PRONUNCIACIÓN RÁPIDA) ESTA ES UN SINÓNIMO DE YEYE Y ES UNA PERSONA ACOMODADA, ALTA ALCURNIA, DELICADA O ADINERADA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHUCHA ',' VULVA; TAMBIÉN USADO COMO INTERJECCIÓN (EJEMPLO:¡CHUCHA!, QUE CHUCHA ME IMPORTA!)')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHUCHITA ',' VÉASE CONGO. [EJM. TE TAN (ESTÁN) COGIENDO DE CONGO!!!]')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHULETA ',' EXCLAMACION DE SORPRESA O ADMIRACION')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHUPAR ',' INGERIR BEBIDAS ALCOHOLICAS')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHUZO ',' VER CHULETA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'COCHO ',' GOLPE EN LA CABEZA PROPINADO CON LOS NUDILLOS DE LA MANO. EJEMPLO TE VOY A DAR UN COCHO!')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'COCOA',' CUENTO O HISTORIA RELACIONADA A UN SUCESO O EVENTO, NORMALMENTE UN BOCHINCHE O CHISME.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CINTA ',' CUENTO O HISTORIA RELACIONADA A UN SUCESO O EVENTO, NORMALMENTE UN BOCHINCHE O CHISME.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'COMPA ',' FRASE CARIÑOSA REFIRIENDOSE A UN CAMPESINO O A UN COMPADRE... BUEN AMIGO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CONFLEI ',' CUALQUIER CEREAL DE CUALQUIER MARCA QUE SE COME EN EL DESAYUNO, DEL INGLÉS CORN FLAKES')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'COSCORRÓN ',' INSECTO REDONDO Y CAFE, GOLPE DADO CON LOS NUDILLOS (VEASE COCHO).(NORMALMENTE COCORRÓN) ')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CUATRERA ',' MUJER LA CUAL ESTA EN BUSCA O ACECHO DE ALGUN HOMBRE CAZADO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CUECO',' HOMOSEXUAL O LESBIANA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CUECA',' HOMOSEXUAL O LESBIANA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CULANTRO ',' UNA BELLA DAMA. PROVENIENTE DEL SEGMENTO DOBLE VIDA DEL PROGRAMA TELEVISIVO PARECEN NOTICIAS. TAMBIEN ES UNA UN PLANTA QUE SE UTILIZA PARA SAZONAR LA SOPA Y OTROS ALIMENTOS.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CULEAR ',' MANERA VULGAR DE DECIR TENER RELACIONES SEXUALES O SEXO CON UNA PERSONA .')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CULILLO',' MIEDO, TERROR O TEMOR A UNA COSA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ÑÁÑARA ',' MIEDO, TERROR O TEMOR A UNA COSA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CULITO ',' VER PAY')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CULO ',' NALGAS')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'DATIEN ',' TRASPALANTE DE TIENDA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'DE A VAINA',' GANAR ALGO POR PURA BUENA SUERTE EN EL ULTIMO MOMENTO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'DE A VAINILLA',' GANAR ALGO POR PURA BUENA SUERTE EN EL ULTIMO MOMENTO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'POR UN PELITO',' GANAR ALGO POR PURA BUENA SUERTE EN EL ULTIMO MOMENTO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'POR UN COCOAZO',' GANAR ALGO POR PURA BUENA SUERTE EN EL ULTIMO MOMENTO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'POR PURA LECHE',' GANAR ALGO POR PURA BUENA SUERTE EN EL ULTIMO MOMENTO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'DE AGENCIA ','NÍTIDO, BONITO, NUEVO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'DE VEZ ',' DE UNA VEZ, EN EL ACTO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'DIABLO ROJO ',' AUTOBUS GENERALMENTE PINTADO DE VARIOS COLORES PROCEDENTE DE LAS ESCUELAS ESTADOUNIDENSES QUE COMÚNMENTE SE LES LLAMA BORRADORES POR EL EFECTO QUE PRODUCE DURANTE UNA COLISION.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'EN TUCO ',' SINONIMO QUIEBRA DE NO TENER DINERO, HACE REFERENCIA A CUANDO UN AUTOMOVIL ESTA MONTADO SOBRE PEDAZOS DE MADERA, GENERALMENTE SIN LLANTAS O EN REPARACION.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'EN VERGA ',' ALGO DE MALA CALIDAD, NO COMPLACIENTE AL GUSTO DE NADIE ESE SHOW ESTA EN VERGA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'FALTA DE TODO',' VERSIÓN MODERNA DE LA FAMOSA FRASE VENEZOLANA POPULARIZADA EN LOS 80 FALTA DE GLAMOUR. SIGNIFICA FALTA DE RESPETO, FALTA DE ÉTICA, FALTA DE ELEGANCIA, FALTA DE CLASE, FALTA DE CONSIDERACIÓN, FALTA DE... TODO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'FICHA',' PERSONA IMPORTANTE')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'FILO',' ARMA PUNZOCORTANTE')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'FLINTIN',' PROVENIENTE DE EL PATOIS( VER GUARI-GUARI), REFERENTE A UNA PAREJA PELEANDO, DONDE LA MUJER LE TIRA COSAS AL HOMBRE, EN INGLES JAMAIQUINO(PATOIS) FLYING THINGS , USADO PARA DESCRIBIR UN PROBLEMA, CONFLICTO O PELEA. YO NO QUIERO FLINTIN CON ESE MAN.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'FULO',' RUBIO/A.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'FULA',' RUBIO/A.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'FUNDILLO',' ESPECIFICAMENTE EL ORIFICIO ANAL.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'FUSTE',' NALGAS, TRASERO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GADACA',' TRASPALANTE DE. CAGADA(ALGO QUE SALE MAL DE MOMENTO)')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GALLINERO','LA ENTREDA GENERAL O AREA POPULAR DE ALGUN EVENTO CULTURAL (CONCIERTO) O EVENTO DEPORTIVO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GALLO',' BARATO, DE POCA CALIDAD; PERSONA SIN GRACIA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GALLA',' BARATO, DE POCA CALIDAD; PERSONA SIN GRACIA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GANDOCA',' TRASPALANTE DE CAGANDO(DEFECAR)')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GARNATÓN',' BOFETÓN. *GARNATADA NORMALMENTE SE DICE GARNATÁ.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GARNATADA ',' BOFETÓN. *GARNATADA NORMALMENTE SE DICE GARNATÁ.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GLOBITO',' CONDON, PRESERVATIVO; *FORRITO HA SIDO POPULARIZADO POR EL HOMÓNIMO PERSONAJE CONDÓN DEL POPULAR PROGRAMA LA CÁSCARA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'FORRITO ',' CONDON, PRESERVATIVO; *FORRITO HA SIDO POPULARIZADO POR EL HOMÓNIMO PERSONAJE CONDÓN DEL POPULAR PROGRAMA LA CÁSCARA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GOLPE DE ALA ',' AROMA INTOLERABLE QUE PROCEDE DE LAS EXILAS... VULG. VER GRAJO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GRAJO ',' SUDOR DE LAS EXILAS SUMAMENTE APESTOSO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GRUBEO',' ESTAR CON UNA PERSONA POR UN TIEMPO O POR UNA NOCHE PARA PASARLA BIEN Y PARA NADA SERIO O FORMAL.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GRUBEAR',' ESTAR CON UNA PERSONA POR UN TIEMPO O POR UNA NOCHE PARA PASARLA BIEN Y PARA NADA SERIO O FORMAL.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GUABAZO',' GRAN GOLPE, USUALMENTE SEGUIDO DE HEMATOMA DE ALGUNA CLASE.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GUABANAZO',' GRAN GOLPE, USUALMENTE SEGUIDO DE HEMATOMA DE ALGUNA CLASE.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GUACHO','ES UNA SOPA ESPESA QUE LLEVA ÑAME, YUCA, CULANTRO, ARROZ, VERDURAS Y ALGUNA CARNE, QUE PUEDE SER RES, RABITO DE PUERCO O CHICHARRÓN. EL GUACHO SE SIRVE TRADICIONALMENTE EN UNA TOTUMA, PLATO QUE SE FABRICA PARTIENDO A LA MITAD UNOS FRUTOS REDONDOS Y DUROS QUE CRECEN EN EL MONTE. TAMBIEN SIGINFICA LA COMBINACION DE VARIAS COSAS.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GUAGUA ',' SE DICE DE UN AUTOMÓVIL MUY VIEJO O EN MAL ESTADO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GUAPIN',' SALUDO QUE INDICA QUE PASA. DEL INGLÉS WHAT HAPPENED? / WHAT IS HAPPENING?.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'JUATAPIN ',' SALUDO QUE INDICA QUE PASA. DEL INGLÉS WHAT HAPPENED? / WHAT IS HAPPENING?.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GUAPOTE ',' INDIVIDUO USUALMENTE CON POCA AUTOESTIMA QUE HACE MUCHA FISICULTURA PERO QUE AL FINAL SIEMPRE SIGUE SIENDO BIEN FEO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GUARI-GUARI',' DIALECTO DE LA PROVINCIA DE BOCAS DEL TORO, ES UNA MEZCLA DE ESPAÑOL, FRANCÉS, INGLÉS Y LENGUAS INDÍGENAS.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GUARO ',' ALCOHOL; BEBIBA ALCOHÓLICA; LICOR.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GUILLADO ',' 1.INFLUENCIADO POR ALUCINÓGENOS 2.EMOCIONADO, INSPIRADO. (NORMALMENTE SE DICE GUILLAO) ')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'HUEVEAR ',' PERDER EL TIEMPO DE LA PEOR FORMA. [EJM. PÓNTE A TRABAJÁ Y DEJA DE TA WEBIANDO!!!]')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'IR AL CHOQUE',' IR DE FRENTE ANTE CUALQUIER ADVERSIDAD.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'JODER',' BROMEAR, MOLESTAR, IRRITAR. EJM: NO JODAS!')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'JUEGA VIVO ',' CON ASTUCIA, GENERALMENTE SIN MORAL, OPORTUNISTA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'JUGO-E-POLICIA ',' AGUA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'KENKE ',' BATE DE MARIHUANA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'LA KENTON ',' LLAVE EN LUCHA LIBRE QUE SE USA PARA AMARRAR AL ADVERSARIO, USANDO LAS PIERNAS, MIENTRAS LO REPLETAN DE RONCABALAOS... USALMENTE ESTA LLAVE SE USA POR MUJERES QUE QUIEREN TENER HIJOS OBLIGANDO AL NOVIO A EJACULAR DENTRO DEL VIENTRE... POR ESO SE DICE CUIDAO Y TE HACE LA KENTON.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'LABIA ',' ADULACIÓN, NORMALMENTE PARA CONVENCER A LA PERSONA DE CUAL ES LA MEJOR ALTERNATIVA EN UNA SITUACIÓN DADA O PARA CONSEGUIR APOYO DE LA MISMA; MUY COMUN EN EL AMBITO DE LA POLITICA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'LÁITER',' ENCENDEDOR, ANGLICISMO [DE LIGHTER].')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'LAOPÉ ',' TRASPALANTE DE PELAO (MUCHACHO)')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'LEVANTE','NOVIO/A, QUIÉNES SE GUSTAN Y TIENEN QUÍMICA ENTRE ELLOS.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'LIMADO',' DICESE DE LA PERSONA QUE SE ENCUENTRA MUY CANSADA LUEGO DE TRABAJAR O BEBER MUCHO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'LIMPIO (A) ',' SIN DINERO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'LLECA ',' TRASPALANTE DERIVADO DE CALLE')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'LOCO ',' ES COMO SE LLAMAN LOS AMIGOS DE CARIÑO. MUY COMUN ENTRE ORIUNDOS DE PANAMÁ.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'MACHIUA',' MAS CHOLO QUE UN CHOLO POP... USUALMENTE UN INDIGENA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'MACHIGUA',' MAS CHOLO QUE UN CHOLO POP... USUALMENTE UN INDIGENA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'MACHIHUA ',' MAS CHOLO QUE UN CHOLO POP... USUALMENTE UN INDIGENA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'MACHOEMONTE ',' TIPO MAS TOF QUE RAMBO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'MAFÁ ',' ABREBOCAS DE HARINA (FRITURA) EN FORMA DE TRENZA; DÍCESE DE UN ENREDO, ASUNTO COMPLICADO, O PERSONAS ABRAZADAS DE FORMA MUY AFECTIVA (COMO MAFÁ).')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'MALEANTE ',' DELINCUENTE O PERSONA QUE QUIERE SER COMO LOS DELINCUENTES.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'MANACHO ',' HOMBRE JOVEN DE CLASE OBRERA, CUERPO ATLÉTICO Y ASPECTO UN POCO RUDO Y MUY MASCULINO. MANACHA: LESBIANA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'MANZANILLO ',' SIN PERSONALIDAD, INFLUENCIABLE CON FACILIDAD, TAMBIÉN SE DICE ASÍ A LOS VIVIDORES.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'MATAPUERCO O SOPLAMOCO ',' GOLPE EXAGERADO Y CERTERO, QUE DUELE MUCHO. NÓTESE QUE SOPLAMOCO ES EHN LA MEJILLA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ME VALE VERGA',' SITUACIÓN QUE NO GENERA NINGUNA CLASE DE REACCIÓN NI DE INTERÉS EN LA PERSONA.(VULGAR)/UN PEPINO/UN COMINO ')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'MEÑA ',' JÓVENES DE LA CALLE DE MAL HABLAR Y VESTIR. DENOTA LAS ÚLTIMAS 4 LETRAS DE LA NACIONALIDAD PANAMEÑA. TAMBIÉN TRASPALANTE DEL TUBÉRCULO ÑAME)')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'METO ',' UNA EXPRESIÓN QUE DENOTA UNA FRASE DE ADMIRACIÓN Y AFIRMACIÓN MUY UTILIZADA EN LA PROVINCIA DE CHIRIQUÍ. EN LA CIUDAD DE PANAMÁ (SOBRETODO) OFI.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'MILLO ',' PALOMITAS DE MAÍZ. MILLO VIENE DE LA LENGUA GALLEGA Y QUIERE DECIR MAÍZ. EN GALICIA SE LE LLAMA A LAS PALOMITAS DE MAÍZ, FLOCOS DE MILLO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'MOCOCOA ',' LIQUIDO PRODUCIDO POR LOS MIEMBROS NASALES, REGULARMENTE DE COLOR VERDE, ESTA SE BEBE EN GRANDES CANTIDADES USUALMENTE LUEGO DE QUE A UNO LO HAN TRAICIONADO (VER QUEMADO) EN UNA RELACION SE CREIA SERIA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'MONTADO',' QUE TIENE BUENA SITUACIÓN ECONÓMICA.  (NORMALMENTE SE DICE MONTAO/A)')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ÑAMERÍA ',' LOCURA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ÑAMPEARSE ',' VOLVERSE LOCO/A.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ÑÁNGARA ',' FORMA DESPECTIVA DE DEFINIR A LOS COMUNISTAS O MIEMBROS DE PARTIDO DE IZQUIERDA O EXTREMA IZQUIERDA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ÑANGOTADO',' PERSONA QUE CAMINA EN CUCLILLAS')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'AÑINGOTADO',' PERSONA QUE CAMINA EN CUCLILLAS')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ÑAPA',' UN REGALO QUE DAN CUANDO SE COMPRA ALGO EN UN TIENDA O ABARROTERRIA (INTRODUCIDO POR LOS CHINOS PARA CAPTAR CLIENTES FRECUENTES).')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ÑECKS ',' VERSIÓN DECENTE DE MIERDA. [EJM. TE WA (VOY A) SACÁ LA ÑECKS!!!]')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'NEVERA ',' REFRIGERADORA; AUTOBÚS CON AIRE ACONDICIONADO (DÍCESE DE LOS TRANS-PROVINCIALES [EJM: PANAMÁ-DAVID] PORQUE NORMALMENTE VAN A TEMPERATURAS MUY FRÍAS); MUJER CUADRADA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'NO ME PARECE',' FRASE POPULARMENTE UTILIZADA PARA DEMOSTRAR DESCONTENTO POR ALGO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ÑORRO ',' HOMOSEXUAL/ ESE MAN ES ÑORRO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'OFI ',' ENTENDIDO, OK (ACORTACIÓN DE OFICIAL, UTILIZADO PARA APROBAR O RECIBIR APROBACIÓN).')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PALANTE ',' REDUCCIÓN DERIVADA DE PARA ADELANTE')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PACIERO(S)',' AMIGO, GENERALMENTE AMIGOS CON QUIENES SE COMPARTE PARRANDAS.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PAJA',' MASTURBARSE')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'VOLAR COMETA ',' MASTURBARSE')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PAJIZO ',' PERSONA QUE SE MASTURBA CONSTANTEMENTE; PERSONA QUE MUESTRA DEBILIDAD ANTE UNA ACTIVIDAD FÍSICA. [EJM. JO! NO PUEDES NI LEVANTAR ESO... TAS PAJIZO!!!].')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PAJIZA ',' PERSONA QUE SE MASTURBA CONSTANTEMENTE; PERSONA QUE MUESTRA DEBILIDAD ANTE UNA ACTIVIDAD FÍSICA. [EJM. JO! NO PUEDES NI LEVANTAR ESO... TAS PAJIZO!!!].')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PAKA ',' CARGAMENTO DE DROGA; PERSONA QUE TIENE FARDOS/MOCHILAS/ BULTOS [DEL INGLÉS PACKS]; REFERENTE A CARTUCHOS DE BALAS; DELINCUENTE.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PARACAÍDAS',' PERSONA QUE ACUDE A UNA REUNIÓN O FIESTA SIN INVITACIÓN.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PARAPAPEO',' PALABRA QUE DESCRIBE EL BAILE DE LAS REINAS DE CARNAVAL. VERBO: PARAPAPEAR; EJM: ESTÁ PARAPAPEANDO. EL TÉRMINO SE DERIVA DEL SONIDO DE LAS TROMPETAS DE UNA MURGA: PARA PA PÁ')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PARKIN',' FIESTA O REUNIÓN ENTRE AMIGOS.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PARQUEARR',' SALIR CON ALGUIEN A PASAR EL RATO: PARQUEAR CON MIS AMIGOS; PONER A ALGUIEN EN SU SITIO QUISO INSULTARME Y LO PARQUEÉ. NORMALMENTE LA GENTE DICE PARQUIAR.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PATACÓN ',' POPULAR ACOMPAÑAMIENTO DE COMIDA, EL CUAL CONSISTE EN RODAJAS DE PLÁTANO APLASTADAS Y LUEGO FRITAS.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PATACONCITO ',' PEQUEÑA ACUMULACIÓN DE BASURA, VIENE DEL RELLENO SANITARIO DE LA CIUDAD DE PANAMÁ (CERRO PATACÓN).')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PATATÚS ',' DESMAYO, ATAQUE CARDÍACO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PATI-AMARILLO ',' CIGARRILLO CON EL FILTRO DE COLOR AMARILLO O ANARANJADO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PATO ',' VER SACALODO, TUTIFRUTI, PUNKY-PUNCH ...I.E. HOMOSEXUAL')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ÑORRO',' VER SACALODO, TUTIFRUTI, PUNKY-PUNCH ...I.E. HOMOSEXUAL')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,' ÑAÑO ',' VER SACALODO, TUTIFRUTI, PUNKY-PUNCH ...I.E. HOMOSEXUAL')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PEBRE',' COMIDA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'REFINE ',' COMIDA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PELO PELO ',' BAILE ERÓTICO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PELONERA ',' GOLPIZA PROPICIADA ENTRE VARIOS SIN SER FUERTE, COMÚNMENTE EN LA CEBEZA Y EN LA SECUNDARIA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PERRO',' DESPECTIVO UTILIZADO COMO SINÓNIMO DE MUJERIEGO; USADO COMO INSULTO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PERRON ',' PERSONA DE POCA CAPACIDAD. DICESE DE UNA PERSONA QUE NO ES MUY POPULAR DENTRO DE UN CIRCULO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PERRÓN',' PERSONA QUE NO DESEMPEÑA BIEN UNA FUNCION REFERENCIADA O EXAGERACION DE PERRO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PESCUEZONA ',' CERVEZA DE BOTELLA TAMAÑO GRANDE.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PESO',' MONEDA DE 50 CENTAVOS, VIENE DEL PERIODO DE LA SEPARACIÓN DE PANAMA DE COLOMBIA DONDE EQUIVALÍA EL PESO COLOMBIANO A 50 CENTAVOS DE DÓLAR; USADO COMÚNMENTE EN LAS PELEAS DE GALLOS PARA CUANTIFICAR LAS APUESTAS.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PICANDO ',' ALGO QUE ESTÁ DE MODA.(SU USO SE DEBE AL FAMOSO BAILE DEL PIQUE, EN PANAMÁ.)')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PICHI',' DROGA, DÍCESE COMÚNMENTE A LA COCAINA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PIEDRA ',' CRACK (DROGA).')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PIEDRERO',' PERSONA DROGADICTA QUE HA LLEGADO A LA INDIGENCIA POR SER DROGADICTO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PIEDRERA',' PERSONA DROGADICTA QUE HA LLEGADO A LA INDIGENCIA POR SER DROGADICTO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PILAR ',' ESTUDIAR CON AFÓN; PILÓN(A) ES ALGUIEN MUY ESTUDISO O SABELOTODO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PILINQUI ',' PERSONA MEZQUINA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PILLAR ',' SYNONIMO DE TOMAR/COGER/AGARRAR, EJM: PILLA LA PLUMA...; ENCONTRAR A HURTADILLAS UNA SITUACION O VER ALGO EN ESPECIAL.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PINTA',' CERVEZA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'FRÍA ',' CERVEZA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PIPÍ ',' PENE, MIEMBRO VIRIL; ORINE.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PLENA ',' USADO PARA CANCIONES/RITMOS DE REGGAE PERO TAMBIÉN USADA PARA OTROS GÉNEROS CUANDO LA CANCION ES BUENA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PONCHAR ',' DESINFLAR; TENER SEXO; SACAR A UN BATEADOR POR OUT EN BÉISBOL.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PONCHERA ',' DESORDEN, ALGARABÍA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PORCÓN',' ENTIÉNDASE POPCON O PALOMITAS DE MAIS')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'MILLO ',' ENTIÉNDASE POPCON O PALOMITAS DE MAIS')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PRAKA PRAKA ',' DERIVACION DE RAKATACA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PUESTO QUEMADO ',' PUESTO RESERVADO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'QUÉ BATE ',' USADO COMO DESCRIPCIÓN DE ALGO FICTICIO, ASOMBROSO O ESPECTACULAR')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'QUE ES LO QUE ES',' QUE HAY DE NUEVO. (PRONUNCIADO QUE LO QUE É O QUELOQUÉ)')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'QUÉ XOPÁ ',' TRASPALANTE, DERIVADO DE ¿QUÉ PASO?')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'QUEMADO',' PERSONA A LA CUAL SU NOVIO/NOVIA ESPOSO/ESPOSA LO HA TRAICIONADO CON OTRA/O.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'QUESO',' CIERTA ATRACCIÓN MERAMENTE FÍSICA Y SEXUAL.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'RAKATACA ',' HOMBE O MUJER SIN CLASE, COMUNMENTE UTILIZA MAYORMENTE LA JERGA PANAMEÑA AUTOCTONA. DERIVADO DEL SONIDO DE LAS METRALLETAS AL DISPARAR RAKATAKATAKATAKATAKA POPULARIZADO DURANTE UNA CANCIÓN DEL GRUPO JAM & SUPPOSE EN 1992: CAMIÓN LLENO DE GUN.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'RAMBULERO',' PERSONA USUALMENTE DE LOS BARRIOS POPULARES QUE GUSTA DE LAS PELEAS, INTRIGAS, CHISMES, BAILE Y OTRAS MANIFESTACIONES DE COMUNICACIÓN SIN CLASE.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'RANGÁLIDO ',' DE MAL ASPECTO, FLACO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'RANTAN ',' MUCHO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'REAL ',' MONEDA DE 5 CENTÉSIMOS DE BALBOA. LA PALABRA VIENE DE LA ÉPOCA DE LA COLONIA EN LA CUAL SE LE DENOMINABA REAL A LAS MONEDAS ACUÑADAS EN POTOSÍ, LIMA Y EN ALGUNOS OTROS LUGARES. EN TABOGA, PANAMÁ, POR EJEMPLO UNA FAMILIA LLEGÓ A ENCONTRAR UNA CANTIDAD DE MONEDAS DE DENOMINACIÓN DE PESOS DE 8 REALES, MIENTRAS CONSTRUÍAN SU CASA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PAU PAU ',' CASTIGO A LOS HIJOS, YA SEA DARLES CON LA CORREA (REJERA) O CON NALGADAS (PAU PAU).')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'REJERA',' CASTIGO A LOS HIJOS, YA SEA DARLES CON LA CORREA (REJERA) O CON NALGADAS (PAU PAU).')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'REJEROS ',' GRUPOS DE HOMBRES (AMIGOS ENTRE SÍ) QUE VAN A UNA DISCOTECA, CLUBES NOCTURNOS O FIESTA A LIGARSE CON MUJERES O QUE SIMPLEMENTE SE REÚNEN PARA PASARLA BIEN. TAMBIÉN SE REÚNEN EN UN CASA PARA LIBAR LICOR Y ECHAR HISTORIAS U APSPECTOS PERSONALES QUE LE HAN PASADO. EL PROGRAMA DE HUMOR DE LA CASCARA HIZO UNA PARODIA DE ESTO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'REJO ',' AZOTE, PENE.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'REVENTAR',' VACILAR, TOMAR EL TIEMPO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'DETONAR',' VACILAR, TOMAR EL TIEMPO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ROMPER ',' VACILAR, TOMAR EL TIEMPO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ROMPE PECHO',' UNA BOTELLA DE CERVEZA MUY GRANDE.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'MANGA LARGA',' UNA BOTELLA DE CERVEZA MUY GRANDE.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'RONCABALAO','GOLPE EXAGERADO CAPAZ DE MATAR A UNA PERSONA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'SABROSÓN ',' ALGO O ALGUIEN QUE SE ENCUENTRE EN EXCELENTES CONDICIONES O ALGÚN EVENTO AGRADABLE.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'SACALODO',' VER CUECON')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'TUTIFRUTI',' VER CUECON')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PUNKYPUNCH ',' VER CUECON')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'SALAO',' PERSONA QUE TIENE MALA SUERTE. EJM. MARIO TU ESTÁS SALADO EN LA LOTERÍA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'SARAO',' FIESTA O BAILE ORGANIZADA GENERALMENTE POR EL SEGUNDO CICLO DE SECUNDARIA. TÍPICAMENTE SE REALIZA EN HORAS DE LA TARDE, EN EL GIMNASIO DE LA ESCUELA. DÍCESE DE CUALQUIER FIESTA EN QUE EL OBJETIVO PRINCIPAL ES BAILAR.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'SÓLIDO ','SIGNIFICA EXCELENTE. TAMBIÉN CHÉVERE.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'TALLAO','BIEN VESTIDO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'TARRANTAN','MÁS QUE RANTAN. MUCHÍSIMO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'TATAI','BYE, HASTA LUEGO, NOS VEMOS.* TÁ BIEN  (VIENE DE: ESTÁ BIEN; SE LE DA SIGNIFICADO SEGÚN LA DICCIÓN, PRONUNCIACIÓN Y EL TONO DE LA VOZ USADA POR LA PERSONA) ALGO SORPRENDENTE; FALSO; EXAGERADO; EMOCIONANTE; TODOS LOS SIGNIFICADOS ANTERIORES A LA VEZ.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'TELLA','BOTELLA (GENERALMENTE DE LICOR).')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'TOTUMA: ','ES UN PLATO QUE SE FABRICA PARTIENDO A LA MITAD UNOS FRUTOS REDONDOS Y DUROS QUE CRECEN EN EL MONTE (CALABAZO).')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'TONGO ',' POLICIA DE BAJO RANGO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'TONTÓN',' VAGINA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'MICHA',' VAGINA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'MOTA',' VAGINA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'TROZO',' VAGINA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'TORTILLERA ',' LESBIANA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'TREPAQUESUBE/VERGUERO/CHUCHAMADRE/ZAPEROCO ',' GRAN PROBLEMA, DISTURBIO, DESORDEN, CONFLICTO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'VERGUERO',' GRAN PROBLEMA, DISTURBIO, DESORDEN, CONFLICTO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHUCHAMADRE',' GRAN PROBLEMA, DISTURBIO, DESORDEN, CONFLICTO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ZAPEROCO ',' GRAN PROBLEMA, DISTURBIO, DESORDEN, CONFLICTO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'TRUENO',' ARMA DE FUEGO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'VACA ',' COLECTA DE DINERO ENTRE VARIAS PERSONAS PARA COMPRAR ALGO. HEY HAGAN UNA VACA PALA CARMEN AHÍ...')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'VAINA ',' UTILIZADO COMO COMODÍN EN CONVERSACIONES, USADO POR COSA (TAMBIÉN USADO EN OTROS PAÍSES CON EL MISMO SIGNIFICADO).')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'VALE CEBO ',' DÍCESE DE UNA SITUACIÓN INJUSTA O ESTÚPIDA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'VAMPIRA',' MUJERES DE ALTO MANTENIMIENTO, SUMAMENTE IGNORANTES EN TODO MENOS EN EL ARTE DE HACER EL AMOR.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHUPASANGRE ',' MUJERES DE ALTO MANTENIMIENTO, SUMAMENTE IGNORANTES EN TODO MENOS EN EL ARTE DE HACER EL AMOR.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'VERGÜERO ',' PROBLEMA, DEBATE DISCUSION ACALORADA LLEGANDO AL PUNTO CERCANO A FORMARSE UNA TRIFULCA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'VIDAJENEAR ',' HUSMEAR, ESPIAR, Y ENTROMETERSE EN LA VIDA AJENA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'VIOLINISTA',' PERSONA QUE ACOPAÑA A UNA PAREJA PERO NO DEBE ESTAR PRESENTE PUES LA PAREJA QUIERE ARROPAR. (VEÁSE ARROPAR).')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'YAPLA ',' PLAYA. SALE DEL REVERSO DE PLAYA, YASPLA, Y QUITÁNDOLE PLA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'YEYE',' PERSONA ADINERADA QUE PRESUME DE SU CONDICIÓN, COMÚNMENTE USA ANGLICISMOS EN SU HABLA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'RABIBLANCO',' PERSONA ADINERADA QUE PRESUME DE SU CONDICIÓN, COMÚNMENTE USA ANGLICISMOS EN SU HABLA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ZAMBITO(A) ',' EXPRESIÓN DE LAS PROVINCIAS DE HERRERA Y LOS SANTOS, SIGNIFICA NIÑO O NIÑA.')");


    conn.commit()
    print("")
    print("                                 -->Base de datos Creada y se insertaron los registros de inicio")
    print("")
    p=input("Presione una <Enter> para continuar")
    conn.close()


