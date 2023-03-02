import requests
import json

url = 'https://dialogflow.googleapis.com/v2/projects/{project_id}/agent:export'

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {api_key}'
}

data = {
    'agentUri': 'projects/{project_id}/agent',
    'environment': 'draft',
    'outputUri': 'gs://{bucket_name}/{file_name}.zip'
}

response = requests.post(url.format(project_id='{project_id}'), headers=headers, data=json.dumps(data))

if response.ok:
    response_json = response.json()
    print('Operación de exportación iniciada con éxito.')
    print('ID de la operación: ', response_json.get('name', ''))
else:
    print('La solicitud falló con código de estado', response.status_code)
