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


# OBTENICIÓN DE LOS DATOS DE UNA ENTIDAD CONCRETA DEL CHATBOT
def get_entidad(dir_ent_parte1, dir_ent_parte2):
    if os.path.exists(dir_ent_parte1) and os.path.exists(dir_ent_parte2):
        with open(dir_ent_parte1, 'r', encoding='utf-8') as eP1, open(dir_ent_parte2, 'r', encoding='utf-8') as eP2:
            entityP1 = json.load(eP1)
            entityP2 = json.load(eP2)
            diccionario = {
                # Parte del fichero 1
                'name': entityP1['name'],
                'isOverridable': entityP1['isOverridable'],
                'isEnum': entityP1['isEnum'],
                'isRegexp': entityP1['isRegexp'],
                'automatedExpansion': entityP1['automatedExpansion'],
                'allowFuzzyExtraction': entityP1['allowFuzzyExtraction'],
                # Parte del fichero 2
                'entries': entityP2
            }
            return diccionario
    else:
        return None
