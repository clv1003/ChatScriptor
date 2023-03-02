import requests

url = 'https://dialogflow.googleapis.com/v2/projects/{project_id}/agent:train'

headers = {
    'Authorization': 'Bearer {api_key}',
    'Content-Type': 'application/json'
}

response = requests.post(url.format(project_id='{project_id}'), headers=headers)

if response.ok:
    print('Agente entrenado exitosamente')
else:
    print('La solicitud falló con código de estado', response.status_code)
