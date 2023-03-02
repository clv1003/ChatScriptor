import requests

url = 'https://dialogflow.googleapis.com/v2/projects/{project_id}/agent'
# project_id es el identificado del proyecto

headers = {
    'Authorization': 'Bearer {api_key}'
}
# api_key es la clave API que se debe obtener para autenticarse en la API

response = requests.delete(url.format(project_id='{project_id}'), headers=headers)

if response.ok:
    print('El agente se eliminó con éxito')
else:
    print('La solicitud falló con código de estado', response.status_code)
