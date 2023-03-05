import requests

from endpoints.datosGoogle import obtenerToken, obtenerURL

#url = 'https://dialogflow.googleapis.com/v2/projects/{project_id}/agent:import'

url = obtenerURL(1)+':import'
token = obtenerToken()

headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json'
}

body = {
    'agentUri': 'gs://bucket-name/file-name.zip'
}

response = requests.post(url, headers=headers, json=body)

if response.ok:
    response_json = response.json()
    print('El agente se importó correctamente')
else:
    print('La solicitud falló con código de estado', response.status_code)
