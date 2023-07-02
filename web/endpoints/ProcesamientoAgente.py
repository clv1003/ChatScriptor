# IMPORTS
import os
import json

'''
PROCESAMIENTO AGENTE
@Author: Claudia Landeira

Funciones encargadas de realizar acciones sobre los datos del agente.
'''


# FUNCION --> getAgente
# Función encargada de obtener los datos del archivo agent.json
def getAgente(rootdir):
    if os.path.exists(rootdir + '/agent.json'):
        with open(rootdir + '/agent.json', 'r', encoding='utf-8') as a:
            agente = json.load(a)

            return agente

    else:
        return None


# FUNCION --> get_agente_language
# Función encargada de obtener el idioma actual del agente
def get_agente_language(rootdir, language='language'):
    agente = getAgente(rootdir)
    if language in agente:
        return agente[language]
    else:
        return None


# FUNCION --> set_agente
# Función encargada de modificar los datos del agente
def set_agente(rootdir, chat, clave, atributo):
    diccionario = getAgente(rootdir + chat)
    diccionario[clave] = atributo

    with open(rootdir + chat + '/agent.json', 'w') as a:
        json.dump(diccionario, a)
