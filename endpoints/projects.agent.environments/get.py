import requests

from endpoints.DatosGoogle import obtenerToken, obtenerURL

#url = 'https://dialogflow.googleapis.com/v2/projects/{project_id}/agent/environments'

url = obtenerURL(5)
token = obtenerToken()

headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers)

if response.ok:
    print('Nombre del environment: ', response.json().get('displayName', ''))
    print('Descripción del environment: ', response.json().get('description', ''))
else:
    print('La solicitud falló con código de estado', response.status_code)
