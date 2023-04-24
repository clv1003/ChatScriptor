import os
import json

from flask import request


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


def get_agente_language(rootdir, language='language'):
    agente = get_agente(rootdir)
    if language in agente:
        return agente[language]
    else:
        return None


def set_agente(rootdir, clave):
    valor = request.json['atributo']

    diccionario = get_agente(rootdir)
    diccionario[clave] = valor

    with open(rootdir + '/agent.json', 'w', encoding='utf-8') as a:
        json.dump(diccionario, a)
