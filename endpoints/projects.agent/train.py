import requests

from endpoints.datosGoogle import obtenerToken, obtenerURL

#url = 'https://dialogflow.googleapis.com/v2/projects/{project_id}/agent:train'

url = obtenerURL(1)+':search'
token = obtenerToken()

headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers)

if response.ok:
    print('Agente entrenado exitosamente')
else:
    print('La solicitud falló con código de estado', response.status_code)
