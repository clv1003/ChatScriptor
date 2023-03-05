import requests

from endpoints.datosGoogle import obtenerToken, obtenerURL

#url = 'https://dialogflow.googleapis.com/v2/projects/{project_id}/agent:search'

url = obtenerURL(1)+':search'
token = obtenerToken()

headers = {
    'Authorization': 'Bearer ' + token
}

params = {
    'pageSize': 10,
    'query': 'nombre-del-agente'
}

response = requests.get(url, headers=headers, params=params)

if response.ok:
    search_results = response.json()
    print(search_results)
else:
    print('La solicitud falló con código de estado', response.status_code)
