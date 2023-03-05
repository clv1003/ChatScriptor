import requests
import json

from endpoints.datosGoogle import obtenerToken, obtenerURL

# PARA ACTUALIZAR EL AGENTE

url = obtenerURL(1)
token = obtenerToken()

headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json'
}

data = {
    'displayName': 'Nuevo nombre del agente',
    'description': 'Nueva descripción del agente'
}

response = requests.patch(url, data=json.dumps(data), headers=headers)

if response.ok:
    print('El agente se ha actualizado con éxito')
else:
    print('La solicitud falló con código de estado', response.status_code)
