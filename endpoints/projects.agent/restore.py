import requests

from endpoints.datosGoogle import obtenerToken, obtenerURL

#url = 'https://dialogflow.googleapis.com/v2/projects/{project_id}/agent:restore'

url = obtenerURL(1)+':restore'
token = obtenerToken()

headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json'
}

data = {
    'agentContent': 'contenido-del-agente-restaurado',
}

response = requests.post(url, headers=headers, json=data)

if response.ok:
    print('Agente restaurado exitosamente')
else:
    print('La solicitud falló con código de estado', response.status_code)
