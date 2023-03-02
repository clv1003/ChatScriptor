import requests
import json

url = 'https://dialogflow.googleapis.com/v2/projects/{project_id}/agent/fulfillment'

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {api_key}'
}

response = requests.get(url.format(project_id='{project_id}'), headers=headers)

if response.ok:
    response_json = response.json()
    fulfillment = response_json.get('fulfillment', {})
    print('URL del servicio de Fulfillment:', fulfillment.get('uri', ''))
    print('Habilitación de la autenticación:', fulfillment.get('enabled', ''))
else:
    print('La solicitud falló con código de estado', response.status_code)
