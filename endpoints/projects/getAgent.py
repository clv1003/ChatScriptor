import requests

from endpoints.datosGoogle import obtenerToken, obtenerURL

# PARA OBTENER UN AGENTE

url = obtenerURL(1)
token = obtenerToken()

headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers)

if response.ok:
    print('Nombre del agente: ', response.json().get('displayName', ''))
    # es opcional para todos los agentes asique no se como gestionarlo de momento
    print('Descripción del agente: ', response.json().get('description', ''))
    print('Lenguaje predeterminado del agente: ', response.json().get('defaultLanguageCode', ''))
    print('Zona horaria del agente: ', response.json().get('timeZone', ''))
else:
    print('La solicitud falló con código de estado', response.status_code)
