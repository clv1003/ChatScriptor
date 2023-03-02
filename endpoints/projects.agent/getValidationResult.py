import requests
import json

url = 'https://dialogflow.googleapis.com/v2/projects/{project_id}/agent/validationResult'

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {api_key}'
}

response = requests.get(url.format(project_id='{project_id}'), headers=headers)

if response.ok:
    response_json = response.json()
    validation_errors = response_json.get('validationErrors', [])

    print('Número de errores de validación:', len(validation_errors))

    for error in validation_errors:
        print('Mensaje:', error.get('errorMessage', ''))
        print('Descripción:', error.get('description', ''))
else:
    print('La solicitud falló con código de estado', response.status_code)
