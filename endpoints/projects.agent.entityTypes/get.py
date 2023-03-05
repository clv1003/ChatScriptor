import requests

from endpoints.datosGoogle import obtenerToken, obtenerURL

#url = 'https://dialogflow.googleapis.com/v2/projects/{project_id}/agent/entityTypes'

url = obtenerURL(4)+'{entity_type_id}'
token = obtenerToken()

headers = {
    'Authorization': 'Bearer ' + token
}

response = requests.get(url, headers=headers)

if response.ok:
    entity_types = response.json().get('entityTypes', [])

    for entity_type in entity_types:
        if entity_type == '{entity_type_id}':
            print(entity_type.get('displayName'))
else:
    print('La solicitud falló con código de estado', response.status_code)
