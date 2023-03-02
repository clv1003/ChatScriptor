import requests

url = 'https://dialogflow.googleapis.com/v2/projects/{project_id}/agent/entityTypes/{entity_type_id}'
headers = {
    'Authorization': 'Bearer {api_key}',
}

response = requests.delete(url.format(project_id='{project_id}', entity_type_id='{entity_type_id}'), headers=headers)

if response.ok:
    print('Tipo de entidad eliminado exitosamente')
else:
    print('La solicitud falló con código de estado', response.status_code)
