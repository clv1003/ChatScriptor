import json
import os

import ProcesamientoAgente


# OBTENCIÓN DE LAS ENTIDADES DEL CHATBOT
def get_entidades(rootdir):
    if os.path.exists(rootdir + '/entities'):
        language = ProcesamientoAgente.get_agente_language(rootdir)
        archivos = os.listdir(rootdir + '/entities')
        agrupados = []

        for archivo in archivos:
            if archivo.endswith('.json'):
                entity = archivo.replace('.json', '')
                entries = entity + '_entries_' + language + '.json'
                if entries in archivos:
                    agrupados.append([archivo, entries])

        return agrupados
    else:
        return None


# OBTENCIÓN DE LOS INTENTS DEL CHATBOT
def get_intents(rootdir):
    if os.path.exists(rootdir + '/intents'):
        language = ProcesamientoAgente.get_agente_language(rootdir)
        archivos = os.listdir(rootdir + '/intents')
        agrupados = []

        for archivo in archivos:
            if archivo.endswith('.json'):
                intent = archivo.replace('.json', '')
                usersays = intent + '_usersays_' + language + '.json'
                if usersays in archivos:
                    agrupados.append([archivo, usersays])

        return agrupados
    else:
        return None


def get_json(parte1, parte2):
    if os.path.exists(parte1) and os.path.exists(parte2):
        with open(parte1, 'r', encoding='utf-8') as iP1, open(parte2, 'r', encoding='utf-8') as iP2:
            part1 = json.load(iP1)
            part2 = json.load(iP2)

            return [part1, part2]
    else:
        return None
