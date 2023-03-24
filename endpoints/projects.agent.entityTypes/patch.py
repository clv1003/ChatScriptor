import requests
import json

from endpoints.DatosGoogle import obtenerToken, obtenerURL

#url = 'https://dialogflow.googleapis.com/v2/projects/{project_id}/agent/entityTypes/{entity_type_id}'

url = obtenerURL(4)+'{entity_type_id}'
token = obtenerToken()

headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json'
}

data = {
    'displayName': 'Nuevo nombre para el tipo de entidad',
    'kind': 'KIND_MAP'
}

response = requests.patch(url, headers=headers, data=json.dumps(data))

if response.ok:
    print('Tipo de entidad actualizado exitosamente')
else:
    print('La solicitud falló con código de estado', response.status_code)
