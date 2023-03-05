import requests

from endpoints.datosGoogle import obtenerToken, obtenerURL

#url = 'https://dialogflow.googleapis.com/v2/projects/{project_id}/agent/entityTypes'

url = obtenerURL(4)
token = obtenerToken()

headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json'
}

data = {
    'displayName': 'Nombre tipo entidad',
    'kind': 'KIND_MAP',
    'autoExpansionMode': 'AUTO_EXPANSION_MODE_UNSPECIFIED',
    'entities': [
        {
            'value': 'Entidad1',
            'synonyms': ['sinónimo1', 'sinónimo2']
        },
        {
            'value': 'Entidad2',
            'synonyms': ['sinónimo3', 'sinónimo4']
        }
    ]
}

response = requests.post(url, headers=headers, json=data)

if response.ok:
    print('Tipo de entidad creado exitosamente')
else:
    print('La solicitud falló con código de estado', response.status_code)
