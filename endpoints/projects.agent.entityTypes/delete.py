import requests

from endpoints.DatosGoogle import obtenerToken, obtenerURL


#url = 'https://dialogflow.googleapis.com/v2/projects/{project_id}/agent/entityTypes/{entity_type_id}'

url = obtenerURL(4)+'{entity_type_id}'  # ASEGURARSE DE QUE ESTO NO FALLA PQ CASI SEGURO QUE VA A EXPLOTAR
token = obtenerToken()

headers = {
    'Authorization': 'Bearer ' + token
}

response = requests.delete(url, headers=headers)

if response.ok:
    print('Tipo de entidad eliminado exitosamente')
else:
    print('La solicitud falló con código de estado', response.status_code)
