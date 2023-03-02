import requests

url = 'https://dialogflow.googleapis.com/v2/projects/{project_id}/agent/entityTypes'

headers = {
    'Authorization': 'Bearer {api_key}'
}

response = requests.get(url.format(project_id='{project_id}'), headers=headers)

if response.ok:
    response_json = response.json()
    entity_types = response_json.get('entityTypes', [])

    for entity_type in entity_types:
        print(entity_type.get('displayName'))
else:
    print('La solicitud falló con código de estado', response.status_code)
