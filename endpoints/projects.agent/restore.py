import requests

url = 'https://dialogflow.googleapis.com/v2/projects/{project_id}/agent:restore'

headers = {
    'Authorization': 'Bearer {api_key}',
    'Content-Type': 'application/json'
}
data = {
    'agentContent': 'contenido-del-agente-restaurado',
}

response = requests.post(url.format(project_id='{project_id}'), headers=headers, json=data)

if response.ok:
    print('Agente restaurado exitosamente')
else:
    print('La solicitud falló con código de estado', response.status_code)
