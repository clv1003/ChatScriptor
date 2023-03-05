import requests

from endpoints.datosGoogle import obtenerToken, obtenerURL

# url = 'https://dialogflow.googleapis.com/v2/projects/{project_id}/agent/entityTypes:batchDelete'

url = obtenerURL(4)+':batchDelete'
token = obtenerToken()

headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json'
}

data = {
    'entityTypeNames': [
        'projects/tfg-dialogflow-clv/agent/entityTypes/{entity_type_id1}',
        'projects/tfg-dialogflow-clv/agent/entityTypes/{entity_type_id2}',
        'projects/tfg-dialogflow-clv/agent/entityTypes/{entity_type_id3}'
    ]
}

response = requests.post(url, headers=headers, json=data)

if response.ok:
    print('Tipos de entidad eliminados exitosamente')
else:
    print('La solicitud falló con código de estado', response.status_code)
