import requests

from endpoints.datosGoogle import obtenerToken, obtenerURL

#url = 'https://dialogflow.googleapis.com/v2/projects/{project_id}/agent/fulfillment'

url = obtenerURL(2)
token = obtenerToken()

headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers)

if response.ok:
    response_json = response.json()
    fulfillment = response_json.get('fulfillment', {})
    print('URL del servicio de Fulfillment:', fulfillment.get('uri', ''))
    print('Habilitación de la autenticación:', fulfillment.get('enabled', ''))
else:
    print('La solicitud falló con código de estado', response.status_code)
