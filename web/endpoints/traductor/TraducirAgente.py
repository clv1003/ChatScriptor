
import os.path
from web.endpoints.ProcesamientoAgente import *


def traducirAgente(traductor, rootdir, chat):
    if os.path.exists(rootdir + chat):
        agente = getAgente(rootdir + chat)

        print(f'')
        print("\033[91m ---------------------------- AGENTE \033[0m")

        diccionario = {}

        if agente['displayName'] != "":
            diccionario['displayName'] = agente['displayName']

        if agente['shortDescription'] != "":
            diccionario['shortDescription'] = agente['shortDescription']

        if agente['description'] != "":
            diccionario['description'] = agente['description']

        if agente['examples'] != "":
            diccionario['examples'] = agente['examples']

        tr_diccionario = traductor.traducirDiccionario(diccionario)

        if 'displayName' in tr_diccionario.keys():
            set_agente(rootdir, chat, 'displayName', tr_diccionario['displayName'])
            print("\033[92m -> OK! - Modificado displayName \033[0m")

        if 'shortDescription' in tr_diccionario.keys():
            set_agente(rootdir, chat, 'shortDescription', tr_diccionario['shortDescription'])
            print("\033[92m -> OK! - Modificado shortDescription \033[0m")

        if 'description' in tr_diccionario.keys():
            set_agente(rootdir, chat, 'description', tr_diccionario['description'])
            print("\033[92m -> OK! - Modificado description \033[0m")

        if 'examples' in tr_diccionario.keys():
            set_agente(rootdir, chat, 'examples', tr_diccionario['examples'])
            print("\033[92m -> OK! - Modificado examples2 \033[0m")

        set_agente(rootdir, chat, 'language', traductor.getIdioma())
        print("\033[92m -> OK! - Modificado idioma \033[0m")
