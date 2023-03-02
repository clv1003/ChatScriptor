import requests
import json

url = 'https://dialogflow.googleapis.com/v2/projects/{project_id}/agent/entityTypes/{entity_type_id}'

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {api_key}'
}

data = {
    'displayName': 'Nuevo nombre para el tipo de entidad',
    'kind': 'KIND_MAP'
}

response = requests.patch(url.format(project_id='{project_id}'), headers=headers, data=json.dumps(data))

if response.ok:
    print('Tipo de entidad actualizado exitosamente')
else:
    print('La solicitud falló con código de estado', response.status_code)
