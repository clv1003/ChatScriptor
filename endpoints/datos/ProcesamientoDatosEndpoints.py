import json
import os
import shutil
import zipfile

import requests
from flask import request
from google.cloud import dialogflow_v2 as dialogflow


# --------------------------------------------------------------------------------------------------------

# DESCOMPRIMIR EL ARCHIVO IMPORTADO
def descomprimir_archivo():
    f = request.files['archivo_zip']

    if f.filename.endswith('.zip'):
        fnombre = f.filename
        f.save(fnombre)

        with zipfile.ZipFile(fnombre, 'r') as zip_ref:
            zip_ref.extractall('unzip/' + os.path.splitext(f.filename)[0])
        os.remove(fnombre)


# EXPORTAR EL ARCHIVO INDICADO
def exportar_archivos(rootdir, name):  # rootdir = ./unzip/ ; name = Weather
    if os.path.exists(rootdir + name):
        downloads_dir = os.path.join(os.path.expanduser('~'), 'Downloads')

        if os.path.exists(downloads_dir + '/' + name + '.zip'):
            num = 1
            while os.path.exists(downloads_dir + '/' + name + '.zip') or os.path.exists(
                    downloads_dir + '/' + name + str(num) + '.zip'):
                fnombre = name + ' (' + str(num) + ')'
                num += 1

                zip_dir = shutil.make_archive(fnombre, format='zip', root_dir=rootdir + name)

                if not os.path.exists(downloads_dir + '/' + fnombre + '.zip'):
                    shutil.move(zip_dir, downloads_dir)
                    break
        else:
            zip_dir = shutil.make_archive(name, format='zip', root_dir=rootdir + name)
            shutil.move(zip_dir, downloads_dir)


# ELIMINAR EL CONTENIDO DEL DIRECTORIO TEMPORAL
def remove_unzip():
    directorio_temporal = './unzip'
    shutil.rmtree(directorio_temporal)
    os.mkdir(directorio_temporal)


# --------------------------------------------------------------------------------------------------------

def get_disponible(rootdir):
    if os.path.exists(rootdir):
        return os.listdir(rootdir)


def get_arbol(rootdir):
    arbol = {}

    for subdir, dirs, files in os.walk(rootdir):
        subdir_rel = os.path.relpath(subdir, rootdir)
        aux_arbol = arbol

        if subdir_rel != '.':
            for d in subdir_rel.split(os.sep):
                aux_arbol = aux_arbol.setdefault(d, {})

        for file in files:
            aux_arbol[file] = None

    return arbol


# --------------------------------------------------------------------------------------------------------
# OBTENCIÓN DE LOS DATOS DEL AGENTE
def get_agente(rootdir):
    if os.path.exists(rootdir + '/agent.json'):
        with open(rootdir + '/agent.json', 'r', encoding='utf-8') as a:
            agente = json.load(a)

            diccionario = {'displayName': agente['displayName'],
                           'shortDescription': agente['shortDescription'],
                           'description': agente['description'],
                           'language': agente['language'],
                           'examples': agente['examples']}

            return diccionario

    else:
        return None


def set_agente(rootdir, clave):
    valor = request.json['atributo']

    diccionario = get_agente(rootdir)
    diccionario[clave] = valor

    with open(rootdir + '/agent.json', 'w', encoding='utf-8') as a:
        json.dump(diccionario, a)


# --------------------------------------------------------------------------------------------------------

# OBTENCIÓN DE LAS ENTIDADES DEL CHATBOT
def get_entidades(rootdir):
    if os.path.exists(rootdir + '/entities'):
        archivos = os.listdir(rootdir + '/entities')
        return archivos
    else:
        return None


# OBTENCIÓN DE LOS INTENTS DEL CHATBOT
def get_intents(rootdir):
    if os.path.exists(rootdir + '/intents'):
        archivos = os.listdir(rootdir + '/intents')
        return archivos
    else:
        return None


# OBTENICIÓN DE LOS DATOS DE UNA ENTIDAD CONCRETA DEL CHATBOT
def get_entidad(rootdir):
    if os.path.exists(rootdir):
        with open(rootdir, 'r', encoding='utf-8') as e:
            entity = json.load(e)
            diccionario = {
                'Nombre': entity['name'],
                'Overridable?': entity['isOverridable'],
                'Enum?': entity['isEnum'],
                'Regexp?': entity['isRegexp'],
                'Automated Expansion?': entity['automatedExpansion'],
                'Fuzzy Extraction?': entity['allowFuzzyExtraction']
            }
            return diccionario
    else:
        return rootdir


def get_entidad_entries(rootdir):
    if os.path.exists(rootdir):
        with open(rootdir, 'r', encoding='utf-8') as e:
            entity = json.load(e)
            diccionario = {}
            c = 1
            for ent in entity:
                etiqueta = 'Entrada ' + str(c)
                diccionario[etiqueta] = ent
                c += 1
            return diccionario
    else:
        return rootdir


# OBTENCIÓN DE LOS DATOS DE UN INTENT CONCRETO DEL CHATBOT
def get_intent(rootdir):
    if os.path.exists(rootdir):
        with open(rootdir, 'r', encoding='utf-8') as i:
            inte = json.load(i)

            diccionario = {
                'Nombre': inte['name'],
                'Responses': inte['responses'],
                'Priority': inte['priority']
            }
            return diccionario
    else:
        return rootdir


def get_intent_usersays(rootdir):
    if os.path.exists(rootdir):
        with open(rootdir, 'r', encoding='utf-8') as i:
            inten = json.load(i)
            diccionario = {}
            c = 1
            for inte in inten:
                etiqueta = 'Intent ' + str(c)
                diccionario[etiqueta] = inte
                c += 1
            return diccionario
    else:
        return rootdir


# --------------------------------------------------------------------------------------------------------
# TRATAMIENTO DE LA INFORMACIÓN DE LA API DIALOGFLOW (me estoy pegando con ello)
'''
def get_chatbots(access_token, project_id):
    try:
        url_dialogflow = f'https://dialogflow.googleapis.com/v2/projects/{project_id}/agent'
        headers = {'Authorization': f'Bearer {access_token}'}
        response = requests.get(url_dialogflow, headers=headers)

        if response.status_code != 200:
            return 'Error al obtener los chatbots ' + str(response.status_code)

        chatbots = response.json().get('enableDomains', [])
        return chatbots
    except google.auth.exceptions.RefreshError:
        return None
'''

'''
def get_chatbots(access_token, project_id):
    try:
        headers = {'Authorization': f'Bearer {access_token}'}
        url = f'https://dialogflow.googleapis.com/v2/projects/{project_id}/agent'
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            bots = json.loads(response.text)
            return bots.get('enabledFeatures', [])
        else:
            return 'Error al obtener los chatbots'
    except ValueError:
        return None
'''

'''
def get_chatbots(token):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    response = requests.get(f'https://dialogflow.googleapis.com/v2/projects', headers=headers)

    if response.status_code == 200:
        projects_data = response.json()
        chatbots = []

        for project in projects_data.get('projects', []):
            project_id = project['projectId']
            display_name = project['displayName']
            chatbot = {
                'project_id': project_id,
                'display_name': display_name
            }

            chatbots.append(chatbot)

        return chatbots
    else:
        print(f'Error al obtener chatbots: {response.status_code} - {response.text}')
        return None
'''


def get_chatbots(token, project_id):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    response = requests.get(f'https://dialogflow.googleapis.com/v2/projects/{project_id}/agent',
                            headers=headers)

    if response.status_code == 200:
        agent_data = response.json()
        chatbots = {
            'project_id': agent_data['parent'].split('/')[-1],
            'display_name': agent_data['displayName']
        }
        return chatbots
    else:
        print(f'Error al obtener chatbots: {response.status_code} - {response.text}')
        return None

# -------------------------------------------------------------------------------
