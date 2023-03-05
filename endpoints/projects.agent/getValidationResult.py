import requests

from endpoints.datosGoogle import obtenerToken, obtenerURL

#url = 'https://dialogflow.googleapis.com/v2/projects/{project_id}/agent/validationResult'

url = obtenerURL(3)
token = obtenerToken()

headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers)

if response.ok:
    response_json = response.json()
    validation_errors = response_json.get('validationErrors', [])

    print('Número de errores de validación:', len(validation_errors))

    for error in validation_errors:
        print('Mensaje:', error.get('errorMessage', ''))
        print('Descripción:', error.get('description', ''))
else:
    print('La solicitud falló con código de estado', response.status_code)
