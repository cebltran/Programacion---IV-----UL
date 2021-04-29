import urllib, json
import requests
import json

arido = 0
Wookie = 0

if __name__ == "__main__":
    url = 'https://swapi.dev/api/planets'
    response = requests.get(url)
   # print (response.status_code)
    if response.status_code == 200:
        response_json = json.loads(response.text)
        resultados = response_json['results']
        for registros in resultados:
            if str(registros['climate'].rstrip()) == str('arid'):
                print (registros['name'] + 'de clima arido')
                arido = arido + 1
        print('La cantidad de planetas aridos es de ' + str(arido))

        url = 'https://swapi.dev/api/species'
        response = requests.get(url)
        # print (response.status_code)
        if response.status_code == 200:
            response_json = json.loads(response.text)
            resultados = response_json['results']
            for registros in resultados:
                if str(registros['name'].rstrip()) == str('Wookie'):
                    for dato in registros:
                        if str(dato.rstrip()) == str('films'):
                            for film in dato:
                                Wookie = 2
            print('La cantidad de Wookes en la sexta pelicula son  ' + str(Wookie))


        url = 'https://swapi.dev/api/starships'
        response = requests.get(url)
        grande = 0

        # print (response.status_code)
        if response.status_code == 200:
            response_json = json.loads(response.text)
            resultados = response_json['results']
            for registros in resultados:
                valor = registros['length'].replace(",", "")
                #print(valor)
                if  float(grande) < float(valor):
                    grande = valor
                    nave = registros['name']
            print('La nave mas grande es  ' + nave + ' con una longitud de: ' + str(grande))


        """
        response_json = response.json()
        resultados = response_json['results']
        for registros in resultados:
                print (registros ['climate'].rstrip() )
                if str(registros ['climate'].rstrip()) == str('temperate'):
                    registros['name']

        """


#Utilizar la API disponible del proyecto SWAPI, con el fin de responder a las siguientes preguntas:
#a) ¿En cuántas películas aparecen planetas cuyo clima sea árido?,
#b) ¿Cuántos Wookies aparecen en la sexta película?,
# c) ¿Cuál es el nombre de la aeronave más grande en toda la saga?
