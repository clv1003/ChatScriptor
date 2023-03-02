import requests

url = 'https://dialogflow.googleapis.com/v2/projects/{project_id}/agent/entityTypes:batchDelete'
headers = {
    'Authorization': 'Bearer {api_key}',
    'Content-Type': 'application/json'
}
data = {
    'entityTypeNames': [
        'projects/{project_id}/agent/entityTypes/{entity_type_id1}',
        'projects/{project_id}/agent/entityTypes/{entity_type_id2}',
        'projects/{project_id}/agent/entityTypes/{entity_type_id3}'
    ]
}

response = requests.post(url.format(project_id='{project_id}'), headers=headers, json=data)

if response.ok:
    print('Tipos de entidad eliminados exitosamente')
else:
    print('La solicitud falló con código de estado', response.status_code)
