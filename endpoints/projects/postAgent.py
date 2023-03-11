import requests
import json

from endpoints.datosGoogle import obtenerToken, obtenerURL

# PARA CREAR EL AGENTE

url = obtenerURL(1)
token = obtenerToken()

headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json'
}

data = {
    'displayName': 'Nombre del agente',
    'defaultLanguageCode': 'es',
    'timeZone': 'Europe/Paris',
    'description': 'Descripción del agente'
}

response = requests.post(url, data=json.dumps(data), headers=headers)

if response.ok:
    print('Nombre del agente: ', response.json().get('displayName', ''))
    print('ID del agente: ', response.json().get('name', ''))
else:
    print('La solicitud falló con código de estado', response.status_code)
