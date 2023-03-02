import requests

url = 'https://dialogflow.googleapis.com/v2/projects/{project_id}/agent:search'

headers = {
    'Authorization': 'Bearer {api_key}'
}
params = {
    'pageSize': 10,
    'query': 'nombre-del-agente'
}

response = requests.get(url.format(project_id='{project_id}'), headers=headers, params=params)

if response.ok:
    search_results = response.json()
    print(search_results)
else:
    print('La solicitud falló con código de estado', response.status_code)
