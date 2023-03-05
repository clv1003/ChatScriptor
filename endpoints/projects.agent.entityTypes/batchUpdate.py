import requests

from endpoints.datosGoogle import obtenerToken, obtenerURL

#url = 'https://dialogflow.googleapis.com/v2/projects/{project_id}/agent/entityTypes:batchUpdate'

url = obtenerURL(4)+':batchUpdate'
token = obtenerToken()

headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json'
}

data = {
    'entityTypeBatchInline': {
        'entityTypes': [
            {
                'name': 'projects/tfg-dialogflow-clv/agent/entityTypes/{entity_type_id1}',
                'displayName': 'Nuevo nombre tipo entidad 1',
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
            },
            {
                'name': 'projects/tfg-dialogflow-clv/agent/entityTypes/{entity_type_id2}',
                'displayName': 'Nuevo nombre tipo entidad 2',
                'entities': [
                    {
                        'value': 'Entidad3',
                        'synonyms': ['sinónimo5', 'sinónimo6']
                    },
                    {
                        'value': 'Entidad4',
                        'synonyms': ['sinónimo7', 'sinónimo8']
                    }
                ]
            },
            {
                'name': 'projects/tfg-dialogflow-clv/agent/entityTypes/{entity_type_id3}',
                'displayName': 'Nuevo nombre tipo entidad 3',
                'entities': [
                    {
                        'value': 'Entidad5',
                        'synonyms': ['sinónimo9', 'sinónimo10']
                    },
                    {
                        'value': 'Entidad6',
                        'synonyms': ['sinónimo11', 'sinónimo12']
                    }
                ]
            }
        ]
    }
}

response = requests.post(url, headers=headers, json=data)

if response.ok:
    print('Tipos de entidad actualizados exitosamente')
else:
    print('La solicitud falló con código de estado', response.status_code)
