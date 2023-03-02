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
    'displayName': 'Nuevo nombre del agente',
    'description': 'Nueva descripción del agente'
}

response = requests.patch(url.format(project_id='{project_id}'), data=json.dumps(data), headers=headers)

if response.ok:
    print('El agente se ha actualizado con éxito')
else:
    print('La solicitud falló con código de estado', response.status_code)
