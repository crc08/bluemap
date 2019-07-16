#Se requiere instalar previamente requests via pip install

import requests


##Generar token con python
url = "https://api.crimsonhexagon.com/api/authenticate"

querystring = {
  "username":"fkina@digitalartsnetwork.com.mx",
  "noExpiration":"true",
  "password":"Teran2019!"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

También se puede generar desde la terminal con un Curl

curl -X GET "https://api.crimsonhexagon.com/api/authenticate?username=fkina@digitalartsnetwork.com.mx&password=Teran2019!&noExpiration=true"
##Generar streaming

#es necesario actualizar el valor del auth o en su defecto ponerlo en una variable
#también puede variar el monitor si lo aplicamos a otro previa dada de alta en el servicioo de streaming
url = "https://api.crimsonhexagon.com/api/stream/25776343057/posts"

querystring = {"auth":"hkcVPsJ285PuFI1I2WMYdXFqMhDkmPkDRYql-Xdk2Ys"}

response = requests.request("GET", url, params=querystring)

print(response.text)

##Guardar en un archivo txt, csv, json cambiando la terminal

#Introducir sólo la respuesta tipo texto en una variable para poder convertirla en json
tweets = response.text

import json

#con la librería json escribir archivo

with open('data.json', 'w') as outfile:  
    json.dump(tweets, outfile)

##Curl para el team list

#Es necesario ejecutarlo fuera terminal por ahora desde curl previamente instalado.
#También se puede poner la url en el navegador

# curl -X GET "https://api.crimsonhexagon.com/api/team/list?auth=hkcVPsJ285PuFI1I2WMYdXFqMhDkmPkDRYql-Xdk2Ys"

### El team id siempre es el mismo por ser un único equipo. Así que se le asigna a una variable

teamid = 2313480090

#se pone el teamid en el monitor list que se llama desde un Curl

curl -X GET "https://api.crimsonhexagon.com/api/monitor/list?auth=hkcVPsJ285PuFI1I2WMYdXFqMhDkmPkDRYql-Xdk2Ys&team=2313480090"



##Wordcloud

params = (
    ('auth', 'hkcVPsJ285PuFI1I2WMYdXFqMhDkmPkDRYql-Xdk2Ys'),
    ('id', '25615108725'),
    ('start', '2019-06-22'),
    ('end', '2019-07-15'),
)

response = requests.get('https://api.crimsonhexagon.com/api/monitor/wordcloud', params=params)

#Extraer el json a una variable. Se puede extraer el campo de data?
words = response.text


#Si no funciona se puede intentar con un Curl
# curl -X GET "https://api.crimsonhexagon.com/api/monitor/wordcloud?auth=hkcVPsJ285PuFI1I2WMYdXFqMhDkmPkDRYql-Xdk2Ys&id=25776343057&start=2019-06-22&end=2019-07-15"



##Monitor post

params = (
    ('auth', 'hkcVPsJ285PuFI1I2WMYdXFqMhDkmPkDRYql-Xdk2Ys'),
    ('id', '25615108725'),
    ('start', '2019-06-22'),
    ('end', '2019-07-15'),
)

response = requests.get('https://api.crimsonhexagon.com/api/monitor/posts', params=params)

print(response.text)

posts = response.text

#Si no funciona se puede intentar con un Curl


# curl -X GET "https://api.crimsonhexagon.com/api/monitor/posts?auth=hkcVPsJ285PuFI1I2WMYdXFqMhDkmPkDRYql-Xdk2Ys&id=25615108725&start=2019-06-22&end=2019-07-15&filter=extendLimit=false&fullContents=true&geotagged=true"


