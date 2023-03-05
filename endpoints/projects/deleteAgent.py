import requests

from endpoints.datosGoogle import obtenerToken, obtenerURL

# PARA ELIMINAR UN AGENTE

url = obtenerURL(1)
token = obtenerToken()

headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json'
}

response = requests.delete(url, headers=headers)

if response.ok:
    print('El agente se eliminó con éxito')
else:
    print('La solicitud falló con código de estado', response.status_code)
