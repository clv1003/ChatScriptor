import requests

from endpoints.DatosGoogle import obtenerToken, obtenerURL

#url = 'https://dialogflow.googleapis.com/v2/projects/{project_id}/agent'

url = obtenerURL(1)
token = obtenerToken()

headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json'
}

params = {
    'updateMask': 'fulfillment'
}

data = {
    'fulfillment': {
        'enabled': True,
        'serviceAccountEmail': '',
        'uri': ''
    }
}

response = requests.patch(url, headers=headers, params=params, json=data)

if response.ok:
    print('Servicio de cumplimiento actualizado exitosamente')
else:
    print('La solicitud falló con código de estado', response.status_code)
