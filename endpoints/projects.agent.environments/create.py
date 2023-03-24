import requests

from endpoints.DatosGoogle import obtenerToken, obtenerURL

#url = 'https://dialogflow.googleapis.com/v2/projects/{project_id}/agent/environments'

url = obtenerURL(5)
token = obtenerToken()

headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json'
}

data = {
    'displayName': 'Nombre del environment',
    'description': 'Descripción del agente'
}

response = requests.post(url, headers=headers, json=data)

if response.ok:
    print('Environments creado exitosamente')
else:
    print('La solicitud falló con código de estado', response.status_code)
