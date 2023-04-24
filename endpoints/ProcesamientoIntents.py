import json
import os
import ProcesamientoAgente


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


# OBTENCIÓN DE LOS DATOS DE UN INTENT CONCRETO DEL CHATBOT
def get_intent(dir_int_parte1, dir_int_parte2):
    if os.path.exists(dir_int_parte1) and os.path.exists(dir_int_parte2):
        with open(dir_int_parte1, 'r', encoding='utf-8') as iP1, open(dir_int_parte2, 'r', encoding='utf-8') as iP2:
            intentP1 = json.load(iP1)
            intentP2 = json.load(iP2)

            diccionario = {
                # Parte del fichero 1
                'name': intentP1['name'],
                'responses': intentP1['responses'],
                'priority': intentP1['priority'],
                # Parte del fichero 2
                'usersays': intentP2
            }
            return diccionario
    else:
        return None
