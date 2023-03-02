import requests
import json

url = 'https://dialogflow.googleapis.com/v2/projects/{project_id}/agent:import'
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {api_key}'
}
body = {
    'agentUri': 'gs://bucket-name/file-name.zip'
}

response = requests.post(url.format(project_id='tu-proyecto-id'), headers=headers, json=body)

if response.ok:
    response_json = response.json()
    print('El agente se importó correctamente')
else:
    print('La solicitud falló con código de estado', response.status_code)
