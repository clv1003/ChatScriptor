import requests

from endpoints.datosGoogle import obtenerToken, obtenerURL

# url = 'https://dialogflow.googleapis.com/v2/projects/{project_id}/agent/environments'

url = obtenerURL(5)
token = obtenerToken()

headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json'
}

response = requests.delete(url, headers=headers)

if response.ok:
    print('El environment se eliminó con éxito')
else:
    print('La solicitud falló con código de estado', response.status_code)
