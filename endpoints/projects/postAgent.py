import requests
import json

# PARA ACTUALIZAR EL AGENTE

url = 'https://dialogflow.googleapis.com/v2/projects/{project_id}/agent'
# project_id es el identificado del proyecto

headers = {
    'Authorization': 'Bearer {api_key}',
    'Content-Type': 'application/json'
}
# api_key es la clave API que se debe obtener para autenticarse en la API

data = {
    'displayName': 'Nombre del agente',
    'defaultLanguageCode': 'es',
    'timeZone': 'Europe/Paris',
    'description': 'Descripción del agente'
}

response = requests.post(url.format(project_id='{project_id}'), data=json.dumps(data), headers=headers)

if response.ok:
    response_json = response.json()
    print('Nombre del agente: ', response_json.get('displayName', ''))
    print('ID del agente: ', response_json.get('name', ''))
else:
    print('La solicitud falló con código de estado', response.status_code)
