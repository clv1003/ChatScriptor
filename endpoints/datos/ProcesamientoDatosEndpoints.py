import json
import os
import shutil
import zipfile

from flask import request
import google.cloud.dialogflow_v2 as dialogflow


def descomprimir_archivo():
    f = request.files['archivo_zip']

    if f.filename.endswith('.zip'):
        fnombre = f.filename
        f.save(fnombre)

        with zipfile.ZipFile(fnombre, 'r') as zip_ref:
            zip_ref.extractall('unzip/' + os.path.splitext(f.filename)[0])
        os.remove(fnombre)


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


def get_agente(rootdir):
    if os.path.exists(rootdir + '/agent.json'):
        with open(rootdir + '/agent.json', 'r', encoding='utf-8') as a:
            agente = json.load(a)

            diccionario = {'Nombre': agente['displayName'],
                           'Descripción corta': agente['shortDescription'],
                           'Descripción': agente['description'],
                           'Idioma': agente['language'],
                           'Ejemplos': agente['examples']}

            return diccionario

    else:
        return None


def get_entidades(rootdir):
    if os.path.exists(rootdir + '/entities'):
        archivos = os.listdir(rootdir + '/entities')
        dicEntidades = {}

        for entK, entV in zip(archivos[::2], archivos[1::2]):
            dicEntidades[entK] = entV

        return dicEntidades
    else:
        return None


def get_entidad():
    return


def get_intents(rootdir):
    if os.path.exists(rootdir + '/intents'):
        archivos = os.listdir(rootdir + '/intents')
        dicIntents = {}

        for intK, intV in zip(archivos[::2], archivos[1::2]):
            dicIntents[intK] = intV

        return archivos
    else:
        return None


def get_intent():
    pass


def remove_unzip():
    directorio_temporal = './unzip'
    shutil.rmtree(directorio_temporal)
    os.mkdir(directorio_temporal)


# -------------------------------------------------------------------------------

def get_chatbots(project_id, credenciales):
    session_client = dialogflow.SessionsClient(credentials=credenciales)
    parent = f'projects/{project_id}/agent'
    response = session_client.list_entity_types(parent=parent)

    chatbots = []
    for c in response:
        chatbots.append(c)

    return chatbots
