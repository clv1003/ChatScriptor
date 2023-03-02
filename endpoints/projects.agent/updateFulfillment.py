import requests

url = 'https://dialogflow.googleapis.com/v2/projects/{project_id}/agent'

headers = {
    'Authorization': 'Bearer {api_key}',
    'Content-Type': 'application/json'
}

params = {
    'updateMask': 'fulfillment'
}

data = {
    'fulfillment': {
        'enabled': True,
        'serviceAccountEmail': '',
        'uri': ''
    }
}

response = requests.patch(url.format(project_id='{project_id}'), headers=headers, params=params, json=data)

if response.ok:
    print('Servicio de cumplimiento actualizado exitosamente')
else:
    print('La solicitud falló con código de estado', response.status_code)
