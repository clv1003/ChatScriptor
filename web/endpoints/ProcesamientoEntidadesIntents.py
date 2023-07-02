# IMPORTS
import json
import os
import re

from web.endpoints.ProcesamientoAgente import get_agente_language

'''
PROCESAMIENTO ENTIDADES/INTENTS
@Author: Claudia Landeira

Funciones encargadas de realizar los procesamientos de la informacion de entidades e intents
'''


# FUNCION --> getEntidades
# Función encargada de obtener las entidades disponibles de un chatbot
def getEntidades(rootdir, language=None):
    if os.path.exists(rootdir + '/entities'):
        if language is None:
            language = get_agente_language(rootdir)

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


# FUNCION --> getIntents
# Función encargada de obtener los intents disponibles de un chatbot
def getIntents(rootdir, language=None):
    if os.path.exists(rootdir + '/intents'):
        if language is None:
            language = get_agente_language(rootdir)

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


# FUNCION --> get_json
# Función encargada de juntar los dos archivos que conforma una entidad o un intent
def get_json(parte1, parte2):
    part1 = get_parte(parte1)
    part2 = get_parte(parte2)

    return [part1, part2]


# FUNCION --> get_parte
# Función encargada de leer los archivos json de entidades e intents
def get_parte(parte):
    if os.path.exists(parte):
        with open(parte, 'r', encoding='utf-8') as p:
            p = json.load(p)

            return p
    else:
        return None


# FUNCION --> directoriosEntidad
# Función encargada de obtener los directorios de las entidades
def directoriosEntidad(root, entidad, language=None):
    if entidad.endswith('.json'):
        entries1 = entidad
        if language is None:
            language = get_agente_language(root)
        entidad = entidad.replace('.json', '')
        entries2 = entidad + '_entries_' + language + '.json'

        ent = [root + '/entities/' + entries1, root + '/entities/' + entries2]
        return ent


# FUNCION --> directoriosIntent
# Función encargada de obtener los directorios de los intents
def directoriosIntent(root, intent, language=None):
    if intent.endswith('.json'):
        intent1 = intent
        if language is None:
            language = get_agente_language(root)
        intent = intent.replace('.json', '')
        intent2 = intent + '_usersays_' + language + '.json'

        inte = [root + '/intents/' + intent1, root + '/intents/' + intent2]
        return inte


# FUNCION --> editar_nombre
# Función encargada de editar el nombre de entidad o intent (primer archivo que conforma o la entidad o el intent)
def editar_nombre(root, clave, atributo):
    diccionario = get_parte(root)
    diccionario[clave] = atributo

    with open(root, 'w') as e:
        json.dump(diccionario, e)


# FUNCION --> removeEntidad
# Función encargada de eliminar una entidad
def removeEntidad(root, chat, entidad, language=None):
    rootdir = root + chat + '/entities/'

    os.remove(rootdir + entidad)

    if language is None:
        language = get_agente_language(root + chat)

    e = entidad.replace('.json', '')
    enti = e + '_entries_' + language + '.json'
    os.remove(rootdir + enti)


# FUNCION --> removeIntent
# Función encargada de eliminar un intent
def removeIntent(root, chat, intent, language=None):
    rootdir = root + chat + '/intents/'

    os.remove(rootdir + intent)

    if language is None:
        language = get_agente_language(root + chat)

    i = intent.replace('.json', '')
    inte = i + '_usersays_' + language + '.json'
    os.remove(rootdir + inte)


# FUNCION --> editar_v_ent
# Función encargada de modificar los valores de una entrada de una entidad
def editar_v_ent(root, value, entidad, atributo, language=None):
    if entidad.endswith('.json'):
        if language is None:
            language = get_agente_language(root)

        entidad = entidad.replace('.json', '')
        entries = entidad + '_entries_' + language + '.json'

        diccionario = get_parte(root + '/entities/' + entries)

        for d in diccionario:
            if d["value"] == value:
                d["value"] = atributo

        with open(root + '/entities/' + entries, 'w') as e:
            json.dump(diccionario, e)


# FUNCION --> editar_s_ent
# Función encargada de modificar los sinonimos de una entrada de una entidad
def editar_s_ent(root, value, entidad, atributo, language=None):
    if entidad.endswith('.json'):
        if language is None:
            language = get_agente_language(root)

        entidad = entidad.replace('.json', '')
        entries = entidad + '_entries_' + language + '.json'

        diccionario = get_parte(root + '/entities/' + entries)

        for d in diccionario:
            if d["value"] == value:
                d["synonyms"] = atributo

        with open(root + '/entities/' + entries, 'w') as e:
            json.dump(diccionario, e)


# FUNCION --> addEntry
# Función encargada de añadir una entrada a una entidad
def addEntry(root, entidad, value, synonyms, language=None):
    if entidad.endswith('.json'):
        if language is None:
            language = get_agente_language(root)

        entidad = entidad.replace('.json', '')
        entries = entidad + '_entries_' + language + '.json'

        diccionario = get_parte(root + '/entities/' + entries)
        aux = {"value": value.split()[0], "synonyms": re.findall(r"'(.*?)'", synonyms)}

        diccionario.append(aux)

        with open(root + '/entities/' + entries, 'w') as e:
            json.dump(diccionario, e)


# FUNCION --> removeEntry
# Función encargada de eliminar una entrada a una entidad
def removeEntry(root, entidad, value, language=None):
    if entidad.endswith('.json'):
        if language is None:
            language = get_agente_language(root)

        entidad = entidad.replace('.json', '')
        entries = entidad + '_entries_' + language + '.json'

        diccionario = get_parte(root + '/entities/' + entries)
        for d in diccionario:
            if d["value"] == value.split()[0]:
                diccionario.remove(d)

        with open(root + '/entities/' + entries, 'w') as e:
            json.dump(diccionario, e)


# FUNCION --> addMessages
# Función encargada de añadir a los intents el parametros speech(respuesta) de la etiqueta messages
def addMessages(root, speach):
    diccionario = get_parte(root)

    if 'speech' in diccionario["responses"][0]["messages"][0]:
        diccionario["responses"][0]["messages"][0]["speech"].append(speach)
    else:
        diccionario["responses"][0]["messages"][0]["speech"] = []
        diccionario["responses"][0]["messages"][0]["speech"].append(speach)

    with open(root, 'w') as i:
        json.dump(diccionario, i)


# FUNCION --> editar_messages
# Función encargada de modificar el parametros speech(respuesta) de la etiqueta messages de los intents
def editar_messages(root, speachOrg, speachNew):
    diccionario = get_parte(root)
    if diccionario["responses"][0]["messages"]:
        lista = []
        for j in diccionario["responses"][0]["messages"][0]["speech"]:
            if j == speachOrg:
                lista.append(speachNew)
            else:
                lista.append(j)

        diccionario["responses"][0]["messages"][0]["speech"] = lista

        with open(root, 'w') as i:
            json.dump(diccionario, i)


# FUNCION --> removeMessages
# Función encargada de eliminar el parametros speech(respuesta) de la etiqueta messages de los intents
def removeMessages(root, speech):
    diccionario = get_parte(root)
    lista = []

    for j in diccionario["responses"][0]["messages"][0]["speech"]:
        if j != speech:
            lista.append(j)

    diccionario["responses"][0]["messages"][0]["speech"] = lista

    with open(root, 'w') as i:
        json.dump(diccionario, i)


# FUNCION --> editar_parameters
# Función encargada de editar los parametros de las responses (frases de entrenamiento) de los intents
def editar_parameters(root, subclave, atributo):
    diccionario = get_parte(root)
    for i in diccionario["responses"][0]["parameters"]:
        if subclave in i:
            i[subclave] = atributo

    with open(root, 'w') as i:
        json.dump(diccionario, i)


# FUNCION --> editar_action
# Función encargada de eliminar parametros de los intents mediante ID
def removeParameters(root, idR):
    diccionario = get_parte(root)

    for i in diccionario["responses"][0]["parameters"]:
        if i["id"] == idR:
            diccionario["responses"][0]["parameters"].remove(i)
            break

    with open(root, 'w') as i:
        json.dump(diccionario, i)


# FUNCION --> editar_action
# Función encargada de editar el parametro action de las responses (frases de entrenamiento) de los intents
def editar_action(root, atributo):
    diccionario = get_parte(root)
    if diccionario["responses"][0]["action"]:
        diccionario["responses"][0]["action"] = atributo

        with open(root, 'w') as i:
            json.dump(diccionario, i)


# FUNCION --> editar_data
# Función encargada de editar data de los intents (segundo archivo de los intents)
def editar_data(root, intent, old, tipo, atributo, language=None):
    if intent.endswith('.json'):
        stopflag = False
        if language is None:
            language = get_agente_language(root)
        intent = intent.replace('.json', '')
        data = intent + '_usersays_' + language + '.json'

        diccionario = get_parte(root + '/intents/' + data)

        for dt in diccionario:
            for d in dt["data"]:
                if len(d) == 2 and tipo == "text":
                    if d[tipo] == old:
                        d[tipo] = atributo
                        stopflag = True
                        break
                elif len(d) != 2 and (tipo == 'meta' or tipo == 'alias'):
                    if d[tipo] == old:
                        d[tipo] = atributo
                        stopflag = True
                        break

            if stopflag:
                break

        with open(root + '/intents/' + data, 'w') as i:
            json.dump(diccionario, i)


# FUNCION --> removeData
# Función encargada de eliminar data de los intents (segundo archivo de los intents)
def removeData(root, intent, idD, language=None):
    if intent.endswith('.json'):
        if language is None:
            language = get_agente_language(root)
        intent = intent.replace('.json', '')
        data = intent + '_usersays_' + language + '.json'

        diccionario = get_parte(root + '/intents/' + data)

        for i in diccionario:
            if i["id"] == idD:
                diccionario.remove(i)
                break

        with open(root + '/intents/' + data, 'w') as i:
            json.dump(diccionario, i)
