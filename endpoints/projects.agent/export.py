import requests
import json

from endpoints.DatosGoogle import obtenerToken, obtenerURL

#url = 'https://dialogflow.googleapis.com/v2/projects/{project_id}/agent:export'

url = obtenerURL(1)+':export'
token = obtenerToken()

headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json'
}

data = {
    'agentUri': 'projects/tfg-dialogflow-clv/agent',
    'environment': 'draft',
    'outputUri': 'gs://{bucket_name}/{file_name}.zip'  # no se muy bien como se determinan estas etiquetas
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.ok:
    response_json = response.json()
    print('Operación de exportación iniciada con éxito.')
    print('ID de la operación: ', response_json.get('name', ''))
else:
    print('La solicitud falló con código de estado', response.status_code)
