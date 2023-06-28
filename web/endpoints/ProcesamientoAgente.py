import os
import json


# OBTENCIÓN DE LOS DATOS DEL AGENTE
def getAgente(rootdir):
    if os.path.exists(rootdir + '/agent.json'):
        with open(rootdir + '/agent.json', 'r', encoding='utf-8') as a:
            agente = json.load(a)

            return agente

    else:
        return None


# OBTENCIÓN DEL IDIOMA DEL AGENTE
def get_agente_language(rootdir, language='language'):
    agente = getAgente(rootdir)
    if language in agente:
        return agente[language]
    else:
        return None


# --------------------------------------------------------------------------------------------------
# MODIFICACIÓN DE LOS DATOS DEL AGENTE ./usuarios/usuario1@correo.com/Weather
def set_agente(rootdir, chat, clave, atributo):
    #if clave == 'displayName':
    #    n_nombre = rootdir + atributo
    #else:
    #    n_nombre = rootdir + chat
    diccionario = getAgente(rootdir + chat)
    diccionario[clave] = atributo

    with open(rootdir + chat + '/agent.json', 'w') as a:
        json.dump(diccionario, a)
    #    os.rename(rootdir + chat, n_nombre)
