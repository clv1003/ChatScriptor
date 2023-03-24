import requests

from endpoints.DatosGoogle import obtenerToken, obtenerURL

# url = 'https://dialogflow.googleapis.com/v2/projects/{project_id}/agent/entityTypes'

url = obtenerURL(4)
token = obtenerToken()

headers = {
    'Authorization': 'Bearer ' + token
}

response = requests.get(url, headers=headers)

if response.ok:
    entity_types = response.json().get('entityTypes', [])
    print(entity_types)

else:
    print('La solicitud falló con código de estado', response.status_code)
