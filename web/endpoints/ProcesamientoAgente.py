import os
import json

from flask import request


# OBTENCIÓN DE LOS DATOS DEL AGENTE
def get_agente(rootdir):
    if os.path.exists(rootdir + '/agent.json'):
        with open(rootdir + '/agent.json', 'r', encoding='utf-8') as a:
            agente = json.load(a)

            return agente

    else:
        return None


# OBTENCIÓN DEL IDIOMA DEL AGENTE
def get_agente_language(rootdir, language='language'):
    agente = get_agente(rootdir)
    if language in agente:
        return agente[language]
    else:
        return None


# --------------------------------------------------------------------------------------------------
# MODIFICACIÓN DE LOS DATOS DEL AGENTE
def set_agente(rootdir, clave, atributo):

    diccionario = get_agente(rootdir)
    diccionario[clave] = atributo

    with open(rootdir + '/agent.json', 'w') as a:
        json.dump(diccionario, a)
